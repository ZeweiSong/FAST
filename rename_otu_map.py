#!usr/bin/env python
# -*- coding: utf-8 -*-
"""
Create on 4/27/2015.

Rename the OTU in a Qiime style OTU map using a provided label.

Please feel free to contact me for any question.
--
Zewei Song
University of Minnesota
Dept. Plant Pathology
songzewei@outlook.com
"""

import argparse
from lib import ParseOtuMap

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input', help='Input OTU map')
parser.add_argument('-o', '--output', help='Output OTU map')
parser.add_argument('-label', default='OTU_', help='New OTU name label')
args = parser.parse_args()

input_otu = args.input
output_otu = args.output
otu_label = args.label

print 'Reading in %s ...' % input_otu
old_map = ParseOtuMap.read_otu_map(input_otu)
otu_temp = old_map.items()
print 'Sorting OTUs by size ...'
otu_temp.sort(key=lambda x: len(x[1]), reverse=True)

with open(output_otu, 'w') as f:
    count = 1
    for otu in otu_temp:
        new_name = otu_label + str(count)
        count += 1
        line = new_name + '\t' + '\t'.join(otu[1])
        f.write('%s\n' % line)
print 'New OTU map saved in %s.' % output_otu