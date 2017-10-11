import numpy as np
from scipy.io.wavfile import write
from sampler import Sampler


s = Sampler()

#z1 = s.generate_z()
#z2 = s.generate_z()

#d

with open('z1.npy', 'r') as f:
	z1 = np.load(f)
with open('z2.npy', 'r') as f:
	z2 = np.load(f)

diff = z1 - z2
	
#i = 1/0

outnum = 3
outpath = 'output'

singleCycle = 500
cycles = 6000

sound = np.zeros((singleCycle))
data = np.zeros((singleCycle * cycles))

delta = diff / cycles
#a = s.generate(z = (z1 + delta * j), x_dim = 2001, y_dim = 2001, scale = 10)
a = s.generate(z = (z1), x_dim = 2001, y_dim = 2001, scale = 10)

b = np.zeros_like(a)

circleCount = 0

#with open('soundArray.npy','r' ) as f:
#    data = np.load(f)

for j in range(0, cycles):
	

    #spiral = ((np.pi * 200) / ) * j
	
    offset1 = np.sin(j * 1.0 / 200)
    offset2 = np.cos(j * 1.0 / 200)
    

    for i in range((singleCycle)):
        #arc = ((np.pi * 2) / singleCycle) * i
	
        circleCount = circleCount + 1
    
        x1 = np.sin((circleCount *1.0) /400)
        y1 = np.cos((circleCount *1.0)/400)
	
        x2 = int(x1 * 800 + (offset1 * 100) + 1000)
        y2 = int(y1 * 800 + (offset2 * 100) + 1000)
	
        b[x2,y2,0] = 1
	
        data[j*singleCycle+i] = (a[x2, y2, 0] -.5) * 2
	
		#print sound[i]
    #with open('soundArray.npy','w') as f:
    #    np.save(f,data)
    print j
	
s.save_png(b, "%s/out%s.png" % (outpath, outnum))

	
#data = np.random.uniform(-1,1,44100) # 44100 random samples between -1 and 1
scaled = np.int16(data/np.max(np.abs(data)) * 32767)
write('%s/test%s.wav' % (outpath, outnum), 44100, scaled)