import crpropa
import EMMuonPairProduction

print("My Simulation\n")

ml = crpropa.ModuleList()

cmb = crpropa.CMB()

ml.add(crpropa.SimplePropagation(1*crpropa.parsec, 1000*crpropa.parsec))
ml.add(crpropa.MaximumTrajectoryLength(1000*crpropa.parsec))
ml.add(EMMuonPairProduction.EMMuonPairProduction(cmb))

print("+++ List of modules")
print(ml.getDescription())

print("+++ Done")
