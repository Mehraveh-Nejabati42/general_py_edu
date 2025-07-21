import random
x=['🦢','🦜','🕊']
y=['🦢','🦜','🕊']
z=['🦢','🦜','🕊']
a=str(input('start?:'))
while a=='yes' or a=='yeah' or a=='ok' or a==' 'or a=='yes!':
    
    x1=random.choice(x)
    y1=random.choice(y)
    z1=random.choice(z)
    print(x1,y1,z1)
    if x1==y1==z1:
        print('jackpot!')
        a='no'
        a=str(input('do u want to play again?:'))
        if a=='no':
            print('✯🙂‍ok!good game🙂‍✯')
            break
    else:
        print('try again')
        a=str(input('do u want to try again?:'))


