#!/usr/bin/env bash

find data -name "*.rgd" | xargs -L 1 ./Relic-SGA-Archive-Tool/src/dump_chunky.py
