import os

if __name__ == '__main__':
    filename = f'test\\'
    title = "hello"
    if not os.path.exists(filename):
        os.mkdir(filename)
    file_path = os.path.join(filename, title)

    with open(file_path+'.txt' , 'w', encoding='utf8') as f:
        f.write("abcddefdfsf")
