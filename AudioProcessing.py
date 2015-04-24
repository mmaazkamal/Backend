__author__ = 'HP'


import numpy as np
import matplotlib.pyplot as plt
from utility import pcm2float
from utility import float2pcm
import scipy.io.wavfile as wav
from AcousticGuids import load_signature


#variable handels
guidStart=8
nbits=5
timeEmbed=5
convert_16_bit = float(2**15)
ampAudio=.49
fDelay=(nbits+1)+nbits+nbits*2                          #Complete Delay of the Signature
#end


# TODO: allow python should be able to fetch the audio and a dictionary of GUIDS to be embedded and its corresponding time stamps. For now, there is just an array of avialable GUIDs

guids=['{0:05b}'.format(x) for x in range(guidStart,2**nbits)] # Avialable Guids

# TODO: perform the following function with the audio from the server

sample_rate, x = wav.read('papa.wav')                   #Read input File
#x=.49*x                                                #Done later
print "1 Data type is:", x.dtype                        # Confirm Audio Tyspe before conversion; this should int16
xNormalized = (x / (convert_16_bit + 1.0))*ampAudio     # Normalize and convert to float64 and recale it to max amplitude at .49
print "2 Data type is:", xNormalized.dtype              # Confirm Audio Type after  conversion; this should float64

# TODO: catch if two interactions intersect

signature=load_signature(guids, sample_rate, nbits)     # get the audio signature based on the guids given in the arguments


# TODO: allow delay due to sound propagation
# TODO: take this assignment to the load_signature() function

indexEmbed=timeEmbed*sample_rate - fDelay               #Interactive Index after accounting for the delays


# TODO: perform a loop to embed all the interactions

xNormalized[indexEmbed:indexEmbed+len(signature),1]= xNormalized[indexEmbed:indexEmbed+(len(signature)),1]+signature # embed signature in channel1
xNormalized[indexEmbed:indexEmbed+len(signature),0]= xNormalized[indexEmbed:indexEmbed+(len(signature)),0]+signature # embed signature in channel0


xNormalized= np.int16( xNormalized * convert_16_bit )    # convert Audio data to 1nt16
print "3 Data type is:", xNormalized.dtype               # Confirm Audio Type ; this should int16 for wavwriting
wav.write("papa(out)Pyt.wav",sample_rate,xNormalized )    #export interactive audio

##################### Testing Cout #################

# plt.plot(xNormalized[:,1])                                     #Plots
# plt.ylabel('some numbers')
# plt.show()


# print(type(xNormalized))

# print(len(signature))
# print(len(xNormalized[indexEmbed:len(signature)+indexEmbed,1]))
#print(fDelay*len(tBit))

# print(xNormalized[1:10,1])

#
# print(max(xNormalized[:,0]))
# print(max(xNormalized[:,1]))