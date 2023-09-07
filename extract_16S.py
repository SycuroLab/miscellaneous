import os
import argparse
from Bio import SeqIO

parser = argparse.ArgumentParser(description = "This program was made to extract the 16S sequences from the .ffn output of a protein annotation program like prokka. You only need to provide the directory where the directories for each sample are found")

parser.add_argument("--input_dir", type=str, help="This is the annotation protein directory where each sample directory is found.")
parser.add_argument("--sample_file", type=str, help="This is the file where the sample names are located, i.e. list_files.txt")
parser.add_argument("--prefix_file", type=str, help="This is the prefix for each of the output files from the protein annotation program, i.e. from finished_prokka/prokka_test_S_NS6_Bs_032/S_NS6_Bs_032_prokka_output.ffn, this would be prokka_output")
parser.add_argument("--prefix_dir", type=str, help="This is the prefix for each sample directory, i.e. from finished_prokka/prokka_test_S_NS6_BS_032, this would be prokka_test")
args = parser.parse_args()

input_dir = args.input_dir
sample_file = args.sample_file
prefix_file = args.prefix_file
prefix_dir = args.prefix_dir

pattern = "16S ribosomal RNA"

with open(sample_file,"r") as file:
    lines = file.readlines()
    for line in lines:
        line = line.strip()
        input_file = input_dir+prefix_dir+"_"+line+"/"+line+"_"+prefix_file+".ffn"
        output_file = line+"_16S_sequences.fasta"
        for record in SeqIO.parse(input_file,"fasta"):
                                                                                                           1,1           Top
