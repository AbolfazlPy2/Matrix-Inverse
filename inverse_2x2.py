from numpy import *
from ast import literal_eval
def calculate():
    A = array(literal_eval(input(" : ")))
    assert shape(A) == (2, 2)
    det = (A[0,0] * A[1,1]) - (A[0,1] * A[1,0])
    if isclose(det,0):
        print("The matrix is singular and has no inverse.")
    else :
        A_ = zeros([2,2])
        D = 1 / det 

        A_[0,0] ,  A_[0,1] , A_[1,0] , A_[1,1] =A[1,1] , (A[0,1] * -1) , A[1,0] * -1 , A[0,0]


        A_1 = multiply(D , A_)
        print(A_1)