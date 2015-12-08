# -*- coding: utf-8 -*-
"""
Created on Tue Dec 08 13:35:44 2015

@author: Zewei Song
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
                                        ------------------------'''))

    parser.add_argument("-i", "--input", help="Name of the input FASTA file.")
    parser.add_argument("-l", "length", help="Length to be truncated.")
    parser.add_argument("-o", "--output", help="Name of the output FASTA file")
    args = parser.parse_args()
    
    sequences = File_IO.read_seqs(args.input)
    count = len(database)
    print "Reading in %s ..." % args.input
    print "%s contains %i records." % (args.input, count)

    with open(args.output, 'w') as f:
        for record in sequences:
            if len(record[1]) >= args.length:
                record[1] = record[1][:length]