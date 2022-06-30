---
title: "Ubuntu CMD"
date: 2020-08-26 16:11:38 +0900
categories: programming
tags: ubuntu command
---

- rename all files starting with letter "n" to "00", \n

  `mmv n\* 00\#1`

- bulk rename file (rename all file with 'data3d' to ''

  `mmv '*data3d*' '#1#2'`

- bulk rename file (rename all file with '-LUL' to '\_gt1'

  `mmv '*-LUL*' '#1_gt1#2'`

- move mip files inside test folder

  `find ./test/ -type f -name '*.mip' -exec mv -i {} ./test/ \;`

- to move a whole directory and its content:

  `mv includes/* ./`

- to copy files recursively

  `cp -R includes/ includes_backup/`

- Change the group of /u and subfiles to "staff"

  `chgrp -R staff /u`

- ssh connection

  `ssh -p 7722 kevin@192.168.0.6`

  `sftp -oPort=7722 kevin@192.168.0.6`

- Transferring Remote Files to the Local System

  `get -r someDirectory`

- Transferring Local Files to the Remote System

  `put -r localDirectory`

- find directories or folder with given patern and save to txt (use '>>' to append)

  `find ./ -type d -name "LSTA" > LSTA.txt`

  `find . -type f -name "*.DC3" > DC3.txt`

- find files without printing error message

  `find ./ -type f -name '33851556_20150316.nii' 2>/dev/null`

- Find file ignoring subdirectories then copy

  `find . -maxdepth 1 -type f -name "*.mp3" -exec cp {} /tmp/MusicFiles \;`

- Find directory then copy

  `find . -maxdepth 1 -type d -name "07787733_20170304" -exec cp -r {} "/home/Documents" \;`

- Mount directory over ssh

```shell
sudo apt update

sudo apt install sshfs

mkdir ~/Documents/folder

sshfs kevin@192.168.0.6:/ ~/Documents/folder/

fusermount -u ~/Documents/folder
```

- Mount network location (tried under WSL)

```shell
  sudo mkdir /mnt/share

  sudo mount -t drvfs '\\server\share' /mnt/share

  sudo mount -t drvfs D: /mnt/d
```

- print directory structure

```shell
  sudo apt-get install tree

  tree -d /path/to/folder
```
