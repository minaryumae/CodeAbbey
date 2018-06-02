#print "Enter number for element."
final_list = []
V = raw_input().strip().split(' ')
N = int(V[0])
for i in range(1, N + 1):
	#print "Enter values for element."
	F = int(V[i])
	C = int(round(round(int(F-32)*5)/float(9)))
	final_list.append(str(C))
print ' '.join(final_list)
