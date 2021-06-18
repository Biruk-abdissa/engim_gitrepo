#User login and password authentication
#print(Benvenuti)
user={'biruk': 'caluso', 'biru': 'acb123'}
my_user=input('Insert username ')
while my_user not in list(user.keys()):
    print('wrong username please insert username ')
    my_user=input('Insert username ')
    print('username successful!')
password=input('Insert password {}'.format(my_user))
pwd_repitation=1
while (password != str(user[my_user]))&(pwd_repitation<3):
    print('password invalid')
    password=input('insert the coorect password ')
    pwd_repitation+=1
    print('welcome you are logged in {}'.format(pwd_repitation) )