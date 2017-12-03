
f = open('repo.txt', 'r')
temp = f.read()
f.close()

temp2 = ""
for char in temp:
    if (char != "?"):
        temp2 = temp2 + char
        

f = open('repo.txt', 'w')
f.write(temp2)
f.close() 