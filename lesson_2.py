from random import choice


symbols = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
password_leng = int(input('Введите длину пароля:'))
password = ''
for i in range(password_leng):
    password += choice(symbols)
print(f"Ваш пароль {password}")