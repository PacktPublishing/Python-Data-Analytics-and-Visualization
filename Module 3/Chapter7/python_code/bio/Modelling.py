

class Structure:
  def __init__(self, name, conformation=0, pdbId=None):
    if not name:
      raise Exception('name must be set to non-empty string')
    self._name = name
    self.conformation = conformation
    self.pdbId = pdbId

    self.chains = [] # For the children

  def delete(self):
    for chain in self.chains:
      chain.delete()

  def getChain(self, code):
    for chain in self.chains:
      if chain.code == code:
        return chain

    return None

  def getPdbIds(self):
    return list(self.pdbIds)

  def getMass(self):
    if hasattr(self, 'mass'):
      # already been calculated so just return value
      return self.mass

    # not been calculated yet so do it
    mass = 0
    for chain in self.chains:
      mass += chain.getMass()
    self.mass = mass # cache for next time
    return mass

  def getName(self):
    return self._name

  def setName(self, name):
    if not name:
      raise Exception('name must be set to non-empty string')
    self._name = name

  name = property(getName, setName)


class Chain:
  allowedMolTypes = ('protein', 'DNA', 'RNA')
  
  def __init__(self, structure, code, molType='protein'):
    if not code:
      raise Exception('code must be set to non-empty string')
    if molType not in self.allowedMolTypes:
      raise Exception('molType="%s" must be one of %s' %
                      (molType, self.allowedMolTypes))

    # check that key code is not already used
    chain = structure.getChain(code)
    if chain:
      raise Exception('code="%s" already used' % code)

    self.structure = structure
    self.code = code
    self._molType = molType

    # ...
    self.resDict = {}
    self.residues = []
    structure.chains.append(self)

  def delete(self):
    for residue in self.residues:
      residue.delete()
    self.structure.chains.remove(self)

  def getResidue(self, seqId):
    return self.resDict.get(seqId)

  def getAtoms(self):
    atoms = []
    for residue in self.residues:
      atoms.extend(residue.atoms)
    return atoms
    
  def getMolType(self):
    return self._molType

  molType = property(getMolType)
 
class Residue:
  def __init__(self, chain, seqId, code=None):
    if not seqId:
      raise Exception('seqId must be set to non-empty string')
    residue = chain.getResidue(seqId)
    if residue:
      raise Exception('seqId="%s" already used' % seqId)

    self.chain = chain
    self.seqId = seqId
    self.code = code

    self.atomDict = {}
    self.atoms = []
    chain.resDict[seqId] = self
    chain.residues.append(self)

  def delete(self):
    for atom in self.atoms:
      atom.delete()
    del self.chain.resDict[self.seqId]
    self.chain.residues.remove(self)

  def getAtom(self, name):
    return self.atomDict.get(name)
  
from numpy import array

class Atom:
  def __init__(self, residue, name, coords, element):
    if not name:
      raise Exception('name must be set to non-empty string')
    atom = residue.getAtom(name)
    if atom:
      raise Exception('name="%s" already used' % name)
    if len(coords) != 3:
      raise Exception('Coordinates must contain three values')
 
    self.residue = residue
    self.name = name
    self.coords = array(coords)
    self.element = element

    residue.atomDict[name] = self
    residue.atoms.append(self)

  def delete(self):
    del self.residue.atomDict[self.name]
    self.residue.atoms.remove(self)


def getStructuresFromFile(fileName):

  fileObject = open(fileName)
  structure = None
  name = 'unknown'
  conformation = 0
  pdbId = None
  structures = []

  for line in fileObject:

    record = line[0:6].strip()
    if record == 'HEADER':
      pdbId = line.split()[-1]

    elif record == 'TITLE':
      name = line[10:].strip()

    elif record == 'MODEL':
      conformation = int(line[10:14])

    elif record == 'ENDMDL':
      structure = None

    elif record == 'ATOM':
      serial     = int(line[6:11])    # not used here
      atomName   = line[12:16].strip()
      altLocn    = line[16]           # not used here
      resName    = line[17:20].strip()
      chainCode  = line[21:22].strip()
      seqId      = int(line[22:26])
      x          = float(line[30:38])
      y          = float(line[38:46])
      z          = float(line[46:54])
      segment    = line[72:76].strip()
      element    = line[76:78].strip() 
      
      if chainCode == '':
        if segment:
          chainCode = segment
        else:
          chainCode = 'A'

      if not structure:
        structure = Structure(name, conformation, pdbId)
        structures.append(structure)

      chain = structure.getChain(chainCode)
      if not chain:
        chain = Chain(structure, chainCode)

      residue = chain.getResidue(seqId)
      if not residue:
        residue = Residue(chain, seqId, resName)
        
      if not element:
        element = name[0] # Have to guess

      coords = (x,y,z)
      atom = Atom(residue, atomName, coords, element)
    
  fileObject.close()

  return structures
  
def guessResidueMolType(residue):

  if residue.getAtom("CA") and residue.getAtom("N"):
    return 'protein'

  elif residue.getAtom("C5'") and residue.getAtom("C3'"): # DNA/RNA
    
    if residue.getAtom("02'"):
      return 'RNA'
    else:           # This is "2'-deoxy"
      return 'DNA'

  return 'other'

if __name__ == '__main__':

  testStructs = getStructuresFromFile('examples/Glycophorin.pdb')

  structure = testStructs[0]
  chain = structure.getChain('A')
  for residue in chain.residues:
    print(residue.seqId, residue.code)
    #print(guessResidueMolType(residue))
