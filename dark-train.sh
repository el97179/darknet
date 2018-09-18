#!/bin/bash

cd ~/dev/darknet
./darknet detector train data/weapons/3-weapons.data cfg/yolov3-3-weapons.cfg models/darknet53.conv.74 -dont_show |& tee /dev/stderr 2> /tmp/darknet.log | grep --line-buffered images > loss.txt
