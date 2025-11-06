def approximate_pi(n_terms):
    pi = 0
    for i in range(n_terms):
        pi += 4 * (((-1)**i) / (2*i + 1))
        print(pi)
        i += 1
    return pi

approximate_pi(10)  # Output: ~3.0418396189
approximate_pi(100)  # Output: ~3.1315929036
approximate_pi(1000)  # Output: ~3.1405926538
