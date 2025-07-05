import threading

def th(cou):
    for i in range(50):
        print(i)

for i in range(10):
    threading.Thread(target=th, args=(0,)).start()