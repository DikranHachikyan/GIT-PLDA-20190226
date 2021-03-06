#!/usr/bin/python
from functools import wraps

def convert_number(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        """Wrapper"""
        f_gen = f(*args, **kwargs)
        result = []
        for res in f_gen:
            result.insert(0,res[1])
            print(f'Digit #{res[0]} is: {res[1]}')

        return result
    return wrapper

@convert_number
def generator(num):
    """Generator"""
    for idx, x in enumerate(num):
        print ("sup")
        print ("just pushing")
        print ("cool")
        yield (str(idx+1),x)

def newFunc():
	print "Hello World!"
	
def main():
    inp = input('Type in number:')
    print('hello')
    print('\nGenerator results:')
    res = generator(inp)
    print(f'\nDecorator result:{res}')

if __name__ == "__main__":
	newFunc()
    main()
