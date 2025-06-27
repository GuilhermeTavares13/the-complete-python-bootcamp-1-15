import random
# import my_module

# print(random.randint(1,9))
# print(my_module.my_favourite_number)

# random_number_0_to_1 = random.random() * 10
# print(random_number_0_to_1)

# random_float = random.uniform(1,10)
# print(random_float)

flip_coin = random.randint(0,1)
print(flip_coin)

if flip_coin == 0:
    print("Heads")
else:
    print("Tails")