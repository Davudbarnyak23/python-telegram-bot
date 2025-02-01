def decorator(func):
    def wrap(*args, **kwargs):
        print('start')
        func(*args, **kwargs)
        print('end')
    return wrap


@decorator
def con_pri(text=''):
    print('наша фнкція',text)


con_pri('')