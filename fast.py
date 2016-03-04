#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 17:00:27 2016

This is the main script for the FAST (Fungal Amplicon Sequencing Toolbox) package.

Please feel free to contact me for any question.
--
Zewei Song
University of Minnesota
Dept. Plant Pathology
songzewei@outlook.com
www.songzewei.org
"""
def main():
    import argparse
    import textwrap
    import sys
    import importlib
    
    parser = argparse.ArgumentParser(prog='fast.py -function', add_help=False)
    
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-add_labels', action = "store_true")
    group.add_argument('-add_seqs_size', action = "store_true")
    group.add_argument('-assign_taxonomy', action = 'store_true')
    group.add_argument('-combine_fast_map', action = "store_true")
    group.add_argument('-convert_fastq', action = 'store_true')
    group.add_argument('-correct_fasta', action = 'store_true')
    group.add_argument('-count_seqs', action = 'store_true')
    group.add_argument('-dereplicate', action = "store_true")
    group.add_argument('-document', action='store_true')
    group.add_argument('-filter_database', action = 'store_true')
    group.add_argument('-filter_otu_map', action = "store_true")
    group.add_argument('-filter_seqs', action = "store_true")
    group.add_argument('-generate_fast_map', action = "store_true")
    group.add_argument('-generate_mapping', action = "store_true")
    group.add_argument('-make_otu_table', action = 'store_true')
    group.add_argument('-merge_otu_maps', action = 'store_true')
    group.add_argument('-merge_seqs', action = "store_true")
    group.add_argument('-otu_deconstruct', action = 'store_true')
    group.add_argument('-otu_map_info', action = 'store_true')
    group.add_argument('-parse_uc_cluster', action = "store_true")
    group.add_argument('-parse_uparse_cluster', action = "store_true")
    group.add_argument('-pick_seqs', action = 'store_true')
    group.add_argument('-random_dataset', action = 'store_true')
    group.add_argument('-rarefy_otu_table', action = 'store_true')
    group.add_argument('-rename_otu_map', action = "store_true")
    group.add_argument('-split_taxa', action = 'store_true')
    group.add_argument('-stat_seqs', action = 'store_true')
    group.add_argument('-substract_controls', action = 'store_true')
    group.add_argument('-truncate_seqs', action = 'store_true')
    
    args = parser.parse_args([sys.argv[1]])
    for option in args.__dict__:
        if args.__dict__[option]:
            function_name = option
    
    sub_args = sys.argv[2:]
    
    if args.document:
        print "This is the helping document:"
    
    else:
        function = importlib.import_module(function_name)
        function.main(sub_args)

#    elif args.generate_mapping:
#        import generate_mapping
#        generate_mapping.main(sub_args)
        
#    else:
#        function = __import__(function_name)
#        function.main(sub_args)
    
    '''    
    if args.generate_mapping:
        import generate_mapping
        generate_mapping.main(sub_args)
    '''

if __name__ == '__main__':
    main()