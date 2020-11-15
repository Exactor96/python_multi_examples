import time


class timeit(object):

    def __init__(self, supress_output=False):
        self.supress_output = supress_output

    def __call__(self, func):
        def wrapper(*args, **kw):
            start = time.monotonic()
            print('-' * 10, func.__name__.upper(), 'START', '-' * 10)
            if self.supress_output:
                func(*args, **kw)
                result = 'Your output suppressed'
            else:
                result = func(*args, **kw)
            print(f'Duration: {time.monotonic() - start} s')
            print('-' * 10, func.__name__.upper(), 'END', '-' * 10, '\n')
            return result

        return wrapper
