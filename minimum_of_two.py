#print "Enter number for element."

N = int(raw_input().strip())
final_list = []

for i in range(N):
	#print "Enter values for element."

	V = raw_input().strip().split(' ')

	if int(V[0]) < int(V[1]):
		final_list.append(V[0])
	else:
		final_list.append(V[1])
print ' '.join(final_list)
