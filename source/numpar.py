## ------- Set up our list of numbers -------
S = [25, 7, 13, 31, 42, 17, 21, 10]

## ------- Set up your QUBO dictionary -------

C = sum(S)
Q = {}
for i in range(len(S)):
    Q[(i,i)] =  -4 * C * S[i] + 4 * S[i] * S[i]
    for j in range(i+1, len(S)):
        Q[(i,j)] = 8 * S[i] * S[j]

## ------- Run our QUBO on the QPU -------
# Set up QPU parameters
chainstrength = 31248
numruns = 10

# Run the QUBO on the solver from your config file
from dwave.system.samplers import DWaveSampler
from dwave.system.composites import EmbeddingComposite
response = EmbeddingComposite(DWaveSampler()).sample_qubo(Q, chain_strength=chainstrength, num_reads=numruns)

## ------- Return results to user -------
R = iter(response)
E = iter(response.data())
for line in response:
    sample = next(R)
    S1 = [S[i] for i in sample if sample[i] > 0]
    S0 = [S[i] for i in sample if sample[i] < 1]
    print("S0 Sum: ", sum(S0), "\tS1 Sum: ", sum(S1), "\t", S0)
