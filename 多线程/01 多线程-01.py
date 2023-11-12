from threading import Thread

def func():
    for i in range(100):
        print("func",i)
if __name__ == "__main__":
    t=Thread(target=func) # 创建线程
    t.start() #多线程状态为可以开始工作状态，具体执行世间由cpu决定
    for i in range(100):
        print("main",i)