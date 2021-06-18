#palindrom

word=input("insert word ")
palindrom=True
print(word)
for i in range(0, int(len(word)/2)):
    if word[i] != word[len(word)-1-i]:
        palindrom=False
if palindrom:
       print("it is palindrom")
else:
       print("it is not")     
        