#count the number of repetaitions
#import time
#List of names
names =['Angela', 'angela', 'Cesare', 'Silvia', 'silvia', 'Angela', 'Giuseppe']
#change the names into lower case
names=[x.lower() for x in names]
print(names)
#create empty array
counter={}
#for loop
for name in names:
    #other method to change the names into lower case
    name=name.lower()
    print(name)
    if name in list(counter.keys()):
        counter[name]+=1
    else:
        counter[name]=1
print(counter)

#sorting numbers
list=[8, 5, 9, 7]
print(len(list))
for i in range(len(list)):
    #display loop i from index o to index 3 for first time and the i length will decrement in every loop i
    for j in range(len(list)-i-1):
        if list[j] > list[j+1]:
            list[j], list[j+1] = list[j+1], list[j]
    print(list)  


#sorting numbers method 2 
list=[8, 5, 9, 7]
#print(len(list))
for i in range(len(list)):
    #display loop i from index o to index 3 for first time and the i length will decrement in every loop i
    for j in range(i+1, len(list)):
        if list[i] > list[j]:
            list[i], list[j] = list[j], list[i]
    print(list)  

    #sorting numbers method 3 using sorted method 
list=[8, 5, 9, 7]
print('using sorted method')
print(sorted(list))