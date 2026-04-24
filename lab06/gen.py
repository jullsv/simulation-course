class BaseGenerator:
    def __init__(self, seed: int = 1):
        self.M = 9223372036854775808 
        self.Beta = 4294967299
        
        if seed % 2 == 0:
            seed += 1
        self.x = seed

    def next_double(self) -> float:
        self.x = (self.Beta * self.x) % self.M
        return self.x / self.M

    def reset(self, seed: int = 1):
        if seed % 2 == 0:
            seed += 1
        self.x = seed
