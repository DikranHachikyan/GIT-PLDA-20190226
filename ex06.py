#!/usr/bin/python
from functools import wraps

def convert_number(f):
    @wraps(f)
    def w(*args, **kwargs):
        """Wrapper"""
        result = []
        f_gen = f(*args, **kwargs)
        for res in f_gen:
            print('c')
            result.insert(0,res[1])
            print(f'Digit #{res[0]} is: {res[1]}')
        return result
    return w

@convert_number
def generator(num):
    """Generator"""
    for idx, x in enumerate(num):
        print ("awdaw")
        yield (str(idx+1),x)

def main():
    inp = input('Type in number:')
    print('hello')
    print('\nGenerator results:')
    res = generator(inp)
    print(f'\nDecorator result:{res}')

if __name__ == "__main__":
    main()
