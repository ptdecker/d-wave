## ------- Set up our list of numbers -------
S = [17, 21, 19]

## ------- Set up your QUBO dictionary -------

lagrange = 20

Q = {(1, 1): (17-3*lagrange), (2, 2): (21-3*lagrange), (3, 3): (19-3*lagrange), (1, 2): 2, (1, 3): 2, (2, 3): 2}

## ------- Run our QUBO on the QPU -------
# Set up QPU parameters
chainstrength = 100
numruns = 100

# Run the QUBO on the solver from your config file
from dwave.system.samplers import DWaveSampler
from dwave.system.composites import EmbeddingComposite
response = EmbeddingComposite(DWaveSampler()).sample_qubo(Q, chain_strength=chainstrength, num_reads=numruns)

## ------- Return results to user -------
#print(response)
print(response.data)
#R = iter(response)
#E = iter(response.data)
#for line in response:
#    sample = next(R)
#    S = [boxes[i-1] for i in sample if sample[i] > 0]
#    print("Boxes: ", S, "\tSum: ", sum(S))

