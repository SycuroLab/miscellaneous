# miscellaneous
The current jobs for this repository vary in purpose. The unicycler, checkm, and quast jobs can (and probably should) be run as part of the same workflow. The unicycler job maker will take polished reads (i.e. prinseq, trimmomatic) and assemble the genomes. Then it is recommended to run quast and the checkm scripts to determine the quality of the genomes.

Each one of these scripts takes input from the user:

## Unicycler
The arguments for this program are:
--input_path [str] (This is a string where the user should specify where the folder with all the illumina polish read files are located. This should be a folder with all the files in it, rather than an individual folder per sample, i.e. ../../plate2/contigs_1000/all_output/prinseq/).
--output_file [str] (This is a string where the user should specify the name of the output bash file where the sequential jobs will be written to, i.e. 1_unicycler_job.sh).
--threads [int] (The number of threads to be run in each sequential job. Given that unicycler takes its time, I'd recommend running it with >40 threads, i.e. 40).
--mode [str] (There are three modes in unicycler: 'normal', 'bold', and 'conservative', see below for explanation from the github unicycler website, i.e. normal)
--illumina_suffix [str] (This is the suffix found for the polished read files. Typically this is user-assigned and it's the name after the sample name. i.e. _filtered)
--file_extension [str] (This is the type of extension for the polished read files. i.e. .fastq)
--output_dir [str] (This is the prefix that the directories for EACH SAMPLE will have. i.e unicycler_test
--sample_file [str] (This is the name of the file where the sample names are located. i.e. list_files.txt




