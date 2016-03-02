#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 17:00:27 2016

This is the main script for the FAST (Fungal Amplicon Sequencing Toolbox) package.

Please feel free to contact me for any question.
--
Zewei Song
University of Minnesota
Dept. Plant Pathology
songzewei@outlook.com
www.songzewei.org
"""

import argparse
import sys
#print sys.argv
parser = argparse.ArgumentParser(prog='fast.py -function', add_help=False)
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('-document', action='store_true', help='Print out the helping document for the main program.')
group.add_argument('-generate_mapping', action = "store_true")
group.add_argument('-add_labels', action = "store_true")
group.add_argument('-merge_seqs', action = "store_true")
group.add_argument('-filter_seqs', action = "store_true")
group.add_argument('-dereplicate', action = "store_true")
group.add_argument('-filter_otu_map', action = "store_true")
group.add_argument('-add_seqs_size', action = "store_true")
group.add_argument('-parse_uc_cluster', action = "store_true")

#args = parser.parse_known_args(['-option1','songzewei','-sub','soon'])
args = parser.parse_args([sys.argv[1]])
sub_args = sys.argv[2:]

if args.document:
    print "This is the helping document:"

if args.generate_mapping:
    import generate_mapping
    generate_mapping.main(sub_args)
    
if args.add_labels:
    import add_labels
    add_labels.main(sub_args)

if args.merge_seqs:
    import merge_seqs
    merge_seqs.main(sub_args)

if args.filter_seqs:
    import filter_seqs
    filter_seqs.main(sub_args)

if args.dereplicate:
    import dereplicate
    dereplicate.main(sub_args)

if args.filter_otu_map:
    import filter_otu_map
    filter_otu_map.main(sub_args)

if args.add_seqs_size:
    import add_seqs_size
    add_seqs_size.main(sub_args)

if args.parse_uc_cluster:
    import parse_uc_cluster
    parse_uc_cluster.main(sub_args)