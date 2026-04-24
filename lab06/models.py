import math
from gen import BaseGenerator

class DiscreteValues:
    def __init__(self, val, prob, generator=None):
        self.val = list(val)
        self.prob = list(prob)
        self.generator = generator if generator else BaseGenerator()
        self.normalize()
        
        self.theo_mean = sum(v * p for v, p in zip(self.val, self.prob))
        self.theo_var = sum((v ** 2) * p for v, p in zip(self.val, self.prob)) - self.theo_mean ** 2

    def normalize(self):
        total_sum = sum(self.prob)
        if total_sum <= 0:
            raise ValueError("Sum of probabilities must be positive")
        self.prob = [p / total_sum for p in self.prob]

    def generate(self):
        A = self.generator.next_double()
        k = 0
        
        while True:
            A = A - self.prob[k]
            if A <= 0:
                return self.val[k]
            k = k + 1

    def experiment(self, N):
        counts = [0] * len(self.val)
        val_to_idx = {v: i for i, v in enumerate(self.val)}
        for _ in range(N):
            x = self.generate()
            counts[val_to_idx[x]] += 1
        return counts


class Calculate:
    def __init__(self, counts, N, val, prob):
        self.counts = counts
        self.N = N
        self.val = val
        self.prob = prob

    def empirical_prob(self):
        return [n / self.N for n in self.counts]

    def mean(self):
        return sum(v * p for v, p in zip(self.val, self.prob))

    def var(self, mean_val=None):
        if mean_val is None:
            mean_val = self.mean()
        e_x2 = sum((v ** 2) * p for v, p in zip(self.val, self.prob))
        return e_x2 - mean_val ** 2

    def emp_mean(self):
        p_emp = self.empirical_prob()
        return sum(v * p for v, p in zip(self.val, p_emp))

    def emp_var(self, emp_m=None):
        if emp_m is None:
            emp_m = self.emp_mean()
        p_emp = self.empirical_prob()
        e_x2 = sum((v ** 2) * p for v, p in zip(self.val, p_emp))
        return e_x2 - emp_m ** 2

    def relative_error(self, theor, emp):
        if abs(theor) < 1e-9:
            return 0.0
        return abs(emp - theor) / abs(theor)

    def chi_kvadrat(self):
        chi = 0.0
        for i in range(len(self.counts)):
            expected = self.N * self.prob[i]
            if expected > 0:
                chi += ((self.counts[i] - expected) ** 2) / expected
        return chi

    def check_chi(self, chi):
        chi_crit = 9.488 
    
        if chi > chi_crit:
            return "H0 отвергнута", chi_crit
        else:
           return "H0 принята", chi_crit


class NormalRandomVariable:
    def __init__(self, mu, sigma, generator=None):
        self.mu = mu
        self.sigma = sigma
        self.generator = generator if generator else BaseGenerator()

    def generate_box_muller(self, N):
        samples = []
        count_needed = N
        while count_needed > 0:
            u1 = self.generator.next_double()
            u2 = self.generator.next_double()
            if u1 == 0:
                u1 = 1e-10
            z0 = math.sqrt(-2.0 * math.log(u1)) * math.cos(2.0 * math.pi * u2)
            z1 = math.sqrt(-2.0 * math.log(u1)) * math.sin(2.0 * math.pi * u2)
            samples.append(self.mu + self.sigma * z0)
            count_needed -= 1
            if count_needed > 0:
                samples.append(self.mu + self.sigma * z1)
                count_needed -= 1
        return samples[:N]

    def normal_cdf(self, x):
        z = (x - self.mu) / (self.sigma * math.sqrt(2))
        return 0.5 * (1 + math.erf(z))

    def chi_kvadrat_continuous(self, samples, n_bins=10):
        N = len(samples)
        if N == 0:
            return 0.0
            
        lower = self.mu - 4 * self.sigma
        upper = self.mu + 4 * self.sigma
        step = (upper - lower) / n_bins
        
        observed = [0] * n_bins
        for x in samples:
            if x < lower:
                observed[0] += 1
            elif x >= upper:
                observed[-1] += 1
            else:
                idx = int((x - lower) / step)
                if idx >= n_bins:
                    idx = n_bins - 1
                observed[idx] += 1
        
        chi = 0.0
        for i in range(n_bins):
            x_left = lower + i * step
            x_right = x_left + step
            p_theo = self.normal_cdf(x_right) - self.normal_cdf(x_left)
            expected = N * p_theo
            
            if expected > 0:
                chi += ((observed[i] - expected) ** 2) / expected
                
        return chi
