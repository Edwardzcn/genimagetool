#! /bin/bash

# This is my first shell script
# Use it to delete the image

d=`date +%Y/%m/%d_%H:%M:%S`
echo "The script begin at $d"

cd ./static/images

for file in `ls gen*.jpg`;do rm -rf $file;done;
