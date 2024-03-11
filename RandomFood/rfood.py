import random

restaurants = ['Juicy Bun', 'Mos Burger', 'McDonald']

meals = {
    'Juicy Bun': {'卡滋雙色起士堡': 220, '國王豬肋排大器套餐': 295, '北海小英雄魚排沙拉': 270, '就是棒雞塊': 185},
    'McDonald': {'金迎招財薯來堡(牛)': 100, '金迎招財薯來堡(鷄)': 100, '金迎招財福堡(牛)': 90},
    'Mos Burger': {'胡麻豚燒福堡': 100, '摩斯豬排堡': 65, '法式蕈菇蛋布里歐堡': 75}}

rand_rest = random.choice(restaurants)
print(rand_rest)

if rand_rest in meals:
    print(f'Menus for{rand_rest}')
    print(meals[rand_rest])
    
    print('still cant choose?(y/n) ')
    user_input = input('> ')
    if user_input == 'y':
        rand_meal = random.choice(list(meals[rand_rest].keys()))
        print(rand_meal)
    elif user_input == 'n':
        print('bye!')
    else:
        print('invalid input')