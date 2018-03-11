#!/bin/bash

num=$(python get_number_of_playlists.py)

for ((i=1; i<=num;i++))
do
    echo $i
done
