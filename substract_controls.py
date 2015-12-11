# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 13:32:33 2015

This script will remove the abundance value in extract control from all samples.
Samples can have different extract control, by providing the names in a file:
Example:

OTU_ID Control_name
Sample_1 Extract_run1
Sample_2 Extract_run1
Sample_3 Extract_run1
Sample_4 Extract_run2
Sample_5 Extract_run2
Sample_6 Extract_run2

Save the name list in a tab-delimited text file.

Please feel free to contact me for any question.
--
Zewei Song
University of Minnesota
Dept. Plant Pathology
songzewei@outlook.com
www.songzewei.org
"""

#%% Read in Extract control list
control_list = 'extract_control_list.txt'

name_dict = {} # corresponding extract control for all samples
with open(control_list, 'rU') as f:
    temp_list = []
    for line in f:
        line = line.strip('\n').split('\t')
        temp_list.append(line)

for item in temp_list[1:]:
    name_dict[item[0]] = item[1]

#%% Read in the OTU table
from lib import ParseOtuTable

otu_table = ParseOtuTable.parser_otu_table("example.txt")
sample_dict = otu_table.sample_dict()

#%% Substract extract control abundances
sample_dict_new = {}

for sample in name_dict.keys():
    sample_dict_new[sample] = {}
    for otu in sample_dict[sample].keys():        
        try:
            sample_dict[name_dict[sample]][otu]
            control_abundance = sample_dict[name_dict[sample]][otu]
            sample_abundance = sample_dict[sample][otu]
            if sample_abundance >= control_abundance:
                new_abundance = sample_abundance - control_abundance
            else:
                new_abundance = 0
        except KeyError:
            new_abundance = sample_dict[sample][otu]
        sample_dict_new[sample][otu] = new_abundance
#%% Output the otu table
content = ParseOtuTable.write_sample_dict(sample_dict_new, otu_table.meta_dict(), otu_table.species_id, 'test.txt')
#%%
new_table = ParseOtuTable.parser_otu_table('test.txt')
ParseOtuTable.sorted_table(new_table, new_file_path='table_control.txt', remove_zero=True)
#%% Sort the otu table
new = ParseOtuTable.sorted_table(otu_table)