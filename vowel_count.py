#print "Enter number for element."

N = int(raw_input().strip())
final_list = []

for i in range(N):
	#print "Enter values for element."

	V = raw_input().strip().split(' ')
	print V
	total = 0
	for j in range(len(V)):
		total += V[j].count('a')
		total += V[j].count('e')
		total += V[j].count('i')
		total += V[j].count('o')
		total += V[j].count('u')
		total += V[j].count('y')
	final_list.append(str(total))
print ' '.join(final_list)
