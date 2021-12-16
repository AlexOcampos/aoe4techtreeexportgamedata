#!/usr/bin/env bash

find data -type d -links 2 | xargs -L 1 ./reverse.py > test.txt
