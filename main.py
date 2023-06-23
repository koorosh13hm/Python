print("Hello, Python...")
# -----------------------------------------------

name = input("Enter Name: ")
print(f"Welcome, {name}.")

age = input("Enter Age: ")
print(f"{name}'s age number type:", type(age))
print(':', age)
age_float = float(age)
print(f"{name}'s age number type after conversion:", type(age_float))
print(':', age_float)

age_int = int(age_float)
print(f"{name}'s age number type after conversion:", type(age_int))
print(':', age_int)