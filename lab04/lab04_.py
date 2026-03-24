import random


class BasicGenerator:
    def __init__(self, betta, m, seed):
        self.betta = betta
        self.m = m
        self.x = seed

    def rand(self):
        self.x = (self.betta * self.x) % self.m
        return self.x / self.m

    def generate(self, n):
        numbers = []
        for _ in range(n):
            numbers.append(self.rand())
        return numbers


def calculate(numbers):
    n = len(numbers)

    mean = sum(numbers) / n

    var = 0
    for x in numbers:
        var += (x - mean) ** 2
    var = var / n

    return mean, var


def main():
    betta = 16807
    m = 2**32
    seed = 1

    N = 100_000

    theor_mean = 0.5
    theor_var = 1.0 / 12.0

    # --- Базовый минимум ---
    generator = BasicGenerator(betta, m, seed)
    numbers = generator.generate(N)
    mean, var = calculate(numbers)

    # --- Встроенный генератор ---
    numbers_ = []

    for i in range(N):
        numbers_.append(random.random())

    mean_, var_ = calculate(numbers_)

    diff_mean = mean - theor_mean
    diff_var = var - theor_var

    diff_mean_ = mean_ - theor_mean
    diff_var_ = var_ - theor_var

    # --- Вывод ---
    print("Базовый датчик")
    print(f"Среднее: {mean:.6f} (diff = {diff_mean:+.6e})")
    print(f"Дисперсия: {var:.6f} (diff = {diff_var:+.6e})")

    print()

    print("Встроенный генератор")
    print(f"Среднее: {mean_:.6f} (diff = {diff_mean_:+.6e})")
    print(f"Дисперсия: {var_:.6f} (diff = {diff_var_:+.6e})")

    print()

    print("Теоретические значения")
    print(f"Среднее: {theor_mean:.6f}")
    print(f"Дисперсия: {theor_var:.6f}")


if __name__ == "__main__":
    main()
