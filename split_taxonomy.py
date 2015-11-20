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
    
    split_tax_table = ParseTaxonomy.taxonomy_info(args.otu, args.tax)
    split_tax_table_output = ParseTaxonomy.taxonomy_output(split_tax_table)
    
    output_abundance = 'abundance_' + args.tax + '_' + args.otu
    output_richness = 'richness_' + args.tax + '_' + args.otu
    
    with open(output_abundance, 'w') as f:
        for line in split_tax_table_output['abundance']:
            line = '/t'.join(line)
            f.write('%s/n' % line)
    with open(output_richness, 'w') as f:
        for line in split_tax_table['richness']:
            line = '/t'.join(line)
            f.write('%s/n' % line)
            
if __name__ == '__main__':
    main()