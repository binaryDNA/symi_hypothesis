# symi_hypothesis
# ===============
#
# This python script shows the SYMI Hypothesis in action. 
# Copyright: Dimitrios Mitsinikos.
#
# For more information, please go to 
# http://dna.mitsinikos.net
# http://dna.mitsinikos.net/symi-hypothesis
#
# The following python script requires matplotlib and generates this graph: 
# http://dna.mitsinikos.net/wp-content/uploads/2013/10/SYMI_2m_calculations.png

from pylab import *
from math import *

S,Y,M,I,D = [],[],[],[],[]

for d in range (2, 2000000):

	m = d*log(d)
	s = ceil(m)
	y=2**ceil(log(s)/log(2))
	i= y-m
	
	D.append(d)	
	S.append(s)
	Y.append(y)	
	M.append(m)
	I.append(i)

desc = "DNA uses the optimal number of outputs (21).\nAt point D=21, the 'Level of Inefficiency' I, has\nthe lowest possible value (I=0.07)"

annotate("Testing 2 million D values", xy=(20, 2000000))
annotate(desc, xy=(21, 0.06), arrowprops=dict(arrowstyle='->'), xytext=(180, 0.018))

plot(D,I)

xscale("log", nonposx='clip')
yscale("log", nonposy='clip')

xlabel('D values (log)')
ylabel('I values (log)')
title('SYMI Hypothesis')

grid(True)
show()
