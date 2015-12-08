# -*- coding: utf-8 -*-
"""
Created on Tue Dec 08 13:35:44 2015

This script will truncate the given FASTA file to a fixed length.
Any sequences shorter than the provided length will be discard.
Any sequences longer than the provided length will be cut to the length.

Please feel free to contact me for any question.
--
Zewei Song
University of Minnesota
Dept. Plant Pathology
songzewei@outlook.com
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
    parser.add_argument("-l", "--length", help="Length to be truncated.")
    parser.add_argument("-o", "--output", help="Name of the output FASTA file")
    args = parser.parse_args()
    truncate_length = int(args.length)
    
    sequences = File_IO.read_seqs(args.input)
    count = len(sequences)
    print "Reading in %s ..." % args.input
    print "%s contains %i records." % (args.input, count)
    print "Truncating sequences to %i ..." % truncate_length

    count_fail = 0
    with open(args.output, 'w') as f:
        for record in sequences:
            if len(record[1]) >= truncate_length:
                record[1] = record[1][:truncate_length]
                f.write('>%s\n' % record[0])
                f.write('%s\n' % record[1])
            else:
                count_fail += 1
    
    print "%i sequences were truncated to %i and save in %s." % (count - count_fail, truncate_length, args.output)

if __name__ == '__main__':
    main()