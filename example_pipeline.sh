bin/FAST/fast.py -generate_mapping -i read1

bin/FAST/fast.py -add_labels -m mapping.txt -i read1 -o read1_labeled -t 4

bin/FAST/fast.py -merge_seqs -i read1_labeled -o raw.fastq

bin/cutadapt raw.fastq -a GCATCGATGAAGAACGCAGC -g CTTGGTCATTTAGAGGAAGTAA -o raw.cut.fastq --time=2

bin/vsearch --fastq_filter raw.cut.fastq --fastq_maxee 1 --fastaout raw.cut.trim.fasta --fasta_width 0

bin/FAST/fast.py -filter_seqs -i raw.cut.trim.fasta -o raw.cut.trim.N0.homop9.fasta -maxN 0 -maxhomop 9

bin/FAST/fast.py -stat_seqs -i raw.cut.trim.N0.homop9.fasta -o qc_report.txt

bin/FAST/fast.py -truncate_seqs -i raw.cut.trim.N0.homop9.fasta -l 200 -o raw.qc.L200.fasta

bin/FAST/fast.py -dereplicate -i raw.qc.L200.fasta -o raw.qc.derep -t 4

bin/FAST/fast.py -filter_otu_map -i raw.qc.derep.txt -o raw.qc.derep.size2.txt -min_size 2

bin/FAST/fast.py -pick_seqs -i raw.qc.derep.fasta -map raw.qc.derep.size2.txt -o raw.qc.derep.size2.fasta -sizeout

bin/vsearch --uchime_denovo raw.qc.derep.size2.fasta --nonchimeras raw.qc.derep.size2.uchime.fasta --sizeout --fasta_width 0

bin/vsearch -cluster_size raw.qc.derep.size2.uchime.fasta --centroids raw.qc.vsearch.fasta --fasta_width 0 -id 0.97 --sizein --uc raw.qc.uc.txt

bin/FAST/fast.py -parse_uc_cluster -i raw.qc.uc.txt -o raw.qc.vsearch.txt

bin/FAST/fast.py -generate_fast_map -map raw.qc.derep.size2.txt -seq raw.qc.derep.size2.uchime.fasta -o fast.derep.txt -derep

bin/FAST/fast.py -generate_fast_map -map raw.qc.vsearch.txt -seq raw.qc.vsearch.fasta -o fast.otu.txt -otu

bin/FAST/fast.py -combine_fast_map -derep_map fast.derep.txt -otu_map fast.otu.txt -o fast.hybrid.txt

bin/FAST/fast.py -rename_otu_map -fast_map fast.hybrid.txt -o fast.hybrid.otu.txt

bin/FAST/fast.py -make_otu_table -fast_map fast.hybrid.otu.txt -o otu_table.txt -rep rep_seq.fasta

bin/FAST/fast.py -rarefy_otu_table -otu otu_table.txt -o otu_table.rare.txt -d 3000 -iter 1000 -t 4

blastn -db database/unite_filter -query rep_seq.fasta -max_target_seqs 1 -outfmt "6 qseqid stitle qlen length pident evalue" -out taxonomy_blast.txt

bin/FAST/fast.py -assign_taxonomy -otu otu_table.rare.txt -tax taxonomy_blast.txt -o otu_table.rare.tax.txt

bin/FAST/fast.py -otu_deconstruct -map fast.hybrid.otu.txt -o otu_deconstruct
