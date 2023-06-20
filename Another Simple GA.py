# Genetic Algorithms

import random
from random import randint

TARGET = 200

# create suggest solution according to length value and min & max
def individual(length, min, max):
    return [ randint(min, max) for x in range(length) ]

def population(count, length, min, max):
    return [ individual(length, min, max) for x in range(count) ]

def fitness(individual):
    total = sum(individual)
    return abs(TARGET - total)

def grade(pop, target):
    # total fitness for whole population
    total_pop = [fitness(x) for x in pop]
    return sum(total_pop) / len((pop))

def mutation(parents, mutate):
    mutation_length = int(len(parents)*mutate)
    for _ in range(mutation_length):
        individual = random.choice(parents)
        pos_to_mutate = randint(0, len(individual[1])-1)
        individual[1][pos_to_mutate] = randint(min(individual[1]), max(individual[1]))
        x = fitness(individual[1])
        individual[0] = x
        return parents

def crossover(parents, desired_length):
    parents_length = len(parents)
    children = []
    while len(children) < desired_length:
        indxmale = randint(0, parents_length-1)
        indxfemale = randint(0, parents_length-1)
        if indxmale != indxfemale:
            male = parents[indxmale]
            female = parents[indxfemale]
            half = round(len(male[1]) / 2)
            child = male[1][:half] + female[1][half:]
            children.append([fitness(child), child])
    return children

def TournamentSelection(population, tournament_size):
    new_offspring = []
    for _ in range(len(population)):
        candidates = [random.choice(population) for _ in range(tournament_size)]
        new_offspring.append(min(candidates, key = lambda ind: ind[0]))
    return new_offspring

def GeneticAlgorithm(pop, target, retain = 0.2, mutate = 0.01):
    generation = 0
    found = False
    population = [ [fitness(x), x] for x in pop]
    population = sorted(population, key = lambda x: x[0])
    while(population[0][0] > 0):
        ######
        # population = [ x[1] for x in sorted(population)]
        retrain_length = int(len(population)*retain)
        # selection by Tournament selection
        new_generation = TournamentSelection(population[:retrain_length], 3)
        # crossover parents to create children
        desired_length = len(population) - len(new_generation)
        new_generation.extend(crossover(new_generation, desired_length))
        # mutate some individuals
        new_generation = mutation(new_generation, mutate)

        population = new_generation
        population = sorted(population, key = lambda x: x[0])
        print("Generation: {}\tString: {}\tFitness: {}".\
            format(generation,
            "".join(str(population[0][1])),
            str(population[0][0])))

        generation += 1

    print("Generation: {}\tString: {}\tFitness: {}".\
            format(generation,
            "".join(str(population[0][1])),
            str(population[0][0])))

GeneticAlgorithm(population(100, 5, 0, 100), 200)