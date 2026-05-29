import math
import random

class ExponentialGenerator:
    def __init__(self, rate):
        if rate <= 0:
            raise ValueError("Интенсивность должна быть > 0")
        self.rate = rate

    def next_time(self):
        u = random.random()
        if u == 0.0:
            u = 1e-10
        return -math.log(u) / self.rate

class MM1System:
    def __init__(self, lambda_, mu):
        if lambda_ <= 0 or mu <= 0:
            raise ValueError("Параметры lambda и mu должны быть положительными")
        self.lambda_ = lambda_
        self.mu = mu
        self.arrival_gen = ExponentialGenerator(lambda_)
        self.service_gen = ExponentialGenerator(mu)

    def simulate(self, T):
        if T <= 0:
            raise ValueError("Время моделирования T должно быть > 0")
        current_time = 0.0
        is_busy = False
        next_arrival_time = self.arrival_gen.next_time()
        next_departure_time = float('inf')
        state_time = {0: 0.0, 1: 0.0}
        arrived_count = 0
        served_count = 0
        lost_count = 0

        while current_time < T:
            if next_arrival_time < next_departure_time:
                event_time = next_arrival_time
                event_type = 'arrival'
            else:
                event_time = next_departure_time
                event_type = 'departure'

            if event_time > T:
                event_time = T

            dt = event_time - current_time
            current_state = 1 if is_busy else 0
            state_time[current_state] += dt
            current_time = event_time

            if current_time >= T:
                break

            if event_type == 'arrival':
                arrived_count += 1
                next_arrival_time = current_time + self.arrival_gen.next_time()
                if not is_busy:
                    is_busy = True
                    service_duration = self.service_gen.next_time()
                    next_departure_time = current_time + service_duration
                else:
                    lost_count += 1
            elif event_type == 'departure':
                served_count += 1
                is_busy = False
                next_departure_time = float('inf')

        distribution = {}
        for state in state_time:
            distribution[state] = state_time[state] / T

        results = {
            "distribution": distribution,
            "arrived": arrived_count,
            "served": served_count,
            "lost": lost_count,
            "loss_prob": lost_count / arrived_count if arrived_count > 0 else 0,
            "accept_prob": served_count / arrived_count if arrived_count > 0 else 0
        }
        return results
