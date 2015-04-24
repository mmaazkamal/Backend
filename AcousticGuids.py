"""Helper functions for working with audio files in NumPy."""

import numpy as np
import contextlib




def load_signature(guids,sample_rate,nbits):

    amp,ampS, t= .49,.49,.05                   #Variable handels for Bits
    tBit = np.arange(0,t*sample_rate+1)/float(sample_rate)  #time Vector for Bits
    F0,F1,Fsync = 19600, 19300, 19900                       #Bits Carrier Frequency


    y0=amp*np.cos(2*np.pi*F0*tBit)                          #Bit0
    winB=np.hanning(len(y0))                                #Applying Windows
    y0=y0*winB

    y1=amp*np.cos(2*np.pi*F1*tBit)                          #Bit1
    y1=y1*winB                                              #Applying Windows

    ysync=ampS*np.cos(2*np.pi*Fsync*tBit)                   #Bit for Synchronization
    winS=np.hanning(len(ysync))                             #Applying Windows
    ysync=ysync*winS

    ySilence=amp*np.sin(2*np.pi*0*tBit)                     #Adding Silence in between all bits



    y0=np.concatenate([ySilence,y0,ySilence,ysync])         #Bit0 coupled with silence and Sync
    y1=np.concatenate([ySilence,y1,ySilence,ysync])         #Bit1 coupled with silence and Sync


    guids1=guids[0]                                         #First available guid
    signature=ysync                                         #Declare and place Sync
    for g in guids1:                                        #Complete Concatenated Signature
        if g=='0':                                          # concatenate Bit0
            signature=np.concatenate([signature,y0])
        else:                                               # concatenate Bit1
            signature=np.concatenate([signature,y1])

    return signature