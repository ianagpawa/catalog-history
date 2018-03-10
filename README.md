# Catalog History Archive

##### This repo is for my catalog history script.  This script retrieves and stores JSON info from my music catalog, and acts as a simple archive system.      


### Quick Start
-Clone the repo: `git clone https://github.com/ianagpawa/catalog-history-archive.git`


#### Dependencies
This app requires `python2.7` to be installed on your system.


#### Deployment
When using command `gcloud app deploy` to deploy, file `index.yaml` is not automatically updated.  Use the following command to upload the index file manually:
`gcloud datastore create-indexes index.yaml`

To see the status of present indexes, visit the following site:
[Datastore Indexes](https://appengine.google.com/datastore/indexes)


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
