import random
import time

from helpers_task1.LRUCache import LRUCache


def range_sum_no_cache(array: list, L, R):
    return sum(array[L:R + 1])

def update_no_cache(array: list, index: int, value):
    array[index] = value

def range_sum_with_cache(array: list, L, R, cache: LRUCache):
    key = (L, R)
    if (cached_sum := cache.get(key)) is not None:
        return cached_sum
    result = sum(array[L:R + 1])
    cache.put(key, result)
    return result


def update_with_cache(array: list, index: int, value, cache: LRUCache):
    array[index] = value
    keys_to_remove = [key for key in cache.cache.keys() if key[0] <= index <= key[1]]
    for key in keys_to_remove:
        del cache.cache[key]


if __name__ == "__main__":
    N = 100_000
    Q = 50_000
    array = [random.randint(1, 1000) for _ in range(N)]
    queries = []
    for _ in range(Q):
        if random.random() < 0.7:
            L, R = sorted([random.randint(0, N - 1), random.randint(0, N - 1)])
            queries.append(('Range', L, R))
        else:
            index = random.randint(0, N - 1)
            value = random.randint(1, 1000)
            queries.append(('Update', index, value))

    cache = LRUCache(1000)

    start = time.time()
    for query in queries:
        if query[0] == 'Range':
            range_sum_no_cache(array, query[1], query[2])
    end = time.time()
    print(f'Час виконання без кешу: {end - start:.2f} секунд')

    start = time.time()
    for query in queries:
        if query[0] == 'Range':
            range_sum_with_cache(array, query[1], query[2], cache)
    end = time.time()
    print(f'Час виконання з LRU-кешем: {end - start:.2f} секунд')
