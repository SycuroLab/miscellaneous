"""
Author: Daniel Castaneda Mogollon
Date: 08/09/2023
Purpose: This program is intended to write Checkm jobs in order for them to be run through ARC as a slurm job. It will generate a file containing the commands for it to be run
"""

import argparse

parser = argparse.ArgumentParser(description="test")

parser.add_argument('--input_path',type=str,help="This is the path to the directory where the assembly directories are found for each sample")
parser.add_argument('--output_dir',type=str,help="This is the prefix for the output directory for each checkm job finished")
parser.add_argument('--threads',type=int,help="This is the number of threads to be used per job")
parser.add_argument('--assembly_prefix',type=str,help="This is the name of the assembly prefix found in the output directories, i.e. unicycler_test")
parser.add_argument('--sample_file',type=str,help="This is the sample file that contains the name of the samples, i.e. list_files.txt")
parser.add_argument('--output_file',type=str,help="This is the name of the file where the bash commands will be generated, i.e. 1_checkm.sh")

args = parser.parse_args()

input_path = args.input_path
output_dir = args.output_dir
threads = args.threads
sample_file = args.sample_file
file_out = args.output_file
assembly_prefix = args.assembly_prefix

output_file = open(file_out,'w')
output_file.write("#!/bin/bash\n")
with open(sample_file,'r') as file:
    lines = file.readlines()
    for line in lines:
        line = line.strip()
        output_file.write("checkm data setRoot /bulk/IMCshared_bulk/shared/dbs/checkm_db; ")
        output_file.write("checkm lineage_wf -t "+str(threads)+" -x fasta --tab_table --file "+output_dir+"_"+line+"/checkm.tsv "+input_path+assembly_prefix+"_"+line+" "+output_dir+"_"+line+"\n")
