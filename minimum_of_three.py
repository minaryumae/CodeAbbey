#print "Enter number for element."

N = int(raw_input().strip())
final_list = []

for i in range(N):
	#print "Enter values for element."

	V = raw_input().strip().split(' ')
	if int(V[0]) < int(V[1]):
		smallest = int(V[0])
	elif int(V[0]) > int(V[1]):
		smallest = int(V[1])
	if smallest < int(V[2]):
		final_list.append(str(smallest))
	elif smallest > int(V[2]):
		final_list.append(V[2])
print ' '.join(final_list)
