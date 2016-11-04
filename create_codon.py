from __future__ import division
import sys
from collections import Counter


filename = sys.argv[1]

with open(filename) as file:
	data = []
	for line in file:
		data.append(line[:-1])
lowexpressed = []
highexpressed = []
if filename == 'lowexpressed.txt':
	myosinXXI = data[0]
	coronin = data[1]
	ARP4 = data[2]
	lowexpressed = [myosinXXI,coronin,ARP4]
else:
	ADF = data[0]
	twinfilin = data[1]
	ARP1 = data[2]
	highexpressed = [ADF,twinfilin,ARP1]

def create_codon(genes):
	sequence = ''
	for gene in genes:
		sequence += gene
	codons = []
	nucleotides = len(sequence)
	codon_number = int(nucleotides/3)
	for i in range(codon_number):
		codons.append(sequence[3*i:3*(i+1)])
	return codons

def codon_frequency(codons):
	codon_frequency = Counter(codons)
	return codon_frequency


if __name__ =='__main__':
	if lowexpressed == []:
		codons = create_codon(highexpressed)
	else:
		codons = create_codon(lowexpressed)
	occurence_frequency = codon_frequency(codons)
	total = sum(occurence_frequency.values())
	print 'Total Codons:' + str(total)
	for codon in sorted(occurence_frequency):
		print codon + '   ' + str(occurence_frequency[codon]/total)
	'''
	with open('res.txt') as file:
		file.write('Total Codons:' + str(total))
		for codon in occurence_frequency:
			file.write(codon + '   ' + str(occurence_frequency[codon]/total))
	'''
