# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 19:23:08 2015

Please feel free to contact me with any question.
--
Zewei Song
University of Minnesota
Dept. Plant Pathology
songzewei@outlook.com
"""

from lib import random_subsample as rs
from lib import ParseOtuTable
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-otu', help='Input OTU table')
parser.add_argument('-o', '--output', help='Output OTU table')
parser.add_argument('-d', '--depth', help='Sampling depth for each sample')
parser.add_argument('-iter', default=1, help='Iteration time for each sample')
parser.add_argument('-thread', default=1, help='Number of threads')
parser.add_argument('-keep_all', action='store_true', help='Indicate to keep all samples')
parser.add_argument('-meta_column', default='taxonomy', help='Name of the first meta data')
args = parser.parse_args()

input_otu = args.otu
depth = int(args.depth)
iter_num = int(args.iter)
thread = int(args.thread)
meta_col = args.meta_column
output_otu = args.output

otu_table = ParseOtuTable.parser_otu_table(input_otu, meta_col=meta_col)
input_sample = otu_table.sample_matrix
if args.keep_all:  # Remove sample with total abundance less than sampling depth
    temp = []
    count_discard = 0
    for line in input_sample:
        if sum(line[1:]) >= depth:
            temp.append(line)
        else: count_discard += 1
    input_sample = temp
    
otu_id = otu_table.species_id

otu_table_rarefied = [['OTU_ID'] + otu_id]

if __name__ == '__main__':
    for sample in input_sample:
        repeat_sample = rs.repeat_rarefaction_parallel(sample[1:],depth,iter_num,processor=thread)
        repeat_sample.sort(key=lambda x: sum(i>0 for i in x))
        repeat_sample = [sample[0]] + repeat_sample[iter_num/2]  # Pick the rarefied sample with the average richness
        otu_table_rarefied.append(repeat_sample[:])

    otu_table_rarefied = [list(i) for i in zip(*otu_table_rarefied)]

    with open(output_otu, 'w') as f:
        for line in otu_table_rarefied:
            line = [str(i) for i in line]
            f.write('%s\n' % '\t'.join(line))