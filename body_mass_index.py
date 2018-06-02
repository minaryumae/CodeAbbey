#print "Enter your weight in 	kilograms."
#print "Enter your height in meters."

N = int(raw_input().strip())
final_list = []



for i in range(N):

	V = raw_input().strip().split(' ')
	weight = int(V[0])
	height = float(V[1])
	BMI = weight/height**2
	
	if BMI < 18.5:
		final_list.append("under")
			
	elif 18.5 <= BMI and BMI < 25:
		final_list.append("normal")
		
	elif 25.0 <= BMI and BMI < 30:
		final_list.append("over")
		
	elif 30<= BMI:
		final_list.append("obese")
		
print ' '.join(final_list)
