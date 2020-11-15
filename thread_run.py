import argparse
import os
import time
from concurrent.futures import ThreadPoolExecutor
from random import randint

from decos import timeit
from tasks import collect_all_hrefs, make_random_image

URLS_LIST = [
    'http://facebook.com/',
    'http://yandex.ru/',
    'http://vk.com/',
    'http://wikipedia.org/'
]

TIMES = None
MAX_WORKERS = None


@timeit(supress_output=True)
def collect_hrefs_urls_multi():
    tpe = ThreadPoolExecutor(max_workers=MAX_WORKERS)
    results = tpe.map(collect_all_hrefs, URLS_LIST)
    return [result for result in results]


@timeit()
def collect_hrefs_urls_single():
    for i in range(len(URLS_LIST)):
        start = time.monotonic()
        collect_all_hrefs(URLS_LIST[i])
        duration = time.monotonic() - start
        print(f'Iteration #{i} - {duration} s')


@timeit(supress_output=True)
def make_random_image_multi():
    tpe = ThreadPoolExecutor(max_workers=os.cpu_count())
    results = tpe.map(lambda local_args: make_random_image(*local_args), [(1000, 1000, str(i+1)) for i in range(TIMES)])
    result_list = []
    for result in results:
        result_list.append(result)

    return result_list


@timeit()
def make_random_image_single():
    for i in range(TIMES):
        start = time.monotonic()
        make_random_image(1000, 1000, str(i))
        print(f'Iteration #{i} - {time.monotonic() - start} s') 


def main():
    make_random_image_multi()
    make_random_image_single()
    
    collect_hrefs_urls_multi()
    collect_hrefs_urls_single()


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='ThreadPoolExecutor')
    parser.add_argument('--workers', metavar='WORKERS', type=int,
                    help='set number of workers for ThreadPoolExecutor')
    parser.add_argument('--times',  metavar='TIMES', type=int,
                    help='run N times for generate image function')

    args = parser.parse_args()

    MAX_WORKERS = args.workers or os.cpu_count()
    TIMES = args.times or randint(1, 10)

    print('-' * 10, 'Start Test!', '-' * 10)
    print(f'[*] Workers: {MAX_WORKERS}')
    print(f'[*] Times: {TIMES}', '\n')
    main()
    print('-' * 10, 'End Test!', '-' * 10)
