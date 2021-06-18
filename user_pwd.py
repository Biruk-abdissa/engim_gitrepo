#User login and password authentication

users ={"biruk": "caluso", "biru" : "acb123"}

insert_user = input("Insert username  :")

while insert_user not in list(users.keys()):

    print('wrong username please insert username ')
    users= input('Insert username please')
    print('username successful!')

password=input('Insert password {}  :'.format(insert_user))
repetations=1
while (password != str(users[insert_user]))&(repetations<3):

    print('password invalid')
    password= input('insert the coorect password :')
    #if ()
print('welcome you are logged in {}'.format(insert_user))