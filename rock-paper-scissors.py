import random
choices=['سنگ','کاغذ','قيچي']
computer_choice=random.choice(choices)
user_choice=str(input('سنگ کاغذ قيچي؟:'))
c='اره'
while c=='اره':
    if computer_choice==user_choice:
        print(computer_choice)
        print('مساوي')
        c=str(input('مي خواي دوباره بازي کنيم؟'))
        if c=='اره':
            computer_choice=random.choice(choices)
            user_choice=str(input('سنگ کاغذ قيچي؟:'))
            continue
        else:
            print('باشه بازيه خوبي بود')
            break
    elif (user_choice=='سنگ' and computer_choice=='قيچي') or (user_choice=='قيچي' and computer_choice=='کاغذ') or (user_choice=='کاغذ' and computer_choice=='سنگ'):
        print(computer_choice)
        print('تو بردي!')
        c=str(input('مي خواي دوباره بازي کنيم؟'))
        if c=='اره':
            computer_choice=random.choice(choices)
            user_choice=str(input('سنگ کاغذ قيچي؟:'))
            continue
        else:
            print('باشه بازيه خوبي بود')
            break
    elif (user_choice=='قيچي' and computer_choice=='سنگ') or (user_choice=='کاغذ' and computer_choice=='قيچي') or (user_choice=='سنگ' and computer_choice=='کاغذ'):
        print(computer_choice)
        print('من بردم!')
        c=str(input('مي خواي دوباره بازي کنيم؟'))
        if c=='اره':
            computer_choice=random.choice(choices)
            user_choice=str(input('سنگ کاغذ قيچي؟:'))
            continue
        else:
            print('باشه بازيه خوبي بود')
            break
    
