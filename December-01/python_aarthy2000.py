print ("Think of a number ")
check =False
low=1
high=100
while check==False:
	print ("I Guessed");
	x=(int )(low+high)//2;
	print (x)
	print ("Is this number High,low or equal ?" )
	s=input()
	if s.lower()=="high" :
		high=x-1
		check=False
	elif s.lower()=="low" :
		low=x+1;
		check=False

	else:
		check=True
print ("U r there !.You thought of "+ str(x))

