# AoE4techtree (ExportGameData)

## Summary

Extract AoE4 info from game files and transform to AoE4TreeTech format

## AoE4techtree project

Part of the project: https://aoe4tree.tech/

Main project:
https://github.com/AlexOcampos/aoe4techtree

## Developed by

<p>
  <a href="https://github.com/AlexOcampos">
    <img src="https://avatars.githubusercontent.com/u/683718?s=48" />
    <p>rudyairlines</p>
  </a>
</p>

# How it works?

> **_NOTE:_** Some steps only works in Linux system.

## Step 1. Extract .sga files

Use **CoH3.ArchiveViewer.exe** to extract them

## Step 2. Extract chunks from .rgd files

Execute:

`$ ./extract-chunks.sh`

## Step 3. Convert chunks to .json

Execute:

`$ python reverse_all.py data`

## Step 4. Convert .json game files to aoe4tree.tech format

Execute:

`$ python convert-jsons.py data`

# Disclaimer

    Age of Empires IV © Microsoft Corporation.

    aoe4tree.tech was created under Microsoft's "Game Content Usage Rules" using assets
    from Age of Empires IV, and it is not endorsed by or affiliated with Microsoft.
