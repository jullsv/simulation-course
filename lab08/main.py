import numpy as np
import math
import random

class PoissonSimulator:
    def simulate_continuous_flow(self, lambda_val, T_interval, total_time):
        events = []
        t = 0.0
        while t < total_time:
            alpha = random.random()
            dt = -math.log(alpha) / lambda_val if alpha > 0 else 0.0001
            t += dt
            if t < total_time:
                events.append(t)
        
        num_intervals = int(total_time // T_interval)
        counts = np.zeros(num_intervals, dtype=int)
        
        for ev_time in events:
            idx = int(ev_time // T_interval)
            if idx < num_intervals:
                counts[idx] += 1
                
        return counts, len(events)

    def get_statistics(self, counts):
        """Вычисление среднего и дисперсии"""
        if len(counts) == 0: return 0, 0, 0
        mean_v = np.mean(counts)
        var_v = np.var(counts)
        ratio = var_v / mean_v if mean_v > 0 else 0
        return mean_v, var_v, ratio
