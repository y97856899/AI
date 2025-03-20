import random


def dragon():
    return random.randint(55, 72)


def population(size):
    hero = []
    
    for m in range(size):
        
        heros = {
            'Speed': random.randint(1, 10),
            'Agility': random.randint(1, 10),
            'Intelligence': random.randint(1, 10),
            'Luck': random.randint(1, 10)
        }
        
        hero.append(heros)
        
    return hero



def fitnes(hero):
    a= hero['Speed'] * 1.5
    b=hero['Agility'] * 2
    c= hero['Intelligence'] * 1.2
    d= hero['Luck'] * 2.5
    
    return a + b + c + d




def update(population):
    for hero in population:
        hero['Fitness'] = fitnes(hero)






def selection(population):
    total_fitness = 0
    for hero in population:
        total_fitness += hero['Fitness']



    probabilities = []
    for hero in population:
        probabilities.append(hero['Fitness'] / total_fitness)


    return random.choices(population, weights=probabilities, k=2)







def crossover(parent1, parent2):
    child1 = parent1.copy()
    child2 = parent2.copy()
    crossover_point = random.choice(['Speed', 'Agility', 'Intelligence', 'Luck'])
    attributes = ['Speed', 'Agility', 'Intelligence', 'Luck']
    
    
    start_index = attributes.index(crossover_point)
    
    
    
    for i in range(start_index, len(attributes)):
        
        att = attributes[i]
        child1[att] = child2[att] 
        
        child2[att] = child1[att]
        
    return child1, child2






def mutate(child, rate):
    if random.random() < rate:
        
        attribute = random.choice(['Speed', 'Agility', 'Intelligence', 'Luck'])
        
        child[attribute] = random.randint(1, 10)






def evolve_population(population, strength):
    for iteration in range(50):
        
        for i in range(len(population)):
            for j in range(0, len(population) - i - 1):
                
                
                if population[j]['Fitness'] < population[j + 1]['Fitness']:
                    population[j], population[j + 1] = population[j + 1], population[j]

        
        
        if population[0]['Fitness'] > strength:
            print("Dragon has been defeated by hero !")
            return
        
        
        parents = selection(population)
        
        
        child1, child2 = crossover(parents[0], parents[1])
        
        
        mutate(child1,0.05)
        mutate(child2,0.05)
        
        
        child1['Fitness'] = fitnes(child1)
        child2['Fitness'] = fitnes(child2)
        
        
        population[-2] = child1
        population[-1] = child2

    
    print("DRAGON the victor!")


def main():
    
    strength = dragon()
    print(f"Dragon's strength: {strength}")
    
    
    population1 = population(50)
    
    
    update(population1)
    
    
    evolve_population(population1, strength)


if __name__ == "__main__":
    main()





