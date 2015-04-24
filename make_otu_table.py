# -*- coding: utf-8 -*-
"""
Create on April 20th, 2015.

Create an OTU table from a Qiime style OTU map. The OTUs will be sorted by their total abundance.

Please feel free to contact me with any question.
--
Zewei Song
University of Minnesota
Dept. Plant Pathology
songzewei@outlook.com
"""

import argparse
from lib import ParseOtuMap
import sys

parser = argparse.ArgumentParser()
parser.add_argument('-map', help='The OTU map')
parser.add_argument('-o', '--output', help='Output OTU table.')
args = parser.parse_args()

input_file = args.map
output_file = args.output

# Parse OTU map into OTU table dictionary
otu_map = ParseOtuMap.read_otu_map(input_file)
sample_list = []
otu_table_dict = {}
for key, value in otu_map.items():
    otu_table_dict[key] = {}
    for sample in value:
        treatment = sample[:sample.find('_')]
        if treatment not in sample_list:
            sample_list.append(treatment)
        try:
            otu_table_dict[key][treatment] += 1
        except KeyError:
            otu_table_dict[key][treatment] = 1

# Convert OTU table dictionary to table
otu_abundance = {}
for sample in sample_list:
    otu_abundance[sample] = 0  # Set initial abundance to zero as place holder
sample_list.sort()
otu_table = []
for key, value in otu_table_dict.items():
    current_otu = [key]
    for sample in sample_list:
        try:
            current_otu.append(value[sample])
        except KeyError:
            current_otu.append(0)
    otu_table.append(current_otu)
otu_table.sort(key=lambda x: sum(x), reverse=True)
otu_table = [['OTU_ID'] + sample_list] + otu_table

# Write OTU table to a new file
sample_list = ['OTU_ID'] + sample_list
with open(output_file, 'w') as f:
    for line in otu_table:
        line = [str(i) for i in line]
        f.write('%s\n' % '\t'.join(line))
