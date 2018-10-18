import dimod
  
# use the exact solver to find energies for all states. This is only
# realistic for very small problems.
exactsolver = dimod.ExactSolver()

# Set up the QUBO. Start with the equations from the slides:
# - red - green - blue + 2 * red * green + 2 * red * blue + 2 * blue * green
# and remember the order: (red, green, blue)
Q = {('x1', 'x1'): 14, ('x2', 'x2'): 18, ('x3', 'x3'): 16, ('x1', 'x2'): 2, ('x1', 'x3'): 2, ('x2', 'x3'): 2}

# There's no need for a constant, so we can use exactsolver directly.
results = exactsolver.sample_qubo(Q)

# print the results
for smpl, energy in results.data(['sample', 'energy']):
    print(smpl, energy)

