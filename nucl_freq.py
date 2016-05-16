#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 20:36:50 2016

Calculte the frequency of nucleotide from the starting of sequences.

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
    
    input_file = args.input
    output_file = args.output
    
    input_seq = File_IO.read_seqs(input_file)
    
    # Get the maximum sequence length
    seq_len = []
    for record in input_seq:
        seq_len.append(len(record[1]))
    max_seq_len = max(seq_len)
    
    # Create dictionary for nucleotide counting    
    nucl_dict = {}
    nucl_list = ['A','T','C','G','N']
    for i in range(max_seq_len):
        nucl_dict[i] = {}
        for nucl in nucl_list:
            nucl_dict[i][nucl] = 0

    # Count the frequency of nucleotide    
    for record in input_seq:
        for index, nucl in enumerate(record[1]):
            try:
                nucl_dict[index][nucl] += 1
            except KeyError:
                print "Unidentified nucleotide %s in %s" % (nucl, record[0])
    
    # Output the counting result
    header = 'Position\tA\tT\tC\tG\tN'
    output_content = [header]
    for pos in range(max_seq_len):
        current_line = []
        current_line = [str(pos)]
        for nucl in nucl_list:
            current_line.append(str(nucl_dict[pos][nucl]))
        current_line = '\t'.join(current_line)
        output_content.append(current_line)
    
    with open(output_file, 'wb') as f:
        for line in output_content:
            f.write("%s\n" %line)
    

if __name__ == '__main__':
    import sys
    main(sys.argv[1:])