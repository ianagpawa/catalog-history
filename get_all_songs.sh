#!/bin/bash

# python get_all_playlists.py

num=$(python get_number_of_playlists.py)


for ((i=1; i<=num;i++))
do
    python get_playlist.py $i
done
