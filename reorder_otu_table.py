#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 08 16:38:10 2016



Please feel free to contact me for any question.
--
Zewei Song
University of Minnesota
Dept. Plant Pathology
songzewei@outlook.com
www.songzewei.org
"""

from __future__ import print_function
def main(name_space):
    
    import argparse
    import textwrap
    from lib import ParseOtuTable
    import sys
    
    parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,
                                     epilog=textwrap.dedent('''\
                                    ------------------------
                                    By Zewei Song
                                    University of Minnesota
                                    Dept. Plant Pathology
                                    songzewei@outlook.com
                                    ------------------------'''), prog='fast.py -parse_uc_cluster')
    parser.add_argument('-i', '--input', help='Input uparse denovo cluster output file')
    parser.add_argument('-o', '--output', help='Output Qiime style OTU map')
    parser.add_argument('-separator', default=';', help='Separator between sample name and size annotation')
#    parser.add_argument('-fast', default='', help='Name of FAST style output.')
#    parser.add_argument('-centroid', default = '', help='Name of the FASTA file contains sequences of centroids.')
    
    args = parser.parse_args(name_space)

if __name__ == '__main__':
    import sys
    main(sys.argv[1:])
