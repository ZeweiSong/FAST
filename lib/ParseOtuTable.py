# -*- coding: utf-8 -*-
#!/usr/bin/env python
"""
Create on 4/21/2015.

This library will parse a tab-delimited OTU table into dictionaries.

Please feel free to contact me with any question.
--
Zewei Song
University of Minnesota
Dept. Plant Pathology
songzewei@outlook.com
"""


class parser_otu_table(object):
    def __init__(self, file_path, meta_col='taxonomy'):
        with open(file_path, 'rU') as f:
            temp = f.readlines()
        table = []
        for line in temp:
            table.append(line.strip('\n').split('\t'))
        size = len(table[0])
        for line in table:
            if len(line) < size:
                line += [''] * (size - len(line))

        # Get id for sample, species, amd meta data
        try:
            meta_position = table[0].index(meta_col)  # Begining position of meta data
        except ValueError:
            meta_position = len(table[0]) + 1
        self.sample_id = table[0][1:meta_position]  # Second column till the first meta column
        self.meta_id = table[0][meta_position:]  # Start from the first meta column to the end
        self.species_id = [i[0] for i in table[1:]]  # First column stating from the second row
        
        # Convert all abundance to intger
        for line in table[1:]:
            try:
                line[1:meta_position] = map(int, line[1:meta_position])
            except ValueError:
                print "There are non-number value in your OTU table."
                import sys                
                sys.exit()
                
        # Get sample, species, and meta data matrix with head names
        self.species_matrix = [i[:meta_position] for i in table[1:]]
        temp = [i[1:meta_position] for i in table]
        self.sample_matrix = [list(i) for i in zip(*temp)]
        temp = [i[meta_position:] for i in table]
        self.meta_matrix = [list(i) for i in zip(*temp)]


    # Generate a dictionary using sample name, OTU name
    def sample_dict(self):
        sample = {}
        for s in self.sample_id:
            sample[s] = {}
        for line in self.sample_matrix:
            abundance = line[1:]
            for i in range(len(self.species_id)):
                if int(abundance[i]) > 0:
                    sample[line[0]][self.species_id[i]] = int(abundance[i])
        return sample

    # Generate a dictionary using OTU name, sample name
    def species_dict(self):
        species = {}
        for s in self.species_id:
            species[s] = {}
        for line in self.species_matrix:
            for i in range(len(self.sample_id)):
                if int(line[1:][i]) > 0:
                    species[line[0]][self.sample_id[i]] = int(line[1:][i])
        return species


    # Generate a dictionary using mata name, OTU name
    def meta_dict(self):
        meta = {}
        for m in self.meta_id:
            meta[m] = {}
        for line in self.meta_matrix:
            for i in range(len(self.species_id)):
                meta[line[0]][self.species_id[i]] = line[1:][i]
        return meta