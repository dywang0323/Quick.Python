# change the case of a string
# capitalize the first letter

name = "my lovelace"
print(name.title())

# capitalize all the letter, lowercase all letters, case conversion
name = "my lovelace"
print(name.upper())
print(name.lower())
print(name.swapcase())

# merge strings

first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
print(full_name)
print("hello, " + full_name.title() + "!")

message = "hello, " + full_name.title() + "!"
print(message)

# Tabs or newlines to add space

print("\tpython")
print("Language:\npython\nC\nJavaScript")
print("Language:\n\tPython\n\tC\n\tJavaScript")
