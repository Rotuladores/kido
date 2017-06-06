import numpy

def viterbi(P, T, O, S):
	current_max = numpy.zeros(P.shape[0])
	maxs = numpy.zeros((P.shape[0], S.shape[0]))
   	for j in range(0,len(P)):
		current_max[j] = P[j]*O[j,S[0]]
	ind = numpy.argmax(current_max);
	maxs[ind,0] = 1;
	for i in range (1,len(S)):
        	maximi = numpy.zeros(len(P))
        	for z in range (0,len(P)):
        		current = numpy.zeros(len(P))
        		for j in range (0,len(P)):
                		current[j] = current_max[j]*T[j,z]*O[z,S[i]];
 	       		m = max(current)
			ind = numpy.argmax(current)
        		maximi[z] = m
            		maxs[z,i] = ind
      		current_max = maximi;

	out = numpy.argmax(current_max);
	v = [out];
	for x in range (len(S)-1 ,0, -1):
		y = numpy.array([maxs[int(v[0]), x]])
       		v = numpy.concatenate([y, v]);
	return v
	

a = 1/float(6)
P = numpy.array([0.52, 0.48])
T = numpy.array([[0.6, 0.4], [0.17, 0.83]])
O = numpy.array([[0.1, 0.1, 0.1, 0.1, 0.1, 0.5], [a, a, a, a, a, a]])
S = numpy.array([2, 0, 5, 5, 5, 3])

v = viterbi(P, T, O, S)
print(v)
