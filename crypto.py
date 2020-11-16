import random
import hashlib
import time
SECRET = 'fkj0vfy9l3fhi4bi'


def get_id():
    gen_mess = str(random.random())[2:]
    gen_time = time.asctime()
    gen_hash = hashlib.sha224(bytes(gen_time + gen_mess + SECRET, 'utf8')).hexdigest()
    return str(gen_time) + '|' + gen_mess + '|' + gen_hash


def check_id(user_id: str):
    gen_time, gen_mess, gen_hash = user_id.split('|')
    curr_hash = hashlib.sha224(bytes(gen_time + gen_mess + SECRET, 'utf8')).hexdigest()
    curr_time = time.asctime()
    curr_time = time.mktime(time.strptime(curr_time))
    gen_time = time.mktime(time.strptime(gen_time))
    if curr_hash == gen_hash and int(gen_time) >= curr_time - 120:
        return 1
    else:
        return 0


while True:
    print('Введите номер операции, которую хотите совершить: '
          '\n1. Выдать новый id. '
          '\n2. Проверить действительность идентификатора')
    t = input()
    if t == '1':
        print('Новый идентификатор:\n', get_id())
    elif t == '2':
        print('Введите идентификатор')
        if check_id(input()) == 1:
            print('Идентификатор действителен')
        else:
            print('Идентификатор недействителен')
    else:
        print('Команда не найдена')
    print('Введите любую команду, чтобы продолжить')
    _ = input()
