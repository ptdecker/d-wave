import neal
sampler = neal.SimulatedAnnealingSampler()
h = {'a': 0.0, 'b': 0.0, 'c': 0.0}
J = {('a', 'b'): 1.0, ('b', 'c'): 1.0, ('a', 'c'): 1.0}
response = sampler.sample_ising(h, J)
for index, answer in enumerate(response.samples_matrix):
    print(str(answer), str(response.data_vectors['energy'][index]))
