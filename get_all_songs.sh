#!/bin/bash

num=$(python get_number_of_playlists.py)

i=1

while [ $i -lt $num ]
do
    echo $i
    i=$[$i+1]
done
