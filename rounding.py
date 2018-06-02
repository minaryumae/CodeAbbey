#print "Enter number for element."

N = int(raw_input().strip())
final_list = []

for i in range(N):
	#print "Enter values for element."

	V = raw_input().strip().split(' ')
	quotient = int(round(int(V[0])/float(int(V[1]))))

	final_list.append(str(quotient))
print ' '.join(final_list)
