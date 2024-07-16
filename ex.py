target = 2
hours = [0,1,2,3,4]
ans = []

for i in hours:
    if i >= target:
        ans.append(i)
print(len(ans))
