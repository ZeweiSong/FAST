#-*- coding: utf-8 -*-
"""
Created on Wed Apr 08 15:44:18 2015
Add Qiime and/or USEARCH style labels to the FASTQ/FASTA files. It uses a mapping file generated by generate_mapping.py to find target files in a specified folder.
All records in each file will be renamed according to the mapping file and specified label type, and also number continuously.
The resulting relabeled files will be stored in a new folder ("labeled" in default), and can be merged into a single file using merge_seqs.py.

Please feel free to contact me for any question.
--
Zewei Song
University of Minnesota
Dept. Plant Pathology
songzewei@outlook.com
"""


def main(name_space):
    import argparse
    import textwrap
    from lib.LabelSeqs import MainLabelFiles
    import time
    import sys

    parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,
                                     epilog=textwrap.dedent('''\
                                        ------------------------
                                        By Zewei Song
                                        University of Minnesota
                                        Dept. Plant Pathology
                                        songzewei@outlook.com
                                        ------------------------'''), prog='fast.py -add_labels')
    parser.add_argument("-m", "--mapping", help="Name of the mapping file, generated by generate_mapping.py")
    parser.add_argument("-i", "--input", help="Name of the input folder")
    parser.add_argument("-o", "--output", default='labeled', help="Name of the output folder")
    parser.add_argument("-t", "--thread", default=1, type=int, help="Number of thread to be used")
    parser.add_argument("-l", "--label", default='qiime', help="Type of label: both, qiime, or usearch")
    parser.add_argument("-fasta", action="store_true", help="Set input file type to FASTA instead of FASTQ")
    args = parser.parse_args(name_space)

    mapping_file = args.mapping
    if mapping_file is None:
        print "Please provide a mapping file."
        sys.exit()
    input_folder = args.input
    if input_folder is None:
        print "Please provide an input folder."
        sys.exit()
    thread = args.thread
    output_folder = args.output
    file_type = 'fastq'
    if args.fasta:  # Set file type to FASTA
        file_type = "fasta"
    label_type = args.label

    start = time.time()
    file_num = MainLabelFiles(mapping_file, input_folder, threads=thread, output_folder=output_folder,
                              file_type=file_type, label_type=label_type)
    end = time.time()
    used_time = round(end - start, 2)
    speed = round((used_time/file_num), 2)
    print '%i files has been labeled in %s seconds (%s sec/file).' % (file_num, str(used_time), str(speed))


if __name__ == '__main__':
    import sys
    main(sys.argv[1:])