import argparse
import os

parser = argparse.ArgumentParser(description = "This program was generated to create blastn jobs to look for homologous or equivalent sequences from a list of fasta files")
parser.add_argument("--input_dir", type = str, help="This is the input directory where the 16S (or equivalent) fasta files are located")
parser.add_argument("--output_file", type = str, help="This is the shell output file, i.e. 1_blast.sh")
#parser.add_arugment("--sample_file", type = str, help="This is the sample file that contains the name of all samples, i.e. sample_file.txt")

args = parser.parse_args()
input_dir = args.input_dir
output_file = args.output_file
#sample_file = args.sample_file
out_file = open(output_file,"w")
out_file.write("#!/bin/bash\n")
for files in os.listdir(input_dir):
    test = files.split("_")
    out_name = (test[1]+"_"+test[2]+"_"+test[3]+"_"+test[4])
    out_file.write("blastn -query "+input_dir+files+" -db /bulk/sycuro_bulk/lsycuro_labshare/blastdbs/GTDB_16S_r202/GTDB_16S_r202 -evalue 1e-05 -max_target_seqs 10 -num_threads 10 -out "+out_name+"_output.txt -outfmt \"7 qseqid salltitles score qlen qstart qend sstart ssend length evalue pident\"\n")
