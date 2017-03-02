import scipy.sparse as sparse

matrixA = sparse.lil_matrix((6,6))

matrixA = sparse.lil_matrix( [[0,25,26,0,0,0], [0,0,85,5,10,0],
   [26,85,0,0,0,10], [0,0,0,0,0,11],[0,0,0,9,0,88],[0,0,0,11,88,0]])
print matrixA   

