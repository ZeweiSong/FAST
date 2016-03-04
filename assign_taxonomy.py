# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 11:44:11 2015

Assign taxonomy information from  a BLAST output to the OTU table.

Now it only accept following output from BLAST:
@ blastn -db blast\unite_02.03.2015 -query raw.qc.fasta_rep_set.fasta -max_target_seqs 1 -outfmt "6 qseqid stitle qlen length pident evalue" -out rep.otu.txt

Please feel free to contact me for any question.
--
Zewei Song
University of Minnesota
Dept. Plant Pathology
songzewei@outlook.com
"""
def main(name_space):
    from lib import ParseOtuTable
    import argparse
    import textwrap
    
    parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,
                                     epilog=textwrap.dedent('''\
                                        ------------------------
                                        By Zewei Song
                                        University of Minnesota
                                        Dept. Plant Pathology
                                        songzewei@outlook.com
                                        ------------------------'''), prog = '-assign_taxonomy')
    parser.add_argument("-otu", help="Input OTU folder")
    parser.add_argument("-tax", help="BLAST taxonomy search result")
    parser.add_argument("-o", "--output", help="Output OTU table")
    parser.add_argument('-scores', action='store_true', help='Indicate to output detail matching score following the taxonomy column.')
    args = parser.parse_args(name_space)
    
    input_otu = args.otu
    input_tax = args.tax
    output_otu = args.output
    
    otu_table = ParseOtuTable.parser_otu_table(input_otu)
    
    # Read in BLAST taxonomy result and store in a dictionary
    taxonomy_temp = []
    with open(input_tax, 'rU') as f:
        if args.scores:
            for line in f:
                taxonomy_temp.append(line.strip('\n').split('\t'))
        else:
            for line in f:
                taxonomy_temp.append(line.strip('\n').split('\t')[:2])
    taxonomy = {}
    for line in taxonomy_temp:
        taxonomy[line[0]] = line[1:]
    
    otu_matrix = otu_table.species_matrix
    hit = 0
    no_hit = 0
    for line in otu_matrix:
        try:
            line += taxonomy[line[0]]
            hit += 1
        except KeyError:
            line.append('no_blast_hit')
            no_hit += 1
    print '{0} OTUs have been assigned a taxa.'.format(hit)
    print '{0} OTUs have no hit.'.format(no_hit)
    
    sample_id = otu_table.sample_id
    if args.scores:
        sample_id = ['OTU_ID'] + sample_id + ['taxonomy','Query_Len','Subject_Len','Pident','Evalue']
    else:
        sample_id = ['OTU_ID'] + sample_id + ['taxonomy']
    
    # Write the new OTU table
    with open(output_otu, 'w') as f:
        f.write('%s\n' % '\t'.join(sample_id))
        for line in otu_matrix:
            line = [str(x) for x in line]
            f.write('%s\n' % '\t'.join(line))
    
    print 'The new OTU table was saved in {0}.'.format(output_otu)
    
if __name__ == '__main__':
    import sys
    main(sys.argv[1:])