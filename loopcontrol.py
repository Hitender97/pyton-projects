#loop control statements = change a loops execution from its normal sequence
#break = used to terminate the loops entirely
#continue = skips to the next iteration of the loops
#pass = does nothing, acts as a placeholder

while True:
    name = input("Enter your name:")
    if name != "":
        break
print(name)

phone_number="123-4567-345"
for i in phone_number:
    if i == "-":
        continue
    print(i,end="")

for i in range(1,21):
    if i == 13:
        pass
    else:
        print("\n",i)
