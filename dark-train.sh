#!/bin/bash

cd ~/dev/darknet
./darknet detector train data/weapons/weapon.data cfg/yolov3-weapon.cfg models/darknet53.conv.74 -dont_show |& tee /dev/stderr 2> /tmp/darknet.log | grep --line-buffered images > loss.log
