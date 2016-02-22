#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 17:00:27 2016



Please feel free to contact me for any question.
--
Zewei Song
University of Minnesota
Dept. Plant Pathology
songzewei@outlook.com
www.songzewei.org
"""

import argparse
parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('-add_labels', action = "store_true")
group.add_argument('-option2')

#args = parser.parse_known_args(['-option1','songzewei','-sub','soon'])
args = parser.parse_known_args()
print args
print args[0].add_labels
print args[0].option2

if args[0].add_labels:
    print "running add_labels.py"
    import add_labels
    add_labels.main(args[1])