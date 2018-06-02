#print "Enter number for element."

N = int(raw_input().strip())
final_list = []

for i in range(N):
	#print "Enter values for element."

	V = raw_input().strip().split(' ')
	weighted_value = 0
	for j in range(len(V[i])):	
		weighted_value += int(V[i][j]) * (j + 1)

	final_list.append(str(weighted_value))
print ' '.join(final_list)
