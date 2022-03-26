# cw13.py (template file)

print("Generate grade from marks.")

# Expect one input from user
usr_input = input("Enter the marks: ")

# Delete the following line and write your own code here
marks = int(usr_input)

if marks < 0 or marks > 100:
    print("invalid input")
elif marks < 50:
    answer = 'F'
elif marks < 60:
    answer = 'D'
elif marks < 70:
    answer = 'C'
elif marks < 80:
    answer = 'B'
else:
    answer = 'A'

# print the answer
print(answer)
