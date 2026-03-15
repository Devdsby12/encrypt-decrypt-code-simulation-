import random
albhbet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',' ']
counting = []
for i in range(len(albhbet)):
    counting.append(i)
random.shuffle(counting)
# print(counting)
dictt ={}
for key ,value in zip( counting ,albhbet):
    dictt[value] = key
# print(dictt)
user_input = input("Enter message to encrupt : ")
new_user_input = list(user_input)
# print(new_user_input)
encruptmessage = []
for i in new_user_input:
    encruptmessage.append(dictt[i])
temp_output = []
for i in encruptmessage:
    temp_output.append(str(i))
print("","-".join(temp_output))

def decrupt (message , key):
    global albhbet
    decrupt_dict = {}
    for keyy ,value in zip(key,albhbet):
        decrupt_dict[keyy] = value
    # print(decrupt_dict)
    normal_text_message = []
    for i in message:
        normal_text_message.append(decrupt_dict[i])
    # print(normal_text_message)
    finall = "".join(normal_text_message)
    print(finall)
decrupt(encruptmessage ,counting)


