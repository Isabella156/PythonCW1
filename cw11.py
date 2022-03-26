# cw11.py (template file)

print("Find ASCII value of a character.")

# expect one input from user
usr_input = input("Enter a character: ")

# Delete the following line and write your own code here
if len(usr_input) != 1:
    answer = "invalid input"
else:
    answer = ord(usr_input)

# print the answer
print(answer)
