import random
characters = list("POIUYTREWQASDFGHJKLMNBVCXZasdfghjklpoiuytrewq,mnbvcxz0987654321)(*&^%$#@!) ")
numbers = []
[numbers.append(i) for i in range(len(characters))]
random.shuffle(numbers)
dictt = {k: v for k, v in zip(characters, numbers)}
userinput = input("enter message to decrupt:")
secretmessage = []
for i in userinput:
    if i in dictt:
        secretmessage.append(dictt[i])
    else:
        secretmessage.append(i)
def decrypt ( onetimekey ,secretmessage):
    characters = list("POIUYTREWQASDFGHJKLMNBVCXZasdfghjklpoiuytrewq,mnbvcxz0987654321)(*&^%$#@!) ")
    decrypt_dictt = {v:k for v,k in zip(onetimekey,characters)}
    message = []
    for i in secretmessage:
        if i in decrypt_dictt:
            message.append(decrypt_dictt[i])
        else:
            message.append(i)
    print("".join(message))
decrypt(numbers,secretmessage)
