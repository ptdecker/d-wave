import dimod
sampler = dimod.SimulatedAnnealingSampler()
Q = {(0, 0): 1, (1, 1): 1, (0, 1): -2}
response = sampler.sample_qubo(Q)
for index, answer in enumerate(response.samples_matrix):
    print(str(answer), str(response.data_vectors['energy'][index]))
