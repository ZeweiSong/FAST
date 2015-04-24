# ！usr/bin/env python
# -*- coding: utf-8 -*-
"""
Create on 4/24/2015.

Please feel free to contact me for any question.
--
Zewei Song
University of Minnesota
Dept. Plant Pathology
songzewei@outlook.com
"""

from lib import ParseOtuTable
import argparse
import textwrap

parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,
                                 epilog=textwrap.dedent('''\
                                    ------------------------
                                    By Zewei Song
                                    University of Minnesota
                                    Dept. Plant Pathology
                                    songzewei@outlook.com
                                    ------------------------'''))
parser.add_argument("-otu", help="Input OTU folder")
parser.add_argument("-mock_list", help="A list of species name in the mock community, Genus and species should be connected with _")
parser.add_argument("-mock_sample", default='mock', help="Name of the mock community sample")
parser.add_argument("-o", "--output", help="Output OTU table")
args = parser.parse_args()

input_otu = args.otu
input_mock = args.mock
mock_column = args.mock_sample
output_report = args.output

otu_table = ParseOtuTable.parser_otu_table(input_otu)
otu_sample = otu_table.sample_dict()
mock_sample = otu_sample[mock_column]
otu_meta = otu_table.meta_dict()

mock_list = []
mock_hit = {}
with open(input_mock, 'rU') as f:
    for line in f:
        mock_list.append(line.strip('\n'))
        mock_hit[line.strip('\n')] = {}
mock_hit['other'] = {}


for otu_name in mock_sample:
    coverage = otu_meta['Subject_Len'][otu_name]/float(otu_meta['Query_Len'][otu_name])
    if coverage >= 0.9 and otu_meta['Pident'] >= 97:
        match_checker = False
        for mock_species in mock_list:
            if otu_meta['taxonomy'].find(mock_species) != -1:  # Found mock species in current OTU
                mock_hit[mock_species][otu_name] = [mock_sample[otu_name], otu_meta['taxonomy'][otu_name]]
                match_checker = True
                break
        if not match_checker:
            match_checker = False
            mock_hit['other'][otu_name] = [mock_sample[otu_name], otu_meta['taxonomy'][otu_name]]

