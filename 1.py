import random

el = ('̾', '̽', '̷', '̴', '̶', '̳', '͓')


def sys10to7(sym: str):
    """Перевод из десятичной системы в семеричную"""
    s7 = ''
    n = ord(sym) - ord('а') + 1
    while n > 0:
        s7 = str(n % 7) + s7
        n //= 7
    if len(s7) == 1:
        s7 = '0' + s7
    return s7


def sys7to10(num):
    """Перевод из семеричной системы в десятичную"""
    sym = 0
    while len(num) > 0:
        sym += int(num[0]) * (7 ** (len(num) - 1))
        num = num[1:]
    return sym


def encryption(container, mess, shift=-1):
    """Алгоритм вставки сообщения в контейнер. В параметрах: контейнер, сообщение и максимальное количество символов
     между вставками (по умолчанию вставки растягиваются на длинну контейнера). Возвращает заполненный контейнер.
     В случае, если сообщение невозможно полностью вставить в текст, возвращается строка, сигнализирующая об этом"""
    enc_mess = ''
    int_mess = ''
    if shift == -1:
        shift = len(container) // len(mess)
    mess = caesar_cipher(mess, shift)
    for x in mess:
        int_mess += sys10to7(x)
    mess = int_mess
    curr_syms = ''
    for sym in container:
        if len(mess) > 0:
            # enc_mess += sym + el[int(mess[0])]
            # mess = mess[1:]
            curr_syms += sym
        else:
            enc_mess += sym
        if len(curr_syms) == shift:
            n = random.randrange(0, shift)
            enc_mess += curr_syms[:n] + el[int(mess[0])] + curr_syms[n:]
            mess = mess[1:]
            curr_syms = ''
    if len(mess) != 0:
        return 'Insufficient length or shift is too large'
    return enc_mess


def decryption(enc_mess):
    """Алгоритм доставания сообщения из контейнера. На параметрах только заполненный контейнер, возращает вставленный
    секрет."""
    mess_int = ''
    mess = ''
    for sym in enc_mess:
        if el.count(sym) > 0:
            mess_int += str(el.index(sym))
    for i in range(0, len(mess_int), 2):
        mess += chr(sys7to10(mess_int[i:i + 2]) + ord('а') - 1)
    mess = caesar_cipher(mess, shift)
    return mess





def main():
    container = 'Привет, меня зовут боб! Если такой текст растянуть на очень большие предложения, то такие вставки "почти" незаметны'
    mess = 'тайна'
    enc_mess = encryption(container, mess)
    print(enc_mess)
    dec_mess = decryption(enc_mess)
    print(dec_mess)


if __name__ == '__main__':
    main()
