# Catalog History Archive

##### This repo is for my catalog history archive script.  This script retrieves and stores JSON info from my music catalog and acts as a simple archive system.  The JSON objects are decoded and stored in text files located in archive under timestamped folders.


## Quick Start
Clone the repo: `git clone https://github.com/ianagpawa/catalog-history-archive.git`


### Dependencies
This app requires `python2.7` to be installed on your system.


## Use
While the terminal is in the project folder:

### To Archive All Playlists
To retrieve and store info regarding all instances of class `Playlist`, run the following command:
```
$ python get_all_playlists.py
```

#### To Archive An Individual Playlist
To retrieve and store info regarding a particular playlist, run the following command with the *PLAYLIST_NAME*:
```
$ python get_playlist.py *PLAYLIST_NAME*
```

### File structure
Within the project folder, you will find the following files:

```
catalog-history-archive/
    ├── archive/
    |    └── TIMESTAMP_FOLDER/
    |        └──  FILES
    ├── rebuilt/
    |    └── EMPTY FOR NOW
    ├── .gitignore
    ├── main.py
    ├── notes.txt
    └── README.md
```

## Creator

**Ian Agpawa**


[Github](https://github.com/ianagpawa)

 agpawaji@gmail.com
