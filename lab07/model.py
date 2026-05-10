import math
import random
import csv
import numpy as np


class MarkovWeatherGenerator:
    def __init__(self, Q, start_state=1):
        self.Q = Q
        self.start_state = start_state
        self.states = [1, 2, 3]

    def generate_next(self, state):
        i = state - 1
        rate = -self.Q[i][i]

        if rate <= 0:
            return state, float("inf")

        tau = -math.log(random.random()) / rate

        probs = []
        next_states = []

        for j in range(3):
            if j != i:
                probs.append(self.Q[i][j] / rate)
                next_states.append(j + 1)

        A = random.random()
        for k in range(len(probs)):
            A -= probs[k]
            if A <= 0:
                return next_states[k], tau

        return next_states[-1], tau

    def experiment(self, T):
        t = 0
        state = self.start_state

        times = [0]
        states = [state]
        durations = [0.0, 0.0, 0.0]

        while t < T:
            new_state, tau = self.generate_next(state)

            if t + tau > T:
                durations[state - 1] += T - t
                break

            durations[state - 1] += tau
            t += tau
            state = new_state

            times.append(t)
            states.append(state)

        return times, states, durations


class MarkovWeatherCalculate:
    def __init__(self, Q):
        self.Q = np.array(Q, dtype=float)

    def empirical_distribution(self, durations):
        total = sum(durations)
        if total == 0:
            return [0.0, 0.0, 0.0]
        return [d / total for d in durations]

    def stationary_distribution(self):
        A = self.Q.T.copy()
        b = np.zeros(3)
        A[2] = np.ones(3)
        b[2] = 1
        pi = np.linalg.solve(A, b)
        return pi.tolist()

    def relative_error(self, theor, emp):
        if theor == 0:
            return 0
        return abs(emp - theor) / abs(theor)

    def stats_text(self, durations):
        emp = self.empirical_distribution(durations)
        theor = self.stationary_distribution()
        names = ["Ясно", "Облачно", "Пасмурно"]

        text = "Статистическая обработка:\n\n"
        text += "Состояние        Время      P эмп.      P теор.     Ошибка\n"

        for i in range(3):
            err = self.relative_error(theor[i], emp[i])
            text += f"{names[i]:12s} {durations[i]:8.3f}   {emp[i]:8.4f}   {theor[i]:8.4f}   {err:8.4f}\n"

        return text, emp, theor

    def export_to_csv(self, durations, filename="markov_weather_result.csv"):
        emp = self.empirical_distribution(durations)
        theor = self.stationary_distribution()
        names = ["Ясно", "Облачно", "Пасмурно"]

        with open(filename, 'w', newline='', encoding='utf-8-sig') as f:
            writer = csv.writer(f)
            writer.writerow(["Состояние", "Время пребывания", "P эмпирическое", "P теоретическое", "Относительная ошибка"])
            for i in range(3):
                err = self.relative_error(theor[i], emp[i])
                writer.writerow([names[i], durations[i], emp[i], theor[i], err])

            writer.writerow([])
            writer.writerow(["Матрица интенсивностей Q"])
            for row in self.Q:
                writer.writerow(row.tolist())
