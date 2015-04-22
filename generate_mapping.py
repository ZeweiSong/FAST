# -*- coding: utf-8 -*-
"""
Created on Wed Apr 01 15:25:06 2015

Try to guess the sample name and read type from the raw Illumina FASTQ files.
The format is according to that used by University of Minnesota Genomic CEnter (UMGC).
The output is a mapping file which can be fed to LabelSeq.py (Right now need to move it
to the same folder with raw sequences to make it work).

This is NOT a qiime mapping file for add_qiime_labels.py, but should be easy to convert to that file.

Please feel free to contact me for any question.
--
Zewei Song
University of Minnesota
Dept. Plant Pathology
songzewei@outlook.com
"""
#%%
def file_list(folder):
#Get the file list in a folder
    from os import walk
    f = []
    for (dirpath,dirnames,filenames) in walk(folder):
        f.extend(filenames)
        break
    return f
#%%
def ParseFileName(filename):
    sample_name = filename[0:filename.find("_")]
    if filename.find("R1") != -1:
        read_type = "R1"
    elif filename.find("R2") != -1:
        read_type = "R2"
    else:
        read_type = "unknown"
    return (filename,sample_name,read_type)
#%%
def WriteMapping(folder,mapping_file='mapping.txt'):
    f = File_IO.file_list(folder)
    mapping = [("Filename","Sample_name","Read_type")]
    unknown_read = 0
    for item in f:
        mapping.append(ParseFileName(item))
        if mapping[-1][2] == 'unknown':
            unknown_read += 1
    with open(mapping_file, 'w') as m:
        count = 0
        for line in mapping:
            m.write("%s\n"%('\t').join(line))
            count += 1
    return count,unknown_read

if __name__ == '__main__':
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
    parser.add_argument('-i','--input',help='Name of the folder with the raw data')
    parser.add_argument('-o','--output',default='mapping.txt',help='Name of the new mapping file')
    args = parser.parse_args()
    
    folder_name = args.input
    count,unknown_read = WriteMapping(folder_name,mapping_file=args.output)
    
    print 'Generated a mapping with %d files in %s.' %(count-1,args.output)
    if unknown_read > 0:
        print 'Can not detect read type in %s files, please check the mapping file.'%unknown_read