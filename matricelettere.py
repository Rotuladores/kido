import numpy
#sistemiamo

#prob lettere non vicine
v2 = float(1)/20
v3 = float(1)/30
v4 = float(1)/40
v5 = float(1)/50
v6 = float(1)/60
v7 = float(1)/70

#prob lettere vicine
k2 = float((1-0.8-v2*2))/24
k3 = float((1-0.8-v3*3))/23
k4 = float((1-0.8-v4*4))/22
k5 = float((1-0.8-v5*5))/21
k6 = float((1-0.8-v6*6))/20
k7 = float((1-0.8-v7*7))/19

#prob rimozione/aggiunzione
s2 = 1-0.8-v2*2-k2*23
s3 = 1-0.8-v3*3-k3*22
s4 = 1-0.8-v4*4-k4*21
s5 = 1-0.8-v5*5-k5*20
s6 = 1-0.8-v6*6-k6*19
s7 = 1-0.8-v7*7-k7*18

g=0.8 #prob di digitare la lettera giusta
u=float(1)/26

plettere = numpy.array([[g,k5,k5,k5,k5,k5,k5,k5,k5,k5,k5,k5,k5,k5,v5,k5,v5,k5,k5,k5,k5,k5,v5,v5,k5,v5,s5],[k4,g,k4,k4,k4,k4,v4,v4,k4,k4,k4,k4,k4,v4,k4,k4,k4,k4,k4,k4,k4,v4,k4,k4,k4,k4,s4],[k4,k4,g,v4,k4,v4,k4,k4,k4,k4,k4,k4,k4,k4,k4,k4,k4,k4,k4,k4,k4,v4,k4,v4,k4,k4,s4],[k6,k6,v6,g,v6,v6,k6,k6,k6,k6,k6,k6,k6,k6,k6,k6,k6,v6,v6,k6,k6,k6,k6,v6,k6,k6,s6],[k5,k5,k5,v5,g,v5,k5,k5,k5,k5,k5,k5,k5,k5,k5,k5,k5,v5,v5,k5,k5,k5,v5,k5,k5,k5,s5],[k6,k6,v6,v6,k6,g,v6,k6,k6,k6,k6,k6,k6,k6,k6,k6,k6,v6,k6,v6,k6,v6,k6,k6,k6,k6,s6],[k6,v6,k6,k6,k6,v6,g,v6,v6,k6,k6,k6,k6,k6,k6,k6,k6,k6,k6,v6,k6,k6,k6,k6,v6,k6,s6],[k6,v6,k6,k6,k6,k6,v6,g,k6,v6,k6,k6,k6,v6,k6,k6,k6,k6,k6,k6,v6,k6,k6,k6,v6,k6,s6],[k5,k5,k5,k5,k5,k5,k5,k5,g,v5,v5,v5,k5,k5,v5,k5,k5,k5,k5,k5,v5,k5,k5,k5,k5,k5,s5],[k6,k6,k6,k6,k6,k6,k6,v6,v6,g,v6,k6,v6,v6,k6,k6,k6,k6,k6,k6,v6,k6,k6,k6,k6,k6,s6],[k5,k5,k5,k5,k5,k5,k5,k5,v5,v5,g,v5,v5,k5,v5,k5,k5,k5,k5,k5,k5,k5,k5,k5,k5,k5,s5],[k3,k3,k3,k3,k3,k3,k3,k3,k3,k3,v3,g,k3,k3,v3,v3,k3,k3,k3,k3,k3,k3,k3,k3,k3,k3,s3],[k3,k3,k3,k3,k3,k3,k3,k3,k3,v3,v3,k3,g,v3,k3,k3,k3,k3,k3,k3,k3,k3,k3,k3,k3,k3,s3],[k4,v4,k4,k4,k4,k4,k4,v4,k4,v4,k4,k4,v4,g,k4,k4,k4,k4,k4,k4,k4,k4,k4,k4,k4,k4,s4],[k4,k4,k4,k4,k4,k4,k4,k4,v4,k4,v4,v4,k4,k4,g,v4,k4,k4,k4,k4,k4,k4,k4,k4,k4,k4,s4],[k2,k2,k2,k2,k2,k2,k2,k2,k2,k2,k2,v2,k2,k2,v2,g,k2,k2,k2,k2,k2,k2,k2,k2,k2,k2,s2],[v3,k3,k3,k3,k3,k3,k3,k3,k3,k3,k3,k3,k3,k3,k3,k3,g,k3,v3,k3,k3,k3,v3,k3,k3,k3,s3],[k5,k5,k5,v5,v5,v5,v5,k5,k5,k5,k5,k5,k5,k5,k5,k5,k5,g,k5,v5,k5,k5,k5,k5,k5,k5,s5],[v6,k6,k6,v6,v6,k6,k6,k6,k6,k6,k6,k6,k6,k6,k6,k6,k6,k6,g,k6,k6,k6,v6,v6,k6,v6,s6],[k4,k4,k4,k4,k4,v4,v4,k4,k4,k4,k4,k4,k4,k4,k4,k4,k4,v4,k4,g,k4,k4,k4,k4,v4,k4,s4],[k4,k4,k4,k4,k4,k4,k4,v4,v4,v4,k4,k4,k4,k4,k4,k4,k4,k4,k4,k4,g,k4,k4,k4,v4,k4,s4],[k4,v4,v4,k4,k4,v4,v4,k4,k4,k4,k4,k4,k4,k4,k4,k4,k4,k4,k4,k4,k4,g,k4,k4,k4,k4,s4],[v4,k4,k4,k4,v4,k4,k4,k4,k4,k4,k4,k4,k4,k4,k4,k4,v4,k4,v4,k4,k4,k4,g,k4,k4,k4,s4],[k4,k4,v4,v4,k4,k4,k4,k4,k4,k4,k4,k4,k4,k4,k4,k4,v4,k4,k4,k4,k4,k4,k4,g,k4,v4,s4],[k4,k4,k4,k4,k4,k4,v4,v4,k4,k4,k4,k4,k4,k4,k4,k4,k4,v4,v4,k4,k4,k4,k4,k4,g,k4,s4],[v3,k3,k3,k3,k3,k3,k3,k3,k3,k3,k3,k3,k3,k3,k3,k3,k3,k3,v3,k3,k3,k3,k3,v3,k3,g,s3],[u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,1]])

#print(plettere)
somma = 0
for i in range(0,26):
	somma = 0
	for j in range(0,27):
		somma = somma+plettere[i][j]
	print(somma)

numpy.savetxt('/home/federica/Documenti/Rotuladores/misspelling/matrice.txt', plettere, delimiter=',')

