# MassMover

Simple Python script for moving large amounts of files

uses Python3

---

- [x] recursive

- [ ] advanced filters

---

## Requirements

Python 3.x.x



---

## Usage:

usage: MassMover [-h] [-p] [-v] [-A] [-a] [-l] [-q] [-m] [-r] [-H] start dest

Copies all Files from all subdirectories into the destination directory.

positional arguments:
  start            directory from where to start
  dest             destination directory

optional arguments:
  -h, --help       show this help message and exit
  -p, --pictures   will copy pictures
  -v, --videos     will copy videos
  -A, --audio      will copy audio files
  -a, --all        copies every file
  -l, --list       list files to copy
  -q, --quiet      no terminal output
  -m, --move       moves all files default is just copy
  -r, --recursive  copies recursive from all subtrees
  -H, --hidden     also shows and copies hidden files

---

## Examples:

$ MassMover -a <Starting_Directory> <Destination_Directory>
Copies every file from all subtrees to the destination.

$ MassMover -a -m <Starting_Directory> <Destination_Directory>
Moves every file from all subtrees to the destination.

$ MassMover -p -m <Starting_Directory> <Destination_Directory>
Moves every picture file from all subtrees to the destination.

$ MassMover -l -a <Starting_Directory> <Destination_Directory>
Lists all availiable files from all subtrees.

---
