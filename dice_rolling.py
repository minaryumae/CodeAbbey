#print "Enter number for element."

N = int(raw_input().strip())
final_list = []
V_new = []

for i in range(N):
	#print "Enter values for element."

	
	V = raw_input().strip()
	number = 6 * float(V)
	number = int(number)
	number += 1
	final_list.append(str(number))
			
	
		
print ' '.join(final_list)
