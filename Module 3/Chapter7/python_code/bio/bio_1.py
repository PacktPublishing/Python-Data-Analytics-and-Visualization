# bio_1.py
#
import matplotlib.pyplot as plt
from phipsi import getPhiPsi
from Modelling import getStructuresFromFile
    
def genPhiPsi(fileName):
  struc = getStructuresFromFile(fileName)[0]

  phiList = []
  psiList = []
  for chain in struc.chains:
    for residue in chain.residues[1:-1]:
      phi, psi = getPhiPsi(residue)
      phiList.append(phi)
      psiList.append(psi)

  return phiList, psiList
     
if __name__ == '__main__':

  phiList = []
  psiList = []
  phiList, psiList = genPhiPsi('/Users/kvenkatr/examples/testTransform.pdb')

  phiList2 = []
  psiList2 = []
  phiList2, psiList2 = genPhiPsi('/Users/kvenkatr/examples/1A12.pdb')

  plt.figure(figsize=(12,9))
  f, (ax1, ax2) = plt.subplots(1, 2, sharey=True, figsize=(12,9))

  ax1.scatter(phiList, psiList, s=90, alpha=0.65)
  ax1.axis([-160,160,-180,180])
  ax1.set_title('Ramachandran Plot for Two Structures')
  ax2.scatter(phiList2, psiList2, s=60, alpha=0.65, color='r')
  plt.show()







