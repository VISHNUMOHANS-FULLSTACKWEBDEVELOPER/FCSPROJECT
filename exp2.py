import random

def coupon_collector_simulation(num_coupons, trials=1000000):

    total_draws = 0

    for _ in range(trials):
        collected = set()
        draws = 0

        while len(collected) < num_coupons:
            coupon = random.randint(1, num_coupons)
            collected.add(coupon)
            draws += 1


        total_draws += draws

    return total_draws / trials

def coupon_collector_exact(num_coupons):
    expected_draws = 0.0
    for i in range(1, num_coupons + 1):
        expected_draws += num_coupons / i

    return expected_draws


if __name__ == "__main__":
    num_coupons = 50
    trials = 10000

    
    sim_expected_draws = coupon_collector_simulation(num_coupons, trials)
    print(f"Simulation: Expected number of draws to collect all {num_coupons} coupons: {sim_expected_draws:.2f}")

   
    exact_expected_draws = coupon_collector_exact(num_coupons)
    print(f"Exact: Expected number of draws to collect all {num_coupons} coupons: {exact_expected_draws:.2f}")
