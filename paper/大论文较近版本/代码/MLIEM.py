from __future__ import print_function
import random

j=1;
while j<=2:
	print("Case:",j)
	j = j+1

	pro=1
	next=11
	count=0
	drr=0
	fore=0
	trend=0
	p = []
	x = []
	send = random.randint(0,1)
	res = random.randint(0,1)

	# print(send)
	# print(res)

	print("Please input N and M:")
	N = input()
	M = input()
	print("Please input u1 and u2:")
	u1 = input()
	u2 = input()
	print("Please input x[5]:")
	x.append(0)
	for i in range(1,6):
		print("x[",i,"]")
		t = input()
		x.append(t)
		fore = fore + x[i]
		if x[i]>x[i-1]:
			count = count+1;

	count = count -1
	print("count:",count)
	print("fore:",fore)

	fore = fore/5.0;
	print("fore:",fore)

	if count==0:
		trend = 0.1
	elif count==1:
		trend = 0.3
	elif count==2:
		trend = 0.5
	elif count==3:
		trend = 0.7
	elif count==4:
		trend = 0.9

	print("trend:",trend)

	fore = fore * trend;
	print("new fore:",fore)

	i=0
	while i<5:
		tt = random.randint(1,4)
		if tt==1:
			p.append(0.1)
		elif tt==2:
			p.append(0.35)
		elif tt==3:
			p.append(0.6)
		elif tt==4:
			p.append(0.85)
		i = i+1;

	print("p:",p[0],"  a:",p[1],"  s:",p[2],"  e:",p[3],"  m:",p[4])

	risk = (1-p[0]) * (1-p[1]) * (1-p[2]) * (1-p[3]) * (1-p[4])

	print("risk:",risk)

	# if send==1 and res==1:
	# 	print("1 1")
	# 	G1 = risk*(-N+M)
	# 	G2 = risk*(3*N)
	# 	print("G1:",G1,"  G2:",G2)
	# elif send==1 and res==0:
	# 	print("1 0")
	# 	G1 = risk*(-N)
	# 	G2 = risk*(3*N)
	# 	print("G1:",G1,"  G2:",G2)
	# elif send==0 and res==1:
	# 	print("0 1")
	# 	G1 = 0
	# 	G2 = 0
	# 	print("G1:",G1,"  G2:",G2)
	# elif send==0 and res==0:
	# 	print("0 0")
	# 	G1 = 0
	# 	G2 = 0
	# 	print("G1:",G1,"  G2:",G2)
	# else:
	# 	print("Error!")

	# drr = u1*fore + u2*G1
	# print("drr:",drr)



	
	print("1 1")
	G1 = risk*(-N+M)
	G2 = risk*(3*N)
	print("G1:",G1,"  G2:",G2)
	drr = u1*fore + u2*G1
	print("drr:",drr)


	print("1 0")
	G1 = risk*(-N)
	G2 = risk*(3*N)
	print("G1:",G1,"  G2:",G2)
	drr = u1*fore + u2*G1
	print("drr:",drr)



	print("0 1")
	G1 = 0
	G2 = 0
	print("G1:",G1,"  G2:",G2)
	drr = u1*fore + u2*G1
	print("drr:",drr)



	print("0 0")
	G1 = 0
	G2 = 0
	print("G1:",G1,"  G2:",G2)
	drr = u1*fore + u2*G1
	print("drr:",drr)

	


	

