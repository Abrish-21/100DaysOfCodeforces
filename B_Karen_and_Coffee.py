freq_count = [0]* 200000
r,k,q = map(int, input().split())
for _ in range(r):
    l,r = map(int, input().split())
    freq_count[l] += 1
    if r + 1 < len(freq_count):
            freq_count[r + 1] -= 1 
for i in range(1, len(freq_count)):
    freq_count[i] += freq_count[i-1]

# step2: another prefix sum 
for i in range(len(freq_count)):
    if freq_count[i] < k:
          freq_count[i] = 0 
    else:
         freq_count[i] = 1

# print(freq_count)
# prefix_sum 
for i in range(1,len(freq_count)):
     freq_count[i] += freq_count[i-1]
    

print(freq_count[94])
print(freq_count[97])
print(freq_count[96])
print(freq_count[100])


    



