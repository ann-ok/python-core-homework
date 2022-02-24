import time

from ex2 import fetcher

CALL_COUNT = 10


def benchmark(num):
    """
    Совершает num прогонов переданной функции и выводит в консоль время каждого прогона и среднее время всех прогонов

    :param num: число итераций
    :return: функцию обёртку
    """

    def wrapper(func):
        def wrapped(*args, **kwargs):
            times = 0

            for _ in range(num):
                start = time.time()
                func(*args, **kwargs)
                end = time.time()
                i_time = end - start
                print(i_time)
                times += i_time

            print(times / num)

        return wrapped

    return wrapper


@benchmark(CALL_COUNT)
def fetch_page(url):
    fetcher.get(url)
