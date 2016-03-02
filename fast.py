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
parser = argparse.ArgumentParser(prog='fast.py -function', add_help=False)
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('-document', action='store_true', help='Print out the helping document for the main program.')
group.add_argument('-generate_mapping', action = "store_true")
group.add_argument('-add_labels', action = "store_true")
group.add_argument('-merge_seqs', action = "store_true")
group.add_argument('-dereplicate', action = "store_true")


#args = parser.parse_known_args(['-option1','songzewei','-sub','soon'])
args = parser.parse_known_args()
#print args

if args[0].document:
    print "This is the helping document:"

if args[0].generate_mapping:
    import generate_mapping
    generate_mapping.main(args[1])
    
if args[0].add_labels:
#    print "running add_labels.py"
    import add_labels
    add_labels.main(args[1])

if args[0].merge_seqs:
    import merge_seqs
    merge_seqs.main(args[1])

if args[0].dereplicate:
    import dereplicate
    dereplicate.main(args[1])