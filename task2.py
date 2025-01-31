import timeit
import functools
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

from helpers_task2.SplayTree import SplayTree


# Реалізація LRU-кешу
@functools.lru_cache(maxsize=None)
def fibonacci_lru(n):
    if n <= 1:
        return n
    return fibonacci_lru(n - 1) + fibonacci_lru(n - 2)

def fibonacci_splay(n, tree):
    if n <= 1:
        return n
    cached = tree.find(n)
    if cached is not None:
        return cached
    value = fibonacci_splay(n - 1, tree) + fibonacci_splay(n - 2, tree)
    tree.insert(n, value)
    return value


if __name__ == "__main__":
    values = list(range(0, 951, 50))
    lru_times = []
    splay_times = []

    for n in values:
        # Вимірюємо час для LRU Cache
        lru_time = timeit.timeit(lambda: fibonacci_lru(n), number=3) / 3
        lru_times.append(lru_time)

        # Вимірюємо час для Splay Tree
        tree = SplayTree()
        splay_time = timeit.timeit(lambda: fibonacci_splay(n, tree), number=3) / 3
        splay_times.append(splay_time)

    # Виведення таблиці результатів
    print(f"{'n':<10}{'LRU Cache Time (s)':<20}{'Splay Tree Time (s)':<20}")
    print("-" * 50)
    for n, lru, splay in zip(values, lru_times, splay_times):
        print(f"{n:<10}{lru:<20.10f}{splay:<20.10f}")

    # Побудова графіка
    plt.plot(values, lru_times, label="LRU Cache", marker="o")
    plt.plot(values, splay_times, label="Splay Tree", marker="s")
    plt.xlabel("Число n")
    plt.title("Порівняння LRU Cache і Splay Tree для обчислення чисел Фібоначчі")
    plt.gca().yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f"{x * 1e4:.1f}"))
    plt.ylabel("Час виконання (×10⁻⁴ с)")
    plt.legend()
    plt.grid()
    plt.show()