# Extract AoE4 info from game files

This only works in Linux system.

## 1. Extract .sga files

Use CoH3.ArchiveViewer.exe to extract them

## 2. Extract chunks from .rgd files

Execute:

```
$ ./extract-chunks.sh
```

## 3. Convert chunks to .json

Execute:

```
$ python reverse_all.py data
```

## 4. Convert .json game files to aoe4tree.tech format

Execute:

```
$ python convert-jsons.py data
```
