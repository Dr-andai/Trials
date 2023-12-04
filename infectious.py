import random

# Define a class for the population
class Population:
    # Initialize the population with a given size and infection rate
    def __init__(self, size, infection_rate):
        self.size = size
        self.infection_rate = infection_rate
        self.healthy = size
        self.infected = 0
        self.recovered = 0
    
    # Method to simulate the spread of the disease in the population
    def spread_disease(self):
        # Calculate the number of new infections based on the infection rate
        new_infections = self.infection_rate * self.healthy
        # Update the number of healthy, infected, and recovered individuals
        self.healthy -= new_infections
        self.infected += new_infections
        # Calculate the number of individuals who recover
        recoveries = self.infected * random.uniform(0.1, 00.15)
        # Update the number of healthy, infected, and recovered individuals
        self.infected -= recoveries
        self.recovered += recoveries
# Initialize the population with 1000 individuals and an infection rate of 0.01
population = Population(8000, 0.01)

# Simulate the spread of the disease for 100 time steps
for i in range(50):
    population.spread_disease()

# Print the final number of healthy, infected, and recovered individuals
print("Healthy:", population.healthy)
print("Infected:", population.infected)
print("Recovered:", population.recovered)