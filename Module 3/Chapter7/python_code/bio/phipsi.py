# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 11:38:58 2015

@author: kvenkatr
"""
from numpy import zeros
from Maths import calcTorsionAngle
from math import degrees

Atomic_numbers = {'H':1, 'C':12, 'N':14, 'O':16, 'P':31, 'S':32}

def getCenterOfMass(structure):

  centerOfMass = zeros(3, float)
  totalMass = 0.0

  for chain in structure.chains:
    for residue in chain.residues:
      for atom in residue.atoms:
        mass = Atomic_numbers.get(atom.element, 12.0)
        centerOfMass += mass * atom.coords
        totalMass += mass
  
  centerOfMass /= totalMass

  return centerOfMass


def getPhiPsi(residue, inDegrees=True):

  phi = 0
  psi = 0

  rchain = residue.chain
  cresidues = rchain.residues

  atomN  = residue.getAtom('N')
  atomCa = residue.getAtom('CA')
  atomC  = residue.getAtom('C')
  
  coordsN  = atomN.coords
  coordsCa = atomCa.coords
  coordsC  = atomC.coords

  index = cresidues.index(residue)
  
  if index > 0:

    residuePrev = cresidues[index-1]
    
    atomCprev = residuePrev.getAtom('C')
    coordsCprev  = atomCprev.coords
    
    phi = calcTorsionAngle(coordsCprev, coordsN, coordsCa, coordsC)
    
    if inDegrees:
      phi = degrees(phi)
    
  if index < ( len(cresidues)-1 ):
    residueNext = cresidues[index+1]
    
    atomNext = residueNext.getAtom('N')
    coordsNext  = atomNext.coords
  
    psi = calcTorsionAngle(coordsN, coordsCa, coordsC, coordsNext)
    
    if inDegrees:
      psi = degrees(psi)
  
  return phi, psi
