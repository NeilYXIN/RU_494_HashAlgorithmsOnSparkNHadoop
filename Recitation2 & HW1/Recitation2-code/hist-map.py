#!/usr/bin/env python
import sys
import numpy

### Prevents pipe IO errors for large files.
from signal import signal, SIGPIPE, SIG_DFL
signal(SIGPIPE,SIG_DFL)
###

# read parameters from distributed cache - nbins, minmeanmax
f = open('nbins','r') # read nbins file
params = f.readline().strip().split() # read nbins file
nbins = int(params[0]) # set maximum number of bins
f.close()

f = open('mmm','r') # open mmm file

'''
Read mmm file and assign min, max and mean values.
File read operation in similar to above reading procedure.
'''
params =  f.readline().strip().split()
xmax = float(params[1]) 
params = f.readline().strip().split()
xmean = float(params[1])
params = f.readline().strip().split()
xmin = float(params[1])
f.close()



dx = (xmax-xmin)/nbins # bin width calculation


# compute bin centre
#### complete this code
for line in sys.stdin:
    line = line.strip()

    words = line.split()
    x = float(words[0])
    if xmax-x<=0 :
        bn = int((x-xmin)/dx)-1
    else:
        bn = int((x-xmin)/dx)
    bc = bn * dx + xmin +dx/2
    strbc = str(bc)


# process input data
#### complete this code
    print '%s\t%d' %(strbc,1);




