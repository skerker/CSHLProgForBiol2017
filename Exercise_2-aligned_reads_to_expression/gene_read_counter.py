#!/usr/bin/env python

import os, sys, re
import subprocess

usage = "\n\n\tusage: {} trans_alignments.bam\n\n\n"

if len(sys.argv) < 2:
    sys.stderr.write(usage)
    sys.exit(1)


def main():

    # capture command line argument
    bam_filename = sys.argv[1]

    # create hashtable for storing reads associated with genes
    gene_read_counter = dict()

    # run command to convert bam to sam
    cmd = "samtools view {}".format(bam_filename)
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # read the sam formatted output line by line
    for line in p.stdout:
        line = line.rstrip()

        # split line into the tab-delimited fields, grab the read and transcript ids
        fields = line.split("\t")
        read_name = fields[0]
        transcript = fields[2]

        # transcript name has format:  gene^transcript
        # capture the gene identifier
        
        (gene_name, transcript_name) = transcript.split("^")

        # increment the read count for that gene
        if gene_name in gene_read_counter:
            read_set = gene_read_counter[gene_name]
            read_set.add(read_name)
        else:
            gene_read_counter[gene_name] = set(read_name)
    
    ret = p.wait()

    if ret:
        # something bad happened... script should exit with non-zero:
        errmsg = "\n".join(p.stderr.readlines())
        sys.stderr.write(errmsg)
        sys.exit(ret)


    # generate report
    for gene_name in sorted(gene_read_counter, key=lambda x:len(gene_read_counter[x]), reverse=True):
        read_set = gene_read_counter[gene_name]
        num_reads = len(read_set)
        print("\t".join([gene_name, str(num_reads)]))
    
    sys.exit(0)
    


if __name__ == '__main__':
    main()
