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

class Server:
    def __init__(self, id):
        self.id = id
        self.is_busy = False
        self.finish_time = float('inf')

    def start_service(self, current_time, service_duration):
        self.is_busy = True
        self.finish_time = current_time + service_duration

    def finish_service(self):
        self.is_busy = False
        self.finish_time = float('inf')

class Queue:
    def __init__(self, max_size):
        self.max_size = max_size
        self.current_size = 0

    def add(self):
        if self.current_size < self.max_size:
            self.current_size += 1
            return True
        return False

    def remove(self):
        if self.current_size > 0:
            self.current_size -= 1

    def is_full(self):
        return self.current_size >= self.max_size

    def is_empty(self):
        return self.current_size == 0

class MMNMSystem:
    def __init__(self, lambda_, mu, n_servers, queue_size):
        if lambda_ <= 0 or mu <= 0:
            raise ValueError("Интенсивности должны быть положительными")
        if n_servers <= 0:
            raise ValueError("Число серверов должно быть > 0")
        
        self.lambda_ = lambda_
        self.mu = mu
        self.n_servers = n_servers
        self.queue_size = queue_size
        
        self.arrival_gen = ExponentialGenerator(lambda_)
        self.service_gen = ExponentialGenerator(mu)
        
        self.servers = [Server(i) for i in range(n_servers)]
        self.queue = Queue(queue_size)

    def _get_free_server(self):
        for server in self.servers:
            if not server.is_busy:
                return server
        return None

    def _get_earliest_finish_server(self):
        earliest_server = None
        min_time = float('inf')
        for server in self.servers:
            if server.is_busy and server.finish_time < min_time:
                min_time = server.finish_time
                earliest_server = server
        return earliest_server

    def simulate(self, T):
        if T <= 0:
            raise ValueError("Время моделирования T должно быть > 0")

        current_time = 0.0
        next_arrival_time = self.arrival_gen.next_time()
        
        # Статистика
        state_time = {}
        arrived_count = 0
        served_count = 0
        lost_count = 0
        
        max_possible_state = self.n_servers + self.queue_size
        for i in range(max_possible_state + 1):
            state_time[i] = 0.0

        while current_time < T:
            event_time = next_arrival_time
            event_type = 'arrival'
            
            earliest_server = self._get_earliest_finish_server()
            if earliest_server and earliest_server.finish_time < event_time:
                event_time = earliest_server.finish_time
                event_type = 'departure'
                departing_server = earliest_server

            if event_time > T:
                event_time = T

            dt = event_time - current_time
            
      
            busy_servers = sum(1 for s in self.servers if s.is_busy)
            current_state = busy_servers + self.queue.current_size
            
            if current_state in state_time:
                state_time[current_state] += dt
            else:
                state_time[current_state] = dt 

            current_time = event_time

            if current_time >= T:
                break

            if event_type == 'arrival':
                arrived_count += 1
                next_arrival_time = current_time + self.arrival_gen.next_time()

                free_server = self._get_free_server()
                if free_server:
                    service_duration = self.service_gen.next_time()
                    free_server.start_service(current_time, service_duration)
                elif not self.queue.is_full():
                    self.queue.add()
                else:
                    lost_count += 1

            elif event_type == 'departure':
                departing_server.finish_service()
                served_count += 1

                if not self.queue.is_empty():
                    self.queue.remove()
                    service_duration = self.service_gen.next_time()
                    departing_server.start_service(current_time, service_duration)

        distribution = {}
        for state, time_spent in state_time.items():
            if time_spent > 0:
                distribution[state] = time_spent / T

        results = {
            "distribution": distribution,
            "arrived": arrived_count,
            "served": served_count,
            "lost": lost_count,
            "loss_prob": lost_count / arrived_count if arrived_count > 0 else 0,
            "avg_queue_len": sum(s * q for s, q in enumerate([0]*self.n_servers + list(range(1, self.queue_size+1))))
        }
        
        return results
