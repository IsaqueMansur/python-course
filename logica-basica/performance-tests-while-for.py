import threading
from datetime import datetime

dateNowFor = None
dateNowWhile = None

def for_loop():
    global dateNowFor
    for n in range(1, 1000):
        dateNowFor = datetime.now()
        print('from FOR:', n)

def while_loop():
    global dateNowWhile
    m = 0
    while m < 1000:
        dateNowWhile = datetime.now()
        print('from WHILE:', m)
        m += 1

thread2 = threading.Thread(target=while_loop)
thread1 = threading.Thread(target=for_loop)

thread2.start()
thread1.start()

thread2.join()
thread1.join()

print('\r\n for  :', dateNowFor)
print('\r\n while:', dateNowWhile, '\r\n')
print('For vence: ' + str(dateNowFor < dateNowWhile))