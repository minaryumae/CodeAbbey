N = int(raw_input().strip())
data = raw_input.strip().split(' ')
final_list = []
for j in range(N):
    if data[0] == insert:
        i = data[j][1]
        e = data[j][2]
        list.insert(i, e)
        print list