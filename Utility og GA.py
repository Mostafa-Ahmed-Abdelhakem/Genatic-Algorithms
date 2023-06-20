# import required libraries
import random
from typing import Dict

def RouletteWheelSelection(population):
    max = sum([pop for pop in population])
    pick = random.uniform(0, max)
    current = 0
    for key, value in population.items():
        current += value
        if current > pick:
            return key

def TournamentSelection(population, tournament_size):
    new_offspring = []
    for _ in range(len(population)):
        candidates = [random.choice(population) for _ in range(tournament_size)]
        new_offspring.append(max(candidates, key = lambda ind: ind.fitness))
    return new_offspring

# run program
population = {0:1, 1:2, 2:3, 3:4, 4:5, 5:6}
print('Before:\n', population)
RouletteWheelSelection(population)