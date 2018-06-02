print "Enter number for element."

N = int(raw_input().strip())
print "Enter values for element."

V = raw_input().strip().split(' ')
total = 0

for i in range(N):
	total += int(V[i])
print total
