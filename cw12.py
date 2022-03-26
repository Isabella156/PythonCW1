# cw12.py (template file)

print("Substitute a character with a key of 3.")

# Expect one input from user
usr_input = input("Enter a character: ")

# Delete the following line and write your own code here
if ord(usr_input) < 32 or ord(usr_input) > 126:
    print("invalid input")
else:
    value = ord(usr_input) + 3

if value > 126:
    value = (value % 127) + 32

answer = chr(value)

# print the answer
print(answer)
