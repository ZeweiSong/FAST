# -*- coding: utf-8 -*-
#!/usr/bin/env python
"""
Create on .

Please feel free to contact me with any question.
--
Zewei Song
University of Minnesota
Dept. Plant Pathology
songzewei@outlook.com
"""

import argparse
import textwrap
from lib import ParseOtuMap
import sys

parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,
                                 epilog=textwrap.dedent('''\
                                    ------------------------
                                    By Zewei Song
                                    University of Minnesota
                                    Dept. Plant Pathology
                                    songzewei@outlook.com
                                    ------------------------'''))
parser.add_argument("-i", "--input", required=True, help="Input OTU map")
parser.add_argument("-subset", help="Name of another OTU map to compare with")
args = parser.parse_args()

input_map = args.input
input_map_compare = args.subset

print 'Reading in %s ...' % input_map
otu_map = ParseOtuMap.read_otu_map(input_map)
otu_map_parser = ParseOtuMap.otu_map_parser(input_map)
otu_num = otu_map_parser.derep_count
seq_num = otu_map_parser.seqs_count
otu_max = otu_map_parser.max_derep
otu_min = otu_map_parser.min_derep
otu_ave = otu_map_parser.ave_derep

print 'OTU = %i; Sequence = %i' % (otu_num, seq_num)
print 'Max abundance = %i; Min abundance = %i; Ave abundance = %i' % (otu_max, otu_min, otu_ave)
print
print 'Reading in %s for comparison ...' % input_map_compare
otu_map_compare = ParseOtuMap.read_otu_map(input_map_compare)