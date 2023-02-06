import socket


def xor(a, b):
    # ініціалізувати результат
    result = []

    # Перейти до всіх бітів, якщо
    #  біти однакові, тоді XOR дорівнює 0, інакше 1
    for i in range(1, len(b)):
        if a[i] == b[i]:
            result.append('0')
        else:
            result.append('1')

    return ''.join(result)


# Виконує ділення по модулю-2
def mod2div(dividend, divisor):
    # Кількість бітів, які потрібно перексорити за раз.
    pick = len(divisor)

    # Нарізка дивідендів відповідно
    # до довжини для конкретного кроку
    tmp = dividend[0: pick]

    while pick < len(dividend):

        if tmp[0] == '1':

            # замінити ділене результатом
            # для XOR і потягніть 1 біт вниз
            tmp = xor(divisor, tmp) + dividend[pick]

        else:  # якщо крайній лівий біт "0"

            # Якщо крайній лівий біт дивіденду (або
            # частина, яка використовується на кожному кроці) дорівнює 0, крок не може
            # використовувати звичайний дільник; нам потрібно використовувати an
            # дільник усіх нулів.
            tmp = xor('0' * pick, tmp) + dividend[pick]

        # збільшити вибір, щоб рухатися далі
        pick += 1

    # Для останніх n бітів ми повинні виконати це
    # зазвичай, оскільки збільшення значення вибору спричинить
    # Індекс поза межами.
    if tmp[0] == '1':
        tmp = xor(divisor, tmp)
    else:
        tmp = xor('0' * pick, tmp)

    checkword = tmp
    return checkword


# Функція, яка використовується на стороні відправника для кодування
# даних шляхом додавання залишку модульного поділу
# в кінці даних.
def encodeData(data, key):
    l_key = len(key)

    # Додає n-1 нулі в кінці даних
    appended_data = data + '0' * (l_key - 1)
    remainder = mod2div(appended_data, key)

    # Додайте залишок у вихідні дані
    codeword = data + remainder
    return codeword


# Створіть об'єкт socket
s = socket.socket()

# Визначте порт, до якого ви хочете підключитися
port = 12345

# підключитися до сервера на локальному комп’ютері
s.connect(('127.0.0.1', port))

# Надіслати дані на сервер "Hello world"

## s.sendall('Hello World')

input_string = input("Enter data you want to send->")
# s.sendall(input_string)
data = (''.join(format(ord(x), 'b') for x in input_string))
print("Entered data in binary format :", data)
key = "1001"

ans = encodeData(data, key)
print("Encoded data to be sent to server in binary format :", ans)
s.sendto(ans.encode(), ('127.0.0.1', 12345))

# отримувати дані з сервера
print("Received feedback from server :", s.recv(1024).decode())

# закрити з'єднання
s.close()
