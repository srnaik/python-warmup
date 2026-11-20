print('Hello World')
print('*' * 10)
x = 1


# \ is an escape character
course = "Python \"Programming"
print(len(course))
print(course[0:3])
print(course[0])
print(course[-1])
print(course[:])
message = """
Hello World, 
This is my Python code!!
"""

first = "Sachin"
last = "Naik"

# f stands for formatted string, this expression gets evaluated at run-time.
full_name = f"{first} {last}"
print(full_name.title())
# It returns a new string object
print(full_name.upper())
print(full_name)
print(full_name.find('Naik'))
replaced_name = full_name.replace('Naik', 'NAIK')
print(f"replaced name {replaced_name}")
print(full_name)
print('Naik' in full_name)
print('Hello' not in full_name)