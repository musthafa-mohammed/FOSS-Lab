#!/bin/sh
rename 'y/A-Z/a-z/' *
for file in *
do
 #echo $file
 #mv "$file" ""
 rename "s/\s+//g" *
done
