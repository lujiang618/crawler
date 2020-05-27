# coding=utf-8

if __name__ == '__main__':
    print(eval("5+8"))

    command = "__import__('os').system('dir')"
    print(eval(command))

    print(eval("{'name':'linux','age':age}", {"age": 1822}))
