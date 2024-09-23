phrase="hello world!"
translation=""
for i in phrase:
    if i in "AEIOUaeiou":
        print(translation + "g")
    else:
        print(translation + i) 
        
def translate(sentence):
    trans=""
    for letter in sentence:
        if letter.lower() in "aeiou":
            if letter.isupper():
                trans=trans + "G"
            else:
                trans=trans + "g"
        else:
            trans = trans + letter
    return trans

print(translate(input("Enter the phrase: ")))

a=("" + "g")
print(a)
print(len(a))
