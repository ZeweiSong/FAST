# Example pipeline for ITS1 data set
#
# The following command between : ' and ' are for setting up the working environment. I just put them here as an example, and I recommend that you visit my Wiki's set up page (https://github.com/ZeweiSong/FAST/wiki/Setup-the-working-folder) for more details. Usually I would visit the webpage of ecah individual prpgram and download their latest version. If you want to try these command, just copy and paste each line to run them.
#
# Please take a look at my GitHub wiki page for the detail of this pipeline (https://github.com/ZeweiSong/FAST/wiki/Fungal-ITS1-Pipeline-Using-Both-Reads).
# This is a Linux shell script. So technically you can run it under Linux environment, and it will automatically go over every command. But I highly recommend to go over these commands by line at the first time to get familiar with them.

: '
#Set up FAST package
mkdir bin
wget https://github.com/ZeweiSong/FAST/archive/FAST_v1.101.tar.gz
tar -xvf FAST_v1.101.tar.gz
mv FAST-FAST_v1.101. bin/FAST
bin/FAST/fast.py -add_labels -h
'

: '
# Install cutadapt
pip install --user --upgrade cutadapt
cp ~/.local/bin/cutadapt bin/
bin/cutadapt --help
'

: '
#Download VSEARCH (I am using v2.1.0 here, their latest version require an update of Linux system if you know how. There is no difference.)
wget https://github.com/torognes/vsearch/releases/download/v2.1.0/vsearch-2.1.0-linux-x86_64.tar.gz
tar -xvf vsearch-2.1.0-linux-x86_64.tar.gz
mv vsearch-2.1.0-linux-x86_64/bin/vsearch bin/
rm -r vsearch-2.1.0-linux-x86_64/
'

: '
#Download PEAR
wget http://sco.h-its.org/exelixis/web/software/pear/files/pear-0.9.10-bin-64.tar.gz
tar -xvf pear-0.9.10-bin-64.tar.gz
mv pear-0.9.10-bin-64/pear-0.9.10-bin-64 bin/pear
rm -r pear-0.9.10-bin-64
'

: '
#Download UNITE database
mkdir database
wget https://unite.ut.ee/sh_files/sh_general_release_22.08.2016.zip
sudo apt-get install zip
unzip sh_general_release_22.08.2016.zip
mv sh_general_release_dynamic_22.08.2016.fasta database/
rm -r developer
'

: '
#Download the example dataset. This file contains example for ITS1 and ITS2 data.
wget https://github.com/ZeweiSong/FAST_example/archive/v1.2.tar.gz
tar -xvf v1.2.tar.gz
mv FAST_example-1.2/ITS2/* ./
'

: '
# Clean up the workspace
rm *.gz
rm *.zip
'

# Generate sample mapping files:
bin/FAST/fast.py -generate_mapping -i read1 -o read1_map.txt
bin/FAST/fast.py -generate_mapping -i read2 -o read2_map.txt

# Label sequences:
bin/FAST/fast.py -add_labels -m read1_map.txt -i read1 -o read1_labeled -t 4
bin/FAST/fast.py -add_labels -m read2_map.txt -i read2 -o read2_labeled -t 4

# Merge all files:
bin/FAST/fast.py -merge_seqs -i read1_labeled -o read1.fastq
bin/FAST/fast.py -merge_seqs -i read2_labeled -o read2.fastq

# Trim off sequencing primers:
bin/cutadapt -a CTGTCTCTTATACACATCTCCGAGCCCACGAGAC -A CTGTCTCTTATACACATCTGACGCTGCCGACGA -o read1.cut.fastq -p read2.cut.fastq read1.fastq read2.fastq -m 50

# Merge Read1 and Read2 sequnces:
bin/pear -f read1.cut.fastq -r read2.cut.fastq -o merge.pear.its2 -k -j 4

# Remove 5.8SR primer and LSU regions:
bin/FAST/fast.py -nucl_freq -i merge.pear.its2.assembled.fastq -o merge.pear.head.txt
bin/FAST/fast.py -nucl_freq -i merge.pear.its2.assembled.fastq -o merge.pear.tail.txt -tail

cutadapt -g ^TCGATGAAGAACGCAGCG -o merge.pear.its2.cut_f.fastq merge.pear.its2.assembled.fastq --discard-untrimmed
bin/FAST/fast.py -truncate_seqs -i merge.pear.its2.cut_f.fastq -slice 0,60 -o merge.pear.its2.cut_fr.fastq

# Discard low quality sequences:
bin/vsearch --fastq_filter merge.pear.its1.cut_fr.fastq --fastq_maxee 1 --fastaout merge.pear.its2.maxee1.fasta --fasta_width 0

# Dereplicate sequences:
bin/FAST/fast.py -dereplicate -i merge.pear.its2.maxee1.fasta -o raw.qc.derep -t 4

# Discard singletons:
bin/FAST/fast.py -filter_otu_map -i raw.qc.derep.txt -o raw.qc.derep.size2.txt -min_size 2
bin/FAST/fast.py -pick_seqs -i raw.qc.derep.fasta -map raw.qc.derep.size2.txt -o raw.qc.derep.size2.fasta -sizeout

# Chimera checking using UNITE as reference
bin/vsearch --uchime_ref raw.qc.derep.size2.fasta --nonchimeras raw.qc.derep.size2.uchime.fasta --db database/sh_general_release_dynamic_22.08.2016.fasta --sizeout --fasta_width 0 --thread 4

# Cluster OTU at 97% similarity using the greedy algorithm:
bin/vsearch --cluster_size raw.qc.derep.size2.uchime.fasta --centroids raw.qc.vsearch.fasta --fasta_width 0 -id 0.97 --sizein --uc raw.qc.uc.txt --threads 4

# Parse the UC output into OTU map:
bin/FAST/fast.py -parse_uc_cluster -i raw.qc.uc.txt -o raw.qc.vsearch.txt

# Combine the Dereplicate map and sequences:
bin/FAST/fast.py -generate_fast_map -map raw.qc.derep.size2.txt -seq raw.qc.derep.size2.uchime.fasta -o fast.derep.txt -derep

# Combine the OTU map and sequences:
bin/FAST/fast.py -generate_fast_map -map raw.qc.vsearch.txt -seq raw.qc.vsearch.fasta -o fast.otu.txt -otu

# Combine to FAST derep map and OTU map into a single hybrid:
bin/FAST/fast.py -combine_fast_map -derep_map fast.derep.txt -otu_map fast.otu.txt -o fast.hybrid.txt

# Rename the OTUs, so them will start with OTU_:
bin/FAST/fast.py -rename_otu_map -fast_map fast.hybrid.txt -o fast.hybrid.otu.txt

# Generate the OTU table from the FAST hybrid map, along with the representative sequences:
bin/FAST/fast.py -make_otu_table -fast_map fast.hybrid.otu.txt -o otu_table.txt -rep rep_seq.fasta

# Search UNITE database for record with similarity >= 60%
bin/vsearch --usearch_global rep_seq.fasta -db database/sh_general_release_dynamic_22.08.2016.fasta --userout taxa.vsearch.txt --userfields query+target+ql+pairs+id --id 0.6

# Filter the assignment with match lenth >= 70% and similarity >= 75% for Fungal Kingdom:
bin/FAST/fast.py -filter_taxonomy -i taxa.vsearch.txt -op taxa.vsearch.fungi.txt -match_length 0.7 -pident 75

# Remove all OTUs that are likely not be fungus:
bin/FAST/fast.py -assign_taxonomy -otu otu_table.txt -tax taxa.vsearch.fungi.txt -o otu_table.fungi.txt -remove_unassigned

# Filter the assignment for similarity >= 97% (species level):
bin/FAST/fast.py -filter_taxonomy -i taxa.vsearch.fungi.txt -op taxa.vsearch.species.txt -match_length 0 -pident 97

# Assign all speceis level taxonomy to the OTU table:
bin/FAST/fast.py -assign_taxonomy -otu otu_table.fungi.txt -tax taxa.vsearch.species.txt -o otu_table.taxa.txt

# Get a summary of the OTU table:
bin/FAST/fast.py -summary_otu_table -otu otu_table.taxa.txt -o otu_report2.txt

# Rarefy to a fixed depth with 1,000 iteration per sample:
bin/FAST/fast.py -rarefy_otu_table -otu otu_table.taxa.txt -o otu.table.taxa.rare.txt -d 14000 -iter 1000 -t 4
