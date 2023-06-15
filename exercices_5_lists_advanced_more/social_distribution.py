population = list(map(int, input().split(", ")))
minimum_wealth = int(input())

total_wealth = sum(population)
average_wealth = total_wealth // len(population)

if minimum_wealth * len(population) > total_wealth:
    print("No equal distribution possible")
else:
    wealth_excess = sum(max(0, wealth - minimum_wealth) for wealth in population)
    wealth_deficit = sum(max(0, minimum_wealth - wealth) for wealth in population)

    while wealth_excess > 0 and wealth_deficit > 0:
        max_wealth = max(population)
        min_wealth = min(population)

        if max_wealth - minimum_wealth > minimum_wealth - min_wealth:
            population[population.index(max_wealth)] -= 1
            population[population.index(min_wealth)] += 1
            wealth_excess -= 1
            wealth_deficit -= 1
        else:
            break

    print(population)