import time

print('------------------------')
print('Welcome to Caesar Cipher')
print('------------------------')
while True:
    n = input("encrypt or decrypt?(en/dt):")

    dic = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g',
           8: 'h', 9: 'i', 10: 'j', 11: 'k', 12: 'l', 13: 'm', 14: 'n',
           15: 'o', 16: 'p', 17: 'q', 18: 'r', 19: 's', 20: 't', 21: 'u',
           22: 'v', 23: 'w', 24: 'x', 25: 'y', 26: 'z'}

    def encrypt(stri):
        a = ''
        b = int(input("enter shift val:"))
        c = []
        d = stri

        for i in d:
            f = list(dic.values()).index(i) + 1
            f = (f + b) % 27
            c.append(f)
        for i in c:
            a += dic[i]
        time.sleep(3)
        print(f"encrypted text is: {a}")

    def decrypt(stri):
        a = ''
        b = int(input("enter shift val:"))
        c = []
        d = stri

        for i in d:
            f = list(dic.values()).index(i) + 1
            f = f - b
            if f < 0:
                f += 27
                f = f % 27
            else:
                f = f % 27
            c.append(f)

        for i in c:
            a += dic[i]
        time.sleep(3)
        print(f'decrypted text is: {a}')

    if n == 'en':
        e = input("enter plain text:")
        encrypt(e)
    else:
        e = input("enter text:")
        decrypt(e)

    qy = input("Do you want to work again(Y/N):")
    if qy == 'Y' or qy == 'y':
        time.sleep(3)
        pass
    else:
        time.sleep(1)
        break

print('----------')
print("Thank you!")
print('----------')
