import dimod

# use the exact solver to find energies for all states. This is only
# realistic for very small problems.
exactsolver = dimod.ExactSolver()

# Set up the QUBO. Start with the equations from the slides:
# - red - green - blue + 2 * red * green + 2 * red * blue + 2 * blue * green
# and remember the order: (red, green, blue)
Q = {('r', 'r'): -1, ('g', 'g'): -1, ('b', 'b'): -1, ('r', 'g'): 2, ('r', 'b'): 2, ('b', 'g'): 2}

# There's no need for a constant, so we can use exactsolver directly.
results = exactsolver.sample_qubo(Q)

# print the results
for smpl, energy in results.data(['sample', 'energy']):
    print(smpl, energy)
