from __future__ import division

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

#print high_freq_dict


for codon in sorted(high_freq_dict.keys()):
	difference = high_freq_dict[codon] - low_freq_dict[codon]
	print codon + ' ' + str(difference) + ' ' + str(100*difference)+ '%'

