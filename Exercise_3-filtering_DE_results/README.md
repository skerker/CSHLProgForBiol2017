# Examine Differential Expression

Numbers of DE features are a function of threshold criteria such as minimum statistical signficance (FDR) and minimum log fold change.

The file 'ph8_vs_std.edgeR.DE_results.txt' contains the results from a differential expression experiment run using edgeR.  The data correspond to an experiment involving the fungal pathogen Candida albicans grown in standard media (std) vs. media with an adjusted pH level (pH8). The format of the data is like so:

    Transcript      logFC   logCPM  PValue  FDR
    TRINITY_DN5022_c0_g2_i1 10.0401687977833        10.9152576386253        0       0
    TRINITY_DN87_c0_g2_i1   9.14950563541908        11.6407970888824        0       0
    ...
    TRINITY_DN4853_c0_g1_i1 1.42888379312822        6.41667934418826        1.72386809265937e-24    9.20405134023116e-24
    TRINITY_DN1003_c0_g1_i1 2.48674371027359        5.09336876108768        1.84284725773483e-24    9.8323983863564e-24
    TRINITY_DN3347_c0_g1_i1 1.13992703633498        7.35299541554418        1.93657730673848e-24    1.03252435225334e-23
    ...
    TRINITY_DN1911_c0_g1_i1 0.00227170107111927     5.28086241788254        1       1
    TRINITY_DN4318_c0_g1_i1 -0.00225181824263063    6.06492389728736        1       1



Write a python program that reports the number of differentially expressed transcripts detected according to a minimum logFC and maximum FDR given the ranges:

    FDR_range = [0.05, 0.001, 1e-5, 1e-10, 0]
    logFC_range = [1, 2, 3, 4, 5]

looking at all combinations of the above values.

Your output may look like so:

    max_FDR	min_logFC	num_transcripts
    0.05	1	3102
    0.05	2	1587
    ...
    0.001	3	658
    0.001	4	353
    ...
    1e-10	2	1016
    1e-10	3	508
    ...
    0	4	57
    0	5	36


>Advanced: store the results in a multi-dimensional data structure and output the data in a matrix form with columns(FDR_range) and rows(logFC_range).   ex.   num_transcripts = data[max_FDR][min_logFC]

