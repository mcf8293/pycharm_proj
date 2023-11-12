from threading import Thread

def func(name):
    for i in range(100):
        print("子进程",i)

if __name__ == '__main__':
    t1=Thread(target=func, args=("t1",))
    t2=Thread(target=func, args=("t2",))
    t1.start()
    t2.start()