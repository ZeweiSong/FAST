#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 15:51:12 2016



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
    from lib import File_IO

    parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,
                                     epilog=textwrap.dedent('''\
                                    ------------------------
                                    By Zewei Song
                                    University of Minnesota
                                    Dept. Plant Pathology
                                    songzewei@outlook.com
                                    ------------------------'''), prog='fast.py -summary_otu_table')
    parser.add_argument('-otu', '--input', help='Name of the input OTU table.')
    parser.add_argument('-o', '--output', default='otu_report.txt', help='Name of the output report.')
    args = parser.parse_args()

if __name__ == '__main__':
    main()
