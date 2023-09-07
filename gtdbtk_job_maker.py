"""
Author: Daniel Castaneda Mogollon
Date: 08/16/2023
Purpose: The purpose of this script is to create a series of GTDBTK commands to identify taxonomic lineage at the species lever. The output could be run through a bash file. Alternatively you can run the output shell file into a slurm file if this is run through a HPC server.
"""

import argparse

parser = argparse.ArgumentParser(description="This program was created to generate GTDBTK jobs that can be run through a slurm file in the server. Simply copy and paste the output of this command into a slurm file, or run the slurm file calling the output bash job")
print('''This job requires the following information:
        --input_path [STR] [Path to where the Unicycler folders are for each sample]
        --output_file [STR] [Name of the bash job that will create the series of GTDBTK commands]
        --threads [NUM] [Recommended to run with higher than 24]
        --file_extension [STR] [The file extension for the assembly files, i.e. .fa, .fastq (type with the dot)]
        --output_dir [STR] [The output directory where you want the GTDBTK files per sample]
        --sample_file [STR] [Name of the file containing the prefix of the sample names]
        --gtdbtk_prefix [STR] [Prefix name for the output directory, i.e gtdbtk_test, gtdbtk_output]
        --assembly_prefix_dir [STR] [Prefix of the directories where the assembly files are for each sample, i.e. unicycler_test
        ''')

parser.add_argument('--input_path',type=str)
parser.add_argument('--output_file',type=str)
parser.add_argument('--threads',type=int)
parser.add_argument('--file_extension',type=str)
parser.add_argument('--output_dir',type=str)
parser.add_argument('--sample_file',type=str)
parser.add_argument('--gtdbtk_prefix',type=str)
parser.add_argument('--assembly_prefix_dir',type=str)

args = parser.parse_args()
input_path = args.input_path
file_out = args.output_file
num_threads = args.threads
file_extension = args.file_extension
output_dir = args.output_dir
sample_file = args.sample_file
gtdbtk_prefix = args.gtdbtk_prefix
assembly_prefix_dir = args.assembly_prefix_dir

output_file = open(file_out,"w")
output_file.write("#!/bin/bash\n")
with open(sample_file,"r") as file:
    lines = file.readlines()
    for line in lines:
        line = line.strip()
        output_file.write("gtdbtk classify_wf --genome_dir "+input_path+assembly_prefix_dir+"_"+line+" --extension \"fasta\" --cpus "+str(num_threads)+" --out_dir "+output_dir+"/"+gtdbtk_prefix+"_"+line+";\n")
output_file.close()
