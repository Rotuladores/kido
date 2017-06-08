import numpy

k=1 #prob lettere non vicine
v=1 #prob lettere vicine
g=0.8 #prob di digitare la lettera giusta
u=float(1)/26

plettere = numpy.array([[g,k,k,k,k,k,k,k,k,k,k,k,k,k,v,k,v,k,k,k,k,k,v,v,k,v,s],[k,g,k,k,k,k,v,v,k,k,k,k,k,v,k,k,k,k,k,k,k,v,k,k,k,k,s],[k,k,g,v,k,v,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,v,k,v,k,k,s],[k,k,v,g,v,v,k,k,k,k,k,k,k,k,k,k,k,v,v,k,k,k,k,v,k,k,s],[k,k,k,v,g,v,k,k,k,k,k,k,k,k,k,k,k,v,v,k,k,k,v,k,k,k,s],[k,k,v,v,k,g,v,k,k,k,k,k,k,k,k,k,k,v,k,v,k,v,k,k,k,k,s],[k,v,k,k,k,v,g,v,v,k,k,k,k,k,k,k,k,k,k,v,k,k,k,k,v,k,s],[k,v,k,k,k,k,v,g,k,v,k,k,k,v,k,k,k,k,k,k,v,k,k,k,v,k,s],[k,k,k,k,k,k,k,k,g,v,v,v,k,k,v,k,k,k,k,k,v,k,k,k,k,k,s],[k,k,k,k,k,k,k,v,v,g,v,k,v,v,k,k,k,k,k,k,v,k,k,k,k,k,s],[k,k,k,k,k,k,k,k,v,v,g,v,v,k,v,k,k,k,k,k,k,k,k,k,k,k,s],[k,k,k,k,k,k,k,k,k,k,v,g,k,k,v,v,k,k,k,k,k,k,k,k,k,k,s],[k,k,k,k,k,k,k,k,k,v,v,k,g,v,k,k,k,k,k,k,k,k,k,k,k,k,s],[k,v,k,k,k,k,k,v,k,v,k,k,v,g,k,k,k,k,k,k,k,k,k,k,k,k,s],[k,k,k,k,k,k,k,k,v,k,v,v,k,k,g,v,k,k,k,k,k,k,k,k,k,k,s],[k,k,k,k,k,k,k,k,k,k,k,v,k,k,v,g,k,k,k,k,k,k,k,k,k,k,s],[v,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,g,k,k,k,k,k,v,k,k,k,s],[k,k,k,v,v,v,v,k,k,k,k,k,k,k,k,k,k,g,k,v,k,k,k,k,k,k,s],[v,k,k,v,v,k,k,k,k,k,k,k,k,k,k,k,k,k,g,k,k,k,v,v,k,v,s],[k,k,k,k,k,v,v,k,k,k,k,k,k,k,k,k,k,v,k,g,k,k,k,k,v,k,s],[k,k,k,k,k,k,k,v,v,v,k,k,k,k,k,k,k,k,k,k,g,k,k,k,v,k,s],[k,v,v,k,k,v,v,k,k,k,k,k,k,k,k,k,k,k,k,k,k,g,k,k,k,k,s],[v,k,k,k,v,k,k,k,k,k,k,k,k,k,k,k,v,k,v,k,k,k,g,k,k,k,s],[k,k,v,v,k,k,k,k,k,k,k,k,k,k,k,k,v,k,k,k,k,k,k,g,k,v,s],[k,k,k,k,k,k,v,v,k,k,k,k,k,k,k,k,k,v,v,k,k,k,k,k,g,k,s],[v,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,v,k,k,k,k,v,k,g,s],[u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,1]])


