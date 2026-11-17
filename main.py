import time
from urllib.request import urlopen

def main():
    url = input("Введите URL файла: ")

    total_size = 0
    total_time = 0

    # Делаем 10 последовательных запросов
    for i in range(10):
        start = time.perf_counter()

        with urlopen(url, timeout=30) as response:
            data = response.read()

        elapsed = time.perf_counter() - start

        size = len(data)
        total_size += size
        total_time += elapsed

        print(f"Запрос {i + 1}: {elapsed:.2f} сек, {size / 1024:.2f} KB")

    # Считаем среднее время и скорость скачивания
    average_time = total_time / 10
    speed = total_size * 8 / total_time / 1_000_000

    print(f"Среднее время запроса: {average_time:.2f} сек")
    print(f"Всего скачано: {total_size / 1_000_000:.2f} MB")
    print(f"Скорость скачивания: {speed:.2f} Mbps")


if __name__ == "__main__":
    main()