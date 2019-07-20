a, b = map(float,input().split())
k = (a/b)
if a < b:
	print(-1)
else:
	if(k % 2 == 1):
		k += 1;
	ans = 1.0*(a+b)/k
	print("%.12lf\n"%(ans))












