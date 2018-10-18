import dimod
from collections import Counter
from dwave.system.composites import EmbeddingComposite
from dwave.system.samplers import DWaveSampler

# Encode the mapping from the slides, from index to (N, R) value
sol_name = {0: '1: R 1', 1: '5: R 1', 2: '8: R 1', 3: '9: R 1',
            4: '1: R 2', 5: '6: R 2', 6: '8: R 2', 7: '9: R 2',
            8: '5: R 3', 9: '6: R 3', 10: '8: R 3', 11: '9: R 3',
            12: '2: R 5', 13: '6: R 5', 14: '8: R 5', 15: '9: R 5',
            16: '1: R 8', 17: '2: R 8', 18: '5: R 8', 19: '6: R 8',
            20: '1: R 9', 21: '5: R 9', 22: '6: R 9'}

# Set up the QUBO. Write out the constraints from the slides:
Q = {(0, 0): -2, (1, 1): -2, (2, 2): -2, (3, 3): -2,
     (4, 4): -2, (5, 5): -2, (6, 6): -2, (7, 7): -2,
     (8, 8): -2, (9, 9): -2, (10, 10): -2, (11, 11): -2,
     (12, 12): -2, (13, 13): -2, (14, 14): -2, (15, 15): -2,
     (16, 16): -1, (17, 17): -2, (18, 18): -3, (19, 19): -2,
     (20, 20): -2, (21, 21): -2, (22, 22): -2,
     (0, 1): 2, (0, 2): 2, (0, 3): 2, (1, 2): 2, (1, 3): 2, (2, 3): 2,
     (4, 5): 2, (4, 6): 2, (4, 7): 2, (5, 6): 2, (5, 7): 2, (6, 7): 2,
     (8, 9): 2, (8, 10): 2, (8, 11): 2, (9, 10): 2, (9, 11): 2, (10, 11): 2,
     (12, 13): 2, (12, 14): 2, (12, 15): 2, (13, 14): 2, (13, 15): 2,
     (14, 15): 2, (16, 17): 2, (16, 18): 2, (16, 19): 2, (17, 18): 2,
     (17, 19): 2, (18, 19): 2, (20, 21): 2, (20, 22): 2, (21, 22): 2,
     (0, 4): 2, (0, 18): 2, (0, 20): 2, (4, 18): 2, (4, 20): 2, (18, 20): 2,
     (12, 17): 2, (1, 8): 2, (1, 18): 2, (1, 21): 2, (8, 18): 2, (8, 21): 2,
     (18, 21): 2, (5, 9): 2, (5, 13): 2, (5, 19): 2, (5, 22): 2, (9, 13): 2,
     (9, 19): 2, (9, 22): 2, (13, 19): 2, (13, 22): 2, (19, 22): 2,
     (2, 6): 2, (2, 10): 2, (2, 14): 2, (6, 10): 2, (6, 14): 2, (10, 14): 2,
     (3, 7): 2, (3, 11): 2, (3, 15): 2, (7, 11): 2, (7, 15): 2, (11, 15): 2}

# Create BinaryQuadraticModel from the qubo matrix, and set the offset
# to zero
bqm = dimod.BinaryQuadraticModel.from_qubo(Q, offset=0.0)

# Embed onto the QPU, and run on the QPU
sampler = EmbeddingComposite(DWaveSampler())

# Obtain the response from the QPU
response = sampler.sample(bqm, num_reads=1000)

# Process and tally the results
results = Counter()
for index, answer in enumerate(response.samples_matrix):
    key = (str(answer), str(response.data_vectors['energy'][index]))
    results[key] += 1

# Loop over the results
for binary_vars, energy in results:

    # the minimum energy is known, from previous runs
    if energy == '-12.0':

        # produce a labeled line for the user
        solution = [sol_name[index] for index, m in enumerate(binary_vars[2:-2].split()) if m == '1']
        print(solution, results[(binary_vars, energy)])
