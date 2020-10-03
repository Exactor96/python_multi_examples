from tasks import *
from concurrent.futures import ThreadPoolExecutor
import os
from random import randint
from decos import timeit
from pickle import dump, load
import time
import sys
import argparse


URLS_LIST = ['http://google.com/favicon.ico']
# NUMBER_LIST = [randint(-10 ** 6, 10 ** 6) for i in range(5000)]
NUMBER_LIST = load(open('NUMLIST.obj', 'rb'))

TIMES = None
MAX_WORKERS = None


@timeit(supress_output=True)
def download_urls_multi():
    tpe = ThreadPoolExecutor(max_workers=MAX_WORKERS)
    results = tpe.map(url_download, URLS_LIST * TIMES)
    return results


@timeit()
def download_urls_single():
    for i in range(TIMES):
        start = time.monotonic()
        url_download(URLS_LIST[0])
        print(f'Iteration #{i} - {time.monotonic() - start} s') 


@timeit(supress_output=True)
def cpu_hard_function_multi():
    tpe = ThreadPoolExecutor(max_workers=os.cpu_count())
    results = tpe.map(cpu_hard_function, [NUMBER_LIST for i in range(TIMES)])
    result_list = []

    for result in results:
        result_list.append(result)

    return result_list


@timeit()
def cpu_hard_function_single():
    for i in range(TIMES):
        start = time.monotonic()
        cpu_hard_function(NUMBER_LIST)
        print(f'Iteration #{i} - {time.monotonic() - start} s') 


def main():
    cpu_hard_function_multi()
    cpu_hard_function_single()
    
    download_urls_multi()
    download_urls_single()


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='ThreadPoolExecutor')
    parser.add_argument('--workers', metavar='WORKERS', type=int,
                    help='set number of workers for ThreadPoolExecutor')
    parser.add_argument('--times',  metavar='TIMES', type=int,
                    help='run N times function')

    args = parser.parse_args()

    MAX_WORKERS = args.workers or os.cpu_count()
    TIMES = args.times or randint(1, 10)

    print('-' * 10, 'Start Test!', '-' * 10)
    print(f'[*] Workers: {MAX_WORKERS}')
    print(f'[*] Times: {TIMES}')
    main()
    print('-' * 10, 'End Test!', '-' * 10)
