def nb_year(p0, percent, aug, p):
    n = 0
    while p >= p0:
        p0 = p0 + p0 * (percent / 100) + aug
        n = n + 1
    return n


number_years = nb_year(1000, 2, 50, 1200)
print(number_years)