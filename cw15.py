# cw15.py (template file)

print("Count the occurences of the word 'test' in string.")

# Expect one input from user
usr_input = input("Enter a string: ")

# Delete the following line and write your own code here
usr_input = usr_input.lower()
if ' ' in usr_input:
    answer = 0
    list1 = usr_input.split()
    for word in list1:
        if word == 'test':
            answer += 1

else:
    if 'test' in usr_input:
        usr_input = usr_input.replace('test', '')
        if len(usr_input) != 0:
            answer = 0
        else:
            answer = 1


# print the answer
print(answer)

# You can test your program
# user enter "test test Test TEST" expected output 4
# user enter "JUST A RANDOM TEST STRING" expected output 1
# user enter "123 no testing 34%%" expected output 0
