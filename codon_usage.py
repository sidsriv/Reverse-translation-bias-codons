from __future__ import division


map = {"TTT":"F", "TTC":"F", "TTA":"L", "TTG":"L",
    "TCT":"S", "TCC":"s", "TCA":"S", "TCG":"S",
    "TAT":"Y", "TAC":"Y", "TAA":"STOP", "TAG":"STOP",
    "TGT":"C", "TGC":"C", "TGA":"STOP", "TGG":"W",
    "CTT":"L", "CTC":"L", "CTA":"L", "CTG":"L",
    "CCT":"P", "CCC":"P", "CCA":"P", "CCG":"P",
    "CAT":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
    "CGT":"R", "CGC":"R", "CGA":"R", "CGG":"R",
    "ATT":"I", "ATC":"I", "ATA":"I", "ATG":"M",
    "ACT":"T", "ACC":"T", "ACA":"T", "ACG":"T",
    "AAT":"N", "AAC":"N", "AAA":"K", "AAG":"K",
    "AGT":"S", "AGC":"S", "AGA":"R", "AGG":"R",
    "GTT":"V", "GTC":"V", "GTA":"V", "GTG":"V",
    "GCT":"A", "GCC":"A", "GCA":"A", "GCG":"A",
    "GAT":"D", "GAC":"D", "GAA":"E", "GAG":"E",
    "GGT":"G", "GGC":"G", "GGA":"G", "GGG":"G",}

rev_codon_table = {
    'A': ('GCT', 'GCC', 'GCA', 'GCG'),
    'C': ('TGT', 'TGC'),
    'D': ('GAT', 'GAC'),
    'E': ('GAA', 'GAG'),
    'F': ('TTT', 'TTC'),
    'G': ('GGT', 'GGC', 'GGA', 'GGG'),
    'I': ('ATT', 'ATC', 'ATA'),
    'H': ('CAT', 'CAC'),
    'K': ('AAA', 'AAG'),
    'L': ('TTA', 'TTG', 'CTT', 'CTC', 'CTA', 'CTG'),
    'M': ('ATG',),
    'N': ('AAT', 'AAC'),
    'P': ('CCT', 'CCC', 'CCA', 'CCG'),
    'Q': ('CAA', 'CAG'),
    'R': ('CGT', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'),
    'S': ('TCT', 'TCC', 'TCA', 'TCG', 'AGT', 'AGC'),
    'T': ('ACT', 'ACC', 'ACA', 'ACG'),
    'V': ('GTT', 'GTC', 'GTA', 'GTG'),
    'W': ('TGG',),
    'Y': ('TAT', 'TAC'),
    '*': ('TAA', 'TAG', 'TGA'),
}

with open('low_expression_frequencies.txt') as file:
    data1 = []
    for line in file:
        data1.append(line[:-1])

total_low = data1[0][data1[0].find(':')+1:]
low_freq_dict = dict()
for line in data1[1:]:
    codon = line.split()[0]
    freq = float(line.split()[1])
    low_freq_dict[codon] = freq

#print low_freq_dict

with open('high_expression_frequencies.txt') as file:
    data2 = []
    for line in file:
        data2.append(line[:-1])

total_high = data2[0][data2[0].find(':')+1:]
high_freq_dict = dict()
for line in data2[1:]:
    codon = line.split()[0]
    freq = float(line.split()[1])
    high_freq_dict[codon] = freq

#print high_freq_dict()
for protein in rev_codon_table.keys():
    num_codon = list(rev_codon_table[protein])
    if len(num_codon) == 1:
        summ = low_freq_dict[num_codon[0]]
        print protein+' '+num_codon[0]+' '+str((low_freq_dict[num_codon[0]]/summ)*100)+'%'
    else:
        summ = 0
        for i in num_codon:
            summ += low_freq_dict[i]
        for i in num_codon:
            print protein+' '+i+' '+str((low_freq_dict[i]/summ)*100)+'%'




