import random

def birthday_paradox_simulation(num_people, trials=1000000):
    count_shared_birthdays = 0

    for _ in range(trials):
        birthdays = [random.randint(1, 365) for _ in range(num_people)]
        if len(birthdays) > len(set(birthdays)):
            count_shared_birthdays += 1

    return count_shared_birthdays / trials

def birthday_paradox_exact(num_people):
    if num_people > 365:
        return 1.0  

    prob_no_shared = 1.0
    for i in range(num_people):
        prob_no_shared *= (365 - i) / 365
    return 1 - prob_no_shared


if __name__ == "__main__":
    group_size = 23
    trials = 10000

    
    sim_probability = birthday_paradox_simulation(group_size, trials)
    print(f"Simulation: Probability of at least two people sharing a birthday in a group of {group_size}: {sim_probability:.4f}")

    
    exact_probability = birthday_paradox_exact(group_size)
    print(f"Exact: Probability of at least two people sharing a birthday in a group of {group_size}: {exact_probability:.4f}")
