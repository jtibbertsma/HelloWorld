#! /usr/bin/env python3

"""Obfuscated Hello World program in Python"""

import random
import math

MAGIC = 9001
ALPHA = 0
BETA  = 1

dick = '->'

def stringify(iter):
   s = ''
   for n in iter:
      s += chr(n)
   return s

obfusc = [
   lambda x:                         x * (3 * x) - 32,
   lambda x:            x ** (x - 21) // 5 - (x + 10),
   lambda x:                                   2 ** x,
   lambda x:                        (x * 7) % x + 101,
   lambda x:                          (x & 0xF0) + 60,
   lambda x:        ((x << 3) // x) + 10 ** len(dick),
   lambda x:                       int(math.gamma(x)),
   lambda x:   ((x % 12) * 100) // 3 + ((x >> 2) + 2),
   lambda x:                             x + (x % 18),
   lambda x:                  int(math.hypot(x, 345)),
   lambda x:                              (x - 1) * 4,
   lambda x:    (((x ^ 44) & (x ^ 33)) * x) % 182 + 1,
   lambda x:                     ((x ^ 0x3D) * 2) - 5,
   lambda x:                  int(math.hypot(x, 112)),
   lambda x:                      ((x * 3) % 4) * 108,
   lambda x:                                   x + 70,
   lambda x:                        9234432 ** x * 33,
   lambda x:                             (x << 2) + x
]

class numbers:
   range = range(len(obfusc))

   def __init__(self, obhello):
      self.ob = obhello
      self.gen = None
      self.count = None

   def inc(self):
      if self.count:
         next(self.count)

   def __iter__(self):
      self.count = iter(self.range)
      self.ob.seed()
      self.gen = self.ob()
      return self

   def __next__(self):
      while True:
         self.inc()
         value = next(self.gen) if self.gen else 0
         if value < 128:
            return value

   def __repr__(self):
      return 'numbers'

class Hello(random.Random):
   def __init__(self, x=None):
      pass

   def __iter__(self):
      return self

   def __next__(self):
      return int(math.asin(self.uniform(ALPHA, BETA)) * 180/math.pi)

   def seed(self, x=None):
      x = MAGIC if x is None else x
      super().seed(x)
      for n in range(len(obfusc)):
         self.uniform(ALPHA, BETA)

   def __call__(self, *args):
      self.ind = 0
      while True:
         try:
            yield obfusc[self.ind % len(obfusc)](next(self))
         except ZeroDivisionError:
            pass
         except ValueError:
            pass
         self.ind += 1

def main():
   print_hello = Hello()
   message = stringify(numbers(print_hello))
   print(message)
   
if __name__ == '__main__':
   main()
