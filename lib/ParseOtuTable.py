# -*- coding: utf-8 -*-
# !/usr/bin/env python
"""
Create on 4/21/2015.

Please feel free to contact me with any question.
--
Zewei Song
University of Minnesota
Dept. Plant Pathology
songzewei@outlook.com
"""


class parser_otu_table(object):
    def __init__(self, file_path):
        with open(file_path, 'rU') as f:
            temp = f.readlines()
        table = []
        for line in temp:
            table.append(line.strip('\n').split('\t'))
        self.sample_id = table[0][1:]
        self.species_id = [i[0] for i in table[1:]]
        self.species_matrix = table[1:]
        temp = [i[1:] for i in self.species_matrix]
        self.sample_matrix = [list(i) for i in zip(*temp)]
        for i in range(len(self.sample_matrix)):
            self.sample_matrix[i] = [self.sample_id[i]] + self.sample_matrix[i]

    def sample_dict(self):
        sample = {}
        for s in self.sample_id:
            sample[s] = {}
        for line in self.species_matrix:
            for i in range(len(self.sample_id)):
                if int(line[1:][i]) > 0:
                    sample[self.sample_id[i]][line[0]] = int(line[1:][i])
        return sample


    def species_dict(self):
        species = {}
        for s in self.species_id:
            species[s] = {}
        for line in self.sample_matrix:
            for i in range(len(self.species_id)):
                if int(line[1:][i]) > 0:
                    species[self.species_id[i]][line[0]] = int(line[1:][i])
        return species