import neal
sampler = neal.SimulatedAnnealingSampler()
for kwarg in sorted(sampler.parameters):
    print(kwarg)
print(sampler.properties['beta_shedule_options'])
