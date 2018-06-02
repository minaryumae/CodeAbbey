#print "Enter number for element."

N = int(raw_input().strip())
final_list = []
V_new = []

for i in range(N):
	#print "Enter values for element."

	V = raw_input().strip().split(' ')
	if int(V[0]) < int(V[1]) and int(V[0]) < int(V[2]):
		smallest = int(V[0])
		if int(V[1]) < int(V[2]):
			final_list.append(V[1])
		else:
			final_list.append(V[2])
			
	elif int(V[1]) < int(V[0]) and int(V[1]) < int(V[2]):
		smallest = int(V[1])
		if int(V[0]) < int(V[2]):
			final_list.append(V[0])
		else:
			final_list.append(V[2])
			
	elif int(V[2]) < int(V[0]) and int(V[2]) < int(V[1]):
		smallest = int(V[2])
		if int(V[0]) < int(V[1]):
			final_list.append(V[0])
		else:
			final_list.append(V[1])
		
print ' '.join(final_list)
