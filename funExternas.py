from time import *

def printSlow(texto, atraso=0.04):
  for c in texto:
    print(c,end='',flush=True)
    sleep(atraso)
  print(' ')
