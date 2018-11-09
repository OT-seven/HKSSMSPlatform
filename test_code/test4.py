
#素数相加
N=100
i=2
num=2
s=0
for i in range(2,N):
  for num in range(2,i):
    if i%num==0:
      break
  else:
    s+=i
print(s)