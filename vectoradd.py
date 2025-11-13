def dot(a,b):
	s=0
	for i,x in enumerate(a):
		s+=x*b[i]
	return s

v1=[1,2,3]
v2=[4,5,6]
print(dot(v1,v2))	
