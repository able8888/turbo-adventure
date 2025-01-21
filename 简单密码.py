word=input()
new_word=''
for i in word:
    if "A"<= i <='Z':
        new_i=ord(i)-5
        if new_i < 65:
            new_i +=26
            new_word+=chr(new_i)
        else:
            new_word += chr(new_i)
    else:
        new_word+=i
print(new_word)

