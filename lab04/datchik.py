import random

class BaseGenerator:
    def __init__(self, b, m, seed):
        self.b = b
        self.m = m
        self.x = seed

    def rand(self):
        self.x = (self.b * self.x) % self.m
        return self.x / self.m

    def generate(self, n):
        numbers = []
        for _ in range(n):
            numbers.append(self.rand())
        return numbers


def count(numbers):
    n = len(numbers)
    mean = sum(numbers) / n
    var = 0
    for x in numbers:
        var += (x - mean) ** 2
    var = var / n
    return mean, var


def main():
    b = 2**32 + 3
    m = 2**63
    seed = b

    N = 100_000

    t_mean = 0.5
    t_var = 1.0 / 12.0

    generator = BaseGenerator(b, m, seed)
    numbers = generator.generate(N)
    mean, var = count(numbers)

    numbers_ = []
    for i in range(N):
        numbers_.append(random.random())

    mean_, var_ = count(numbers_)

    diff_mean = mean - t_mean
    diff_var = var - t_var

    diff_mean_ = mean_ - t_mean
    diff_var_ = var_ - t_var

    print("Базовый датчик")
    print(f"Среднее: {mean:.6f} (diff = {diff_mean:+.6e})")
    print(f"Дисперсия: {var:.6f} (diff = {diff_var:+.6e})")

    print()

    print("Встроенный датчик")
    print(f"Среднее: {mean_:.6f} (diff = {diff_mean_:+.6e})")
    print(f"Дисперсия: {var_:.6f} (diff = {diff_var_:+.6e})")

    print()

    print("Теоретические значения")
    print(f"Среднее: {t_mean:.6f}")
    print(f"Дисперсия: {t_var:.6f}")


if __name__ == "__main__":
    main()