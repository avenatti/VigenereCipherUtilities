#!/usr/bin/env python3.7

from vigenere import *

# demo start

# Demo 1 - Encrypt/Decrypt 
t = "HelloWorld"
k = "PHD"
print("-------------------------------------\nDEMO 1:\ntext=" + t + " key=" + k + "\n" + "-------------------------------------")
e = vigenere(t,k,Method.ENCRYPT)
print("Encrypted to: " + e)
d = vigenere(e,k,Method.DECRYPT)
print("Decrypted to: " + d + "\n")

# Demo 2 - Encrypt/Decrypt 
t = "Programming Project 1"
k = "XDA"
print("-------------------------------------\nDEMO 2:\ntext=" + t + " key=" + k + "\n" + "-------------------------------------")
e = vigenere(t,k,Method.ENCRYPT)
print("Encrypted to: " + e)
d = vigenere(e,k,Method.DECRYPT)
print("Decrypted to: " + d+ "\n")

# Demo 3 - Crack Cipher
t = "Wiqsfxes topo tiks ju siqumf bf csicmff! Hju uofesyebt it jaoiioi oo vhf nanr. Hju rbkndqau ks ujesg io vhf qvftsuwfggd djajt, Aof tig cicis ks cgcpoioi qvktf oudmy bpd ecmq. Jit yosmbpqk ju wffgff io vhf yiofox, Jit uwfctft bfgn ujrpyn pp tig fmqos. Jit ucbtf bpd ppe tmi bte cgnfcti vhf VV, Bpd iks qcnuu hbxe cgeo easglfusma hvpg pp tig dpqr. Iks cqolu asg amn jbomff io vhf elpueu, Jit xetv hbu bfgn mgfu kn uje iclm. C ljbasf nboee Gd ju atnefr io jit dee, Cne jit umfnlz qle uodm hbu bfgn tvudm tp vhf yamn. Wiqsfxes topo tiks ju siqumf bf csicmff! Ypw sba iu’u mjpe? Pj, dfcr, J mnfy iu nopmee hankljcr!"
print("-------------------------------------\nDEMO 3:\ntext=" + t + "\n" + "-------------------------------------")
e = vigenere(t,None,Method.CRACK)

k = "ABC"
d = vigenere(t,k,Method.DECRYPT)
print("Decrypted to: " + d + "\n")

# demo end
