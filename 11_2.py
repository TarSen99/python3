#!/usr/bin/env python3

__seed = 0

def initGen(seed : int):
  global __seed
  __seed = seed

def __fixSeedSize(seed : int, l : int) -> str:
  s = str(seed);
  if len(s) >= l: 
    return s[:l]
  else:
    return s.rjust(l,'0')

 
def gen():
  while True:
    global __seed
    X = __fixSeedSize(__seed, 6)
    Y = (X)[3:6] + (X)[:3];
    S = __fixSeedSize((int(X) * int(Y)), 12)
    __seed = int(S[3:9])
    yield  __seed

seed = input("Enter seed: ")
initGen(seed)
rand = gen()
for i in range(1,16):
  print(rand.__next__())
