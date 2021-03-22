# py-sync
rsync via python for ease of configuration

## Requirements
* Python 3 - this script has not been fully tested on Python 2
* [Python pip](https://pip.pypa.io/en/stable/installing/)


## Installation

Using git:
```
cd
git clone https://github.com/rycolos/py-sync.git
cd py-sync
```
Using wget:
```
cd
wget https://github.com/rycolos/py-sync/archive/master.zip
unzip master.zip
cd py-sync-master
```
Install dependencies:
```
pip install -r requirements.txt
```

## Configuration
Remove `.template` from the `py-sync.conf.template` config file and update per your local and backup path on the same machine or per your backup path on a remote system.

```
#THIS SCRIPT MUST BE RUN ON THE LOCAL MACHINE

[input_paths] #separate by comma, no space. trailing slash only copies content and not directory level
input_paths = /Users/PATH,/Users/PATH

[output_path] #directory must already exist
output_path = user@PATH.local:/PATH

[backup_path]
backup_path = user@PATH.local:/PATH/deleted

[exclude_paths] #requires disable_relative_path enabled. separate by comma, no space. use full path name.
exclude_paths = 

[arguments] #1 enabled, 0 disabled
delete_from_dest = 1
use_relative_path = 1
backup_deleted_dest = 1

#arguments explained (if enabled):
#delete_from_dest -- if files are deleted at source, also delete at destination
#use_relative_path -- full source path names are copied to destination
#backup_deleted_dest -- if a file is deleted at destination, copy to this folder on destination
```

## Usage
Ensure your py-syn.conf file has been updated and run the script:
```
python3 py-sync.py
```
