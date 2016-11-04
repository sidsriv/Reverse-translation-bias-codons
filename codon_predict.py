#from collections import defaultdict
import sys
import numpy as np

peptide = sys.argv[1]
filename = sys.argv[2]
with open(filename) as file:
	data = []
	for line in file:
		data.append(line[:-1])
codon_usage = dict()
for i in range(2,len(data)):
	p,codon, percentage = data[i].split()
	percentage = float(percentage[:-1])/100
	if p in codon_usage.keys():
		codon_usage[p].append((codon,percentage))
	else:
		codon_usage[p] = [(codon,percentage)]
#for protein in codon_usage:
	#print protein , codon_usage[protein]

def reverse_translate(protein,usage_table):
	gene = ''
	for aa in protein:
		candidate_codon = []
		candidate_percent = []
		for codon in usage_table[aa]:
			candidate_codon.append(codon[0])
			candidate_percent.append(codon[1])
		rand_codon = np.random.choice(candidate_codon,1,p=candidate_percent)
		gene += str(rand_codon)[2:-2]
	return gene


if __name__ == '__main__':
	ans = reverse_translate(peptide,codon_usage)
	print ans