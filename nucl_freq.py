#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 20:36:50 2016

Please feel free to contact me with any question.
--
Zewei Song
University of Minnesota
Dept. Plant Pathology
songzewei@outlook.com
"""

def main(Namespace):
    import argparse
    import textwrap
    from lib import File_IO

    parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,
                                     epilog=textwrap.dedent('''\
                                    ------------------------
                                    By Zewei Song
                                    University of Minnesota
                                    Dept. Plant Pathology
                                    songzewei@outlook.com
                                    ------------------------'''), prog='fast.py -nucl_freq')
    parser.add_argument('-i', '--input', help='Name of the input FASTA or FASTQ file.')
    parser.add_argument('-o', '--output', default='nucl_report.txt', help='Name of the reporting file.')
    args = parser.parse_args(Namespace)

if __name__ == '__main__':
    import sys
    main(sys.argv[1:])