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
  flag = False
  print("Bye.")


available_choices = ["1", "2", "3"]
flag = True
while flag:
  choice = input("Choose your option:\n\t1. Add\n\t2. Read\n\t3. Quit\n>>> ")

  if choice in available_choices:
    match choice:
      case "3":
        ender()
        break
      case "1":
        add()
        continue
      case "2":
        practice()
        continue
  else:
    print("No valid choice entered. Try again...")
