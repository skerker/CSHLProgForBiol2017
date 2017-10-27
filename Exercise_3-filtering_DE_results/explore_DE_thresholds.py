#!/usr/bin/env python

import os, sys


class DE_entry:
    transcript = None
    logFC = None
    FDR = None


my_DE_entries = list()

with open("ph8_vs_std.edgeR.DE_results.txt") as fh:
    header_line = fh.next()
    for line in fh:
        line = line.rstrip()
        fields = line.split("\t")
        transcript_name = fields[0]
        logFC = float(fields[1])
        FDR = float(fields[4])

        de_entry = DE_entry()
        de_entry.transcript = transcript_name
        de_entry.logFC = abs(logFC)
        de_entry.FDR = FDR

        my_DE_entries.append(de_entry)


FDR_range = [0.05, 0.001, 1e-5, 1e-10, 0]
logFC_range = [1, 2, 3, 4, 5]

print("\t".join(["max_FDR", "min_logFC", "num_transcripts"]))

for FDR in FDR_range:
    for logFC in logFC_range:
        de_entry_in_range = [de_entry for de_entry in my_DE_entries if de_entry.logFC >= logFC and de_entry.FDR <= FDR]
        print("\t".join([str(FDR), str(logFC), str(len(de_entry_in_range))]))


sys.exit(0)
