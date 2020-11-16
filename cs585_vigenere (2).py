#!/usr/bin/env python3.7
# --------------------------------------------------------------------------
# Encrypt, Decrypt, Crack,
# --------------------------------------------------------------------------
# Copyright (c) 2020 Bernard Avenatti and/or its affiliates.  All rights reserved.
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software 
# and associated documentation files (the "Software"), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge, publish, distribute, 
# sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is 
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all copies or 
# substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT 
# NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND 
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, 
# DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, 
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
# --------------------------------------------------------------------------
# import libraries
import re
import itertools
from enum import Enum
import freqAnalysis #!!! bja - not my code borrowed library for english frequencies under BSD

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' 

class Method:
   """Enum to describe which requirement is being exercised"""
   ENCRYPT = 1
   DECRYPT = 2
   CRACK = 3
 
def getIndexOne(x):
   """Get the Item at index position one.
   """
   return x[1]

def compute_vigenere(t, k, m):
   """Transform the supplied text and return the result.
   Args:
       text (str): The text to transform.
       key (str): The key with which to apply the transformation.
       want_decrypted (bool): Whether to encrypt (False) or decrypt (True).
   """   
   # holds the answer for t passed into compute_vigenere
   answer = ""
   tUp = t.upper()
   kUp = k.upper()
   # iterate through each character of text in t while comparing characters in SQUARE 
   for i, c in enumerate(tUp):
       # if character is not alpha skip and concatenate to answer
       if c not in alphabet:
           answer += c
       # if not matching, find matching character    
       else:
           # get the index of the character in the alphabet
           # get position based on text inbound
           tindex = alphabet.index(c)
           # get position based on key value
           kindex = alphabet.index(kUp[i % len(kUp)])
           # if m is 2 --> we are decrypting
           if m == 2:
               kindex *= -1
           # concatenate character to answer outout based on alphabet index tool position    
           answer += alphabet[(tindex + kindex) % len(alphabet)]
   return answer
 
def crack_vigenere_key(t, n):
   """Attempt to use frequncy to Crack the supplied cipher text and determine key. 
      This function is not working 100% of the time and I cannot figure out why.
      Basic Idea: 1. Get Nth letter chunk
                  2. Do freq analysis
                  3. Brute force keys 
   Args:
       t(str): Target text for encryption
       n(int): Length of key
   """
   # Determine the most likely letters for each letter in the key.
   answer = ""
   tUp = t.upper()
   # These inner lists are the scores lists.
   allScores = []
   # 1. Get Nth letter chunk
   for nth in range(1, n + 1):
      # returns every positional letter for each set of letters in key text
      # remove non-letters from the message
      tUp2 = re.compile('[^A-Z]').sub('', tUp.upper())
      i = nth - 1
      letters = []
      # while items remain to iterate
      while i < len(tUp2):
         letters.append(tUp2[i])
         i += n
      positionalLetters = ''.join(letters)
      # 2. Do freq analysis
      scores = []
      for key in alphabet:
         dt = compute_vigenere(positionalLetters, key, Method.DECRYPT)
         # using freqAnalysis library to assist
         match = (key, freqAnalysis.englishFreqMatchScore(dt))
         scores.append(match)
      # Sort by match score
      scores.sort(key=getIndexOne, reverse=True)
      allScores.append(scores[:4])
   # Try every combination of the most likely letters for each position
   # 3. Brute force keys 
   for indexes in itertools.product(range(4), repeat=n):
      # Create a possible key from the letters in allFreqScores
      key = ""
      for i in range(n):
         key += allScores[i][indexes[i]][0]
      print("Most likey key is " + key)
      break
   return None

def vigenere(t, k, m):
   """Encrypt or Decrypt the supplied text and return the result.
   Args:
       t(str): Target text for encryption
       k(str): Encryption key. Note: Use None for Crack.
       m(int): Determines what action to take on the target text. Encrypt, Decrypt, Crack
   """
   # if encrypt/decrypt call compute_vigenere
   if m == 1 or m == 2:
       return compute_vigenere(t, k, m)
   # if crack call crack_vigenere
   elif m == 3:
       # assignment says to assume period n = 3
       return crack_vigenere_key(t, 3)