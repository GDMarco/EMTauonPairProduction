import crpropa
import EMMuonPairProduction

print("My Simulation\n")

ml = crpropa.ModuleList()

ml.add(crpropa.SimplePropagation(1*crpropa.parsec, 100*crpropa.parsec))
ml.add(crpropa.MaximumTrajectoryLength(1000*crpropa.parsec))
ml.add(EMMuonPairProduction.EMMuonPairProduction())

print("+++ List of modules")
print(ml.getDescription())

print("+++ Done")
