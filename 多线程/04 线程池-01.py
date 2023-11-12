"""
线程池：
一次性开辟一些线程，用户直接给线程池提交任务，线程任务的调度交给线程池完成
"""
from concurrent.futures import ThreadPoolExecutor

def fn(args):
    for i in range(500):
        print(args,i)

if __name__ == '__main__':
    # 创建线程池
    with ThreadPoolExecutor(50) as t:
        for i in range(100):
            t.submit(fn, args=f"线程{i}")
    # 等待线程池中的任务全部执行完毕，才继续执行（守护）
    print("123")