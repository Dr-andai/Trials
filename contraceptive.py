#-- Population of women in an area
#-- Simulate the use of contraceptive in the population

# variables to consider
#-- population
#-- method

# example
#-- population X, consists of non-gravid women
#-- over a period of time, based on fertility rate we expect a certain chnage id demoghraphy
#-- contraceptive method, will be influencing fertility

####
# create characteristics for this population
# Population
# 1 = size
# 2 = fertility rate
# 3 = contraceptive uptake rate
# 4 = contraceptive non-uptake

# Method
# 1 = uptake
# 2 = reuptake



import random
# Define a class for the population
class Population:
    # Initialize the population with a given size and fertility rate
    def __init__(self, size, fertility_rate):
        self.size = size
        self.fertility_rate = fertility_rate
        self.no_contraceptive = size
        self.contraceptive = 0
        self.fertile = 0

    # Method to simulate the fertility in the population
    def fertility(self):
        # Calculate the number of new infections based on the infection rate
        new_fertility = self.fertility_rate * self.no_contraceptive
        # Update the number of healthy, infected, and recovered individuals
        self.no_contraceptive -= new_fertility
        self.fertile += new_fertility
        # Calculate the number of individuals who recover
        recoveries = self.fertile * random.uniform(0.1, 00.15)
        # Update the number of healthy, infected, and recovered individuals
        self.contraceptive -= recoveries
        self.fertile += recoveries
# Initialize the population with 1000 individuals and an infection rate of 0.01
population = Population(8000, 0.01)

# Simulate the spread of the disease for 100 time steps
for i in range(50):
    population.fertility()

# Print the final number of healthy, infected, and recovered individuals
print("Healthy:", population.contraceptive)
print("Infected:", population.fertile)
print("Recovered:", population.no_contraceptive)
        