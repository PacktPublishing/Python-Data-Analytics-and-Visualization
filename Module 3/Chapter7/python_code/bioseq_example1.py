from Bio.Seq import Seq 
from Bio.Alphabet import IUPAC 
from Bio.SeqUtils import GC 

def DNACodons(seq):
    end = len(seq) - (len(seq)%3 -1)
    codons = [seq[i:i+3] for i in range(0, end,3)]    
    return codons 
    
my_seq = Seq('GGTCGATGGGCCTAGCAGCATATCTGAGC', IUPAC.unambiguous_dna) 
print "GC Result==>", GC(my_seq)  

DNACodons(my_seq)


