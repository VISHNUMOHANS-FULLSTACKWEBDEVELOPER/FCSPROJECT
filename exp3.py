import math
import random

def hatcheck_exact(n):
    
   
    return math.factorial(n) * sum((-1)**k / math.factorial(k) for k in range(n + 1)) / math.factorial(n)

def hatcheck_simulation(n, trials=1000000):
    
    deranged_count = 0

    for _ in range(trials):
        hats = list(range(n))  
        random.shuffle(hats) 

        
        if all(hats[i] != i for i in range(n)):
            deranged_count += 1

    return deranged_count / trials


if __name__ == "__main__":
    n = 10  
    trials = 10000

    
    exact_probability = hatcheck_exact(n)
    print(f"Exact: Probability of no one getting their own hat with {n} people: {exact_probability:.4f}")

    
    sim_probability = hatcheck_simulation(n, trials)
    print(f"Simulation: Probability of no one getting their own hat with {n} people: {sim_probability:.4f}")
