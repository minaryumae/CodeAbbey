V = raw_input().strip().split(' ')
N = len(V)
final_list = []

if int(V[0]) < int(V[1]):
	smallest = int(V[0])
	largest = int(V[1])
elif int(V[0]) > int(V[1]):
	smallest = int(V[1])
	largest = int(V[0])
	
for i in range(2, N):
	if largest < int(V[i]):
		largest = int(V[i])
		
	elif smallest > int(V[i]):
		smallest = int(V[i])
final_list.append(str(largest))
final_list.append(str(smallest))
print ' '.join(final_list)


24
0.647150957026
0.987115122844
0.865972751286
0.896573067177
0.621044113766
0.168384324759
0.795170877129
0.654232886154
0.403128709178
0.199963932391
0.27748399321
0.286042954773
0.653460169677
0.859494392294
0.195051797666
0.611783667468
0.74828169588
0.00758656859398
0.869659913704
0.264864529017
0.725997001398
0.55784617085
0.461213982198
0.187693074811