def determinant(A):
  """takes a 2D matrix as a list of atleast size 2x2"""
  if len(A) == 2 and len(A[0]) == 2:
    return A[0][0]*A[1][1] - A[0][1]*A[1][0] 
  else:
    terms = []
    for i in range(len(A[0])):
      terms += [((-1)**i)*A[0][i]*determinant(get_sub_matrix(A, i))]
    return sum(terms)
    
def get_sub_matrix(A, i):
  B = [[r[c] for c in range(len(r)) if c != i] for r in A[1:]]
  return B
