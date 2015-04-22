# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 16:41:33 2015

Pick sequences from a given FASTA file using a OTU map or a name list.

For OTU map, the default method is to pick using name of each OTU.

Using -sequence to specify picking using sequence names within each OTU.

Please feel free to contact me for any question.
--
Zewei Song
University of Minnesota
Dept. Plant Pathology
songzewei@outlook.com
"""

import argparse
from lib import ParseOtuMap
from lib import Seq_IO
from lib import File_IO

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input', help='Input FASTA file to be picked')
parser.add_argument('-o', '--output', help='Name for output FASTA file.')
group = parser.add_mutually_exclusive_group()
group.add_argument('-map', help='OTU map file, will pick OTU names in default')
group.add_argument('-name_list', help='File with names in separated lines')
parser.add_argument('-sequence', action='store_true', help='Indicate to pick by sequence names instead of OTU names')
args = parser.parse_args()

input_fasta = args.input
output_fasta = args.output
pick_list = []
if args.map:
    if not args.sequence:
        otu_map = ParseOtuMap.read_otu_map(args.map)
        for key in otu_map:
            pick_list.append(key)
    elif args.sequence:
        otu_map = ParseOtuMap.read_otu_map(args.map)
        for key, value in otu_map.items():
            pick_list += value
if args.name_list:
    with open(args.name_list, 'rU') as f:
        for line in f:
            pick_list.append(line.strip('\n'))
print 'Found %i names to be picked.' % len(pick_list)

print 'Reaing in the original FASTA file: %s ...' % input_fasta
input_content = File_IO.read_seqs(input_fasta)
print 'Indexing the original sequence file ...'
input_dict = Seq_IO.make_dict(input_content)

count_picked = 0
count_missed = 0
print 'Search name list in the sequence file ...'
picked_content = []
for name in pick_list:
    try:
        picked_content.append([name, input_dict[name][0]])
        count_picked += 1
    except KeyError:
        count_missed += 1

print 'Finished searching.'
print 'Original sequence=%i' % len(input_content)
print 'Input names=%i' % len(pick_list)
print 'Picked sequences=%i' % count_picked
print 'Not found sequences=%i' % count_missed

print 'Writing to a new FASTA file ...'
count = File_IO.write_seqs(picked_content, output_fasta, checker=False, overwrite=True)
print 'Picked sequences wrote to %s.' % output_fasta