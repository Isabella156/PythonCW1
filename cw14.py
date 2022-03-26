# cw14.py (template file)

print("Encrypt a string with a key of 7.")

# Expect one input from user
usr_input = input("Enter a string: ")

# Delete the following line and write your own code here
index = 0
answer = ''
while index < len(usr_input):
    value = ord(usr_input[index])
    value += 7
    if value < 32 or value > 126:
        value = (value % 127) + 32

    answer += chr(value)

    index += 1

# Print the answer
print(answer)
# You can test your program
# user enter "abcde" expected output "hijkl"
# user enter "Testing!" expected output "[lz{pun("
# user enter "aBc@XyZ" expected output "hIjG_!a"
# user enter "Hello World:)" expected output "Olssv'^vyskA0"
