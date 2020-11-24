import math
import time

def factorize(n):
  start = time.time()
  for p in range(2, int(math.sqrt(n))):
    if n % p == 0:
      end = time.time()
      q = int(n / p);
      print("Results: p =", p, "and q =", q)
      print("Time elapsed:", end - start, "seconds")
      return

def main():
  print("Select two prime numbers p and q")
  p = int(input("p: "))
  q = int(input("q: "))
  n = p * q
  print("n = p * q =", n)
  print("The factorization of n has started...")
  factorize(n)

main();