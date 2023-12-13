import random

coin_flip = random.randint(0, 1)

if coin_flip == 1:
  print("Heads")
elif coin_flip == 0:
  print("Tails")