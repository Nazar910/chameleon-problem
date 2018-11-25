#!/bin/bash
TESTS=$(ls -A *.test.py)
for t in $TESTS;
    do python3 $t;
done
