
print("Hi, having an access token for this repo [Starting the branch `learn`]...\n")
"""
#########################################################################
#########################################################################
"""

""" Variables In Python"""
first_name = "koorosh"
last_name = "sadeghi tehran"
age = 44

print("-----------------------------------------------------------------")
print("Variables We Use:\n\t"
      "First Name:", first_name,
      "\n\tLast Name:", last_name)
print("\n")


print("-----------------------------------------------------------------")
""" Check Variable Data Type In Python """
print("First Name's variable type is:\n\t", type(first_name))
print("Last Name's variable type is:\n\t", type(last_name))
print("Age's variable type is:\n\t", type(age))
print("\n")


print("-----------------------------------------------------------------")
""" Concatenating string variable with number ones """
message = first_name +" "+ last_name + "'s age is:\n\t" + str(age)
print(message)
print("\n")


""" Multiple Assignments In Python """
# First Way:
first_name, last_name, age = "koorosh", "sadeghi tehran", 44
# Second Way:
prince_1 = prince_2 = prince_3 = prince_4 = 177


print("-----------------------------------------------------------------")
""" Builtin String Functions: String's length """
print("Here are the different string variables' lengths:")
print("\tFirst Name's Length: " + str(len(first_name)))
print("\tLast Name's Length: " + str(len(last_name)))
print("\n")


print("-----------------------------------------------------------------")
""" Builtin String Functions: variable.title() """
print("title() function for both first name and last_name ",
      "variables:\n\t" + first_name.title() + " " +
      last_name.title())
print("\n")


print("-----------------------------------------------------------------")
""" Builtin String Functions: variable.upper() """
print("upper() function for both first name and last_name ",
      "variables:\n\t" + first_name.upper() + " " +
      last_name.upper())
print("\n")


print("-----------------------------------------------------------------")
""" Builtin String Functions: variable.lower() """
print("lower() function for both first name and last_name ",
      "variables:\n\t" + first_name.lower() + " " +
      last_name.lower())
print("\n")


print("-----------------------------------------------------------------")
""" Builtin String Functions: variable.find() """
print("find() function for both first name and last_name ",
      "variables:\n\t" + str(first_name.find("k")) + " " +
      str(last_name.find("t")))
print("\n")


print("-----------------------------------------------------------------")
""" Builtin String Functions: variable.isdigit() """
name_1 = "Barcelona"
name_2 = "2675874"
print("name_1.isdigit():", name_1.isdigit())
print("name_2.isdigit():", name_2.isdigit())
print("\n")


