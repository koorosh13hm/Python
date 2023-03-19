import json

database_file = {}

def add():
  word = input("Enter the word:\n\t--> ")
  description = input("Enter the description2:\n\t--> ")
  grammair = input("Enter the grammaire:\n\t--> ")
  example = input("Enter the example:\n\t--> ")


def practice():
  print("Practiced..")


def ender():
  print("Bye.")

flag = True
while flag:
  choice = input("Choose your option:\n\t1. Add\n\t2. Read\n\t3. Quit\n>>> ")
  if choice == str(3):
    flag = False
    ender()
    continue
  elif choice == str(1):
    add()
  else:
    practice()
