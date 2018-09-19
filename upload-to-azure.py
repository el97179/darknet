# ----------------------------------------------------------------------------------
# MIT License
#
# Copyright(c) Microsoft Corporation. All rights reserved.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# ----------------------------------------------------------------------------------
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.



import os, uuid, sys
from azure.storage.blob import BlockBlobService, PublicAccess

# ---------------------------------------------------------------------------------------------------------
# Method that creates a test file in the 'Documents' folder.
# This sample application creates a test file, uploads the test file to the Blob storage,
# lists the blobs in the container, and downloads the file with a new name.
# ---------------------------------------------------------------------------------------------------------
# Documentation References:
# Associated Article - https://docs.microsoft.com/en-us/azure/storage/blobs/storage-quickstart-blobs-python
# What is a Storage Account - http://azure.microsoft.com/en-us/documentation/articles/storage-whatis-account/
# Getting Started with Blobs-https://docs.microsoft.com/en-us/azure/storage/blobs/storage-python-how-to-use-blob-storage
# Blob Service Concepts - http://msdn.microsoft.com/en-us/library/dd179376.aspx
# Blob Service REST API - http://msdn.microsoft.com/en-us/library/dd135733.aspx
# ----------------------------------------------------------------------------------------------------------


def run_sample(argv):
    try:
        # Create the BlockBlockService that is used to call the Blob service for the storage account
        block_blob_service = BlockBlobService(account_name='tdwmlmodels', account_key='i2YgBbapUGRVgWesufo3h4Y9ozPNWz5zU6bmydPo5UM++kQ+Ju8XWMeEgUhGcM23d++u9jarlVCO2RLIWeiMrw==')

        # Create a container called 'quickstartblobs'.
        if (len(argv) == 3):
            container_name = argv[2]
        else:
            container_name ='tmp'
        block_blob_service.create_container(container_name)

        # Set the permission so the blobs are public.
        block_blob_service.set_container_acl(container_name, public_access=PublicAccess.Container)

        # Upload all files which are inside the drectory provided as input
        if (len(argv) == 1):
            print("How to use this script? Provide as input arguments the full folder path which contents will be uploaded and (optionally) the name of the container in azure")
            print("e.g.: python upload_to_azure.py /home/tanman/dev/darknet/backup models")
            return
        else:
            folder = argv[1]
        files_list = os.listdir(folder)
        for filename in files_list:
            filepath = folder + "/" + filename
            if os.path.isdir(filepath):
                print("skipping directory " + filepath)
                continue
            print("\nUploading to Blob storage as blob: " + filepath)
            block_blob_service.create_blob_from_path(container_name, filename, filepath)

        # List the blobs in the container
        print("\nList blobs in the container")
        generator = block_blob_service.list_blobs(container_name)
        for blob in generator:
            print("\t Blob name: " + blob.name)

    except Exception as e:
        print(e)


# Main method.
if __name__ == '__main__':
    print(sys.argv)
    print(len(sys.argv))
    run_sample(sys.argv)



