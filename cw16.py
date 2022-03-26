# cw16.py (template file)
print("Print sublists of a list.")

# Expect one input from user
usr_input = input("Enter a list: ")

# Delete the following line and write your own code here
usr_input = usr_input.replace('[', '')
usr_input = usr_input.replace(']', '')
usr_input = usr_input.replace('\"', '\'')
usr_input = usr_input.replace('‘', '\'')
usr_input = usr_input.replace('’', '\'')
usr_input = usr_input.replace(' ', '')
usr_input = usr_input.replace('\'', '')
usr_input = usr_input.replace('“', '')
usr_input = usr_input.replace('”', '')

original_list = usr_input.split(',')

result = []
index = 0
for i in original_list:
    if ((ord(i)) <= 57) and ((ord(i)) >= 48):
        original_list[index] = int(original_list[index])
    index += 1

index = 0
while len(original_list) != 0:
    count = original_list.count(original_list[0])
    new = original_list[0]
    while count != 0:
        result.append([])
        result[index].append(new)
        count -= 1
        original_list.remove(new)
    index += 1

none_number = result.count([])
while none_number != 0:
    result.remove([])
    none_number -= 1

answer = result
print(answer)

# You can test your program
# user enter "[2, 1, 2, 1]" expected output [[2, 2], [1, 1]]
# user enter "[5, 4, 5, 5, 4, 3]" expected output [[5, 5, 5], [4, 4], [3]]
# user enter "[2,1,2,1]" expected output [[2, 2], [1, 1]]
