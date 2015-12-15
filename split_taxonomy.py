# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 14:54:48 2015

This scrtipt with output two files with the abundance and richess of the given taxonomic level.

Please feel free to contact me with any question.
--
Zewei Song
University of Minnesota
Dept. Plant Pathology
songzewei@outlook.com
"""

def main():
    import argparse
    import textwrap
    from lib import ParseTaxonomy
#    import time
#    import sys

    parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,
                                     epilog=textwrap.dedent('''\
                                        ------------------------
                                        By Zewei Song
                                        University of Minnesota
                                        Dept. Plant Pathology
                                        songzewei@outlook.com
                                        ------------------------'''))
    parser.add_argument("-otu", help="Name of the OTU table, tab delimited.")
    parser.add_argument("-tax", help="Taxonomic level from k, p, c, o, f, g, s")
    args = parser.parse_args()
    tax_dict = {'k':'Kingdom', 'p':'Phylum', 'c':'Class', 'o':'Order', 'f':'Family', 'g':'Genus', 's':'Species'}
    
    split_tax_table = ParseTaxonomy.taxonomy_info(args.otu, args.tax)
    tax_number = len(split_tax_table['abundance'])
    split_tax_table_output = ParseTaxonomy.taxonomy_output(split_tax_table)
    
    output_abundance = 'abundance_' + args.tax + '_' + args.otu
    output_richness = 'richness_' + args.tax + '_' + args.otu

    # Write the abundance data    
    temp_abundance = []
    for line in split_tax_table_output['abundance'][1:]:
        temp_sum = sum([int(i) for i in line[1:]])
        line = [temp_sum] + line
        temp_abundance.append(line)
    temp_abundance = sorted(temp_abundance, reverse = True)
    with open(output_abundance, 'w') as f:
        header = split_tax_table_output['abundance'][0]
        header = '\t'.join(header)
        f.write('%s\n' % header)
        for line in temp_abundance:
            line = line[1:]
            line = [str(i) for i in line]
            line = '\t'.join(line)
            f.write('%s\n' % line)
    
    # Write the richness data
    temp_richness = []
    for line in split_tax_table_output['richness'][1:]:
        temp_sum = sum([int(i) for i in line[1:]])
        line = [temp_sum] + line
        temp_richness.append(line)
    temp_richness = sorted(temp_richness, reverse = True)                        
    with open(output_richness, 'w') as f:
        header = split_tax_table_output['richness'][0]
        header = '\t'.join(header)
        f.write('%s\n' % header)
        for line in temp_richness:
            line = line[1:]
            line = [str(i) for i in line]
            line = '\t'.join(line)
            f.write('%s\n' % line)
    
    print 'Split %s at the level of %s.' % (args.otu, tax_dict[args.tax])
    print 'Find %i %s.' % (tax_number, tax_dict[args.tax])
    print 'Splitted OTU table by abundance saved in %s.' % output_abundance
    print 'Splitted OTU table by richness saved in %s.' % output_richness
            
if __name__ == '__main__':
    main()