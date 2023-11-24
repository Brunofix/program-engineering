#!/bin/bash
#
echo "Cleaning previous files"
rm -rf levarino
# Pull upstream repo
echo "Cloning repo"
git clone https://gitlab.com/levara/se-labs-2324-sr.git levarino

echo "Moving files"
rm -rf myimgur
cp -r levarino/lab6/myimgor myimgur
echo "Cleaning up"
rm -rf levarino


