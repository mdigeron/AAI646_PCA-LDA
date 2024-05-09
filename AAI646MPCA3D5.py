#change based on size in problem, remeber that these are not transposed need correct orientation
# [top, middle, bottom}
import numpy as np
D1 = [[8,3,6], [7,9,10], [6,2,2], [3,9,3], [9,3,10]]
D2 = [[-2,-2,3], [5,7,-1], [3,2,-2], [1,-1,5], [1,3,-1]]
DT = D1 + D2
print("D values")
print(DT)
m = [0,0,0]
for esh in DT:
    m[0] += esh[0]
    m[1] += esh[1]
    m[2] += esh[2]
m[0] = m[0]/len(DT)
m[1] = m[1]/len(DT)
m[2] = m[2]/len(DT)
print("m value")
print(m)
xkm0 =[0,0,0]
xkm1 =[0,0,0]
xkm2 =[0,0,0]
xkm3 =[0,0,0]
xkm4 =[0,0,0]
xkm5 =[0,0,0]
xkm6 =[0,0,0]
xkm7 =[0,0,0]
xkm8 =[0,0,0]
xkm9 =[0,0,0]
xkm0[0] = DT[0][0]- m[0]
xkm0[1] = DT[0][1]- m[1]
xkm0[2] = DT[0][2]- m[2]
xkm1[0] = DT[1][0]- m[0]
xkm1[1] = DT[1][1]- m[1]
xkm1[2] = DT[1][2]- m[2]
xkm2[0] = DT[2][0]- m[0]
xkm2[1] = DT[2][1]- m[1]
xkm2[2] = DT[2][2]- m[2]
xkm3[0] = DT[3][0]- m[0]
xkm3[1] = DT[3][1]- m[1]
xkm3[2] = DT[3][2]- m[2]
xkm4[0] = DT[4][0]- m[0]
xkm4[1] = DT[4][1]- m[1]
xkm4[2] = DT[4][2]- m[2]
xkm5[0] = DT[5][0]- m[0]
xkm5[1] = DT[5][1]- m[1]
xkm5[2] = DT[5][2]- m[2]
xkm6[0] = DT[6][0]- m[0]
xkm6[1] = DT[6][1]- m[1]
xkm6[2] = DT[6][2]- m[2]
xkm7[0] = DT[7][0]- m[0]
xkm7[1] = DT[7][1]- m[1]
xkm7[2] = DT[7][2]- m[2]
xkm8[0] = DT[8][0] -m[0]
xkm8[1] = DT[8][1] -m[1]
xkm8[2] = DT[8][2]- m[2]
xkm9[0] = DT[9][0] -m[0]
xkm9[1] = DT[9][1] -m[1]
xkm9[2] = DT[9][2]- m[2]
print("(xk-m) values")
print(xkm0, xkm1, xkm2, xkm3, xkm4, xkm5, xkm6, xkm7, xkm8, xkm9, sep="\n")
print("S = [s11, s12],[s21, s22]")
aa = xkm0[0]**2 + xkm1[0]**2 + xkm2[0]**2 + xkm3[0]**2 + xkm4[0]**2 + xkm5[0]**2 + xkm6[0]**2 + xkm7[0]**2 + xkm8[0]**2 + xkm9[0]**2        
ab = xkm0[0]*xkm0[1] + xkm1[0]*xkm1[1] + xkm2[0]*xkm2[1] + xkm3[0]*xkm3[1] + xkm4[0]*xkm4[1] + xkm5[0]*xkm5[1] + xkm6[0]*xkm6[1] + xkm7[0]*xkm7[1] + xkm8[0]*xkm8[1] + xkm9[0]*xkm9[1]
ac = xkm0[0]*xkm0[2] + xkm1[0]*xkm1[2] + xkm2[0]*xkm2[2] + xkm3[0]*xkm3[2] + xkm4[0]*xkm4[2] + xkm5[0]*xkm5[2] + xkm6[0]*xkm6[2] + xkm7[0]*xkm7[2] + xkm8[0]*xkm8[2] + xkm9[0]*xkm9[2] 
bb = xkm0[1]**2 + xkm1[1]**2 + xkm2[1]**2 + xkm3[1]**2 + xkm4[1]**2 + xkm5[1]**2 + xkm6[1]**2 + xkm7[1]**2 + xkm8[1]**2 + xkm9[1]**2
bc = xkm0[1]*xkm0[2] + xkm1[1]*xkm1[2] + xkm2[1]*xkm2[2] + xkm3[1]*xkm3[2] + xkm4[1]*xkm4[2] + xkm5[1]*xkm5[2] + xkm6[1]*xkm6[2] + xkm7[1]*xkm7[2] + xkm8[1]*xkm8[2] + xkm9[1]*xkm9[2] 
cc = xkm0[2]**2 + xkm1[2]**2 + xkm2[2]**2 + xkm3[2]**2 + xkm4[2]**2 + xkm5[2]**2 + xkm6[2]**2 + xkm7[2]**2 + xkm8[2]**2 + xkm9[2]**2        
S = [[aa, ab, ac], [ab, bb, bc], [ac, bc, cc]]
print(S)
#check eigenvalues on matlab
V, D = np.linalg.eig(S)
print("V array")
print(V)
print("D array")
print(D)
e = [0,0,0]
if V[0] > V[1] and V[0] > V[2]:
    e[0] = D[0][0]
    e[1] = D[1][0]
    e[2] = D[2][0]
elif V[1] > V[0] and V[1] > V[2]:
    e[0] = D[0][1]
    e[1] = D[1][1]
    e[2] = D[2][1]
else:
    e[0] = D[0][2]
    e[1] = D[1][2]
    e[2] = D[2][2]
print("e value")
print(e)
ak0 = e[0]*xkm0[0] + e[1]*xkm0[1] + e[2]*xkm0[2]
ak1 = e[0]*xkm1[0] + e[1]*xkm1[1] + e[2]*xkm1[2]
ak2 = e[0]*xkm2[0] + e[1]*xkm2[1] + e[2]*xkm2[2]
ak3 = e[0]*xkm3[0] + e[1]*xkm3[1] + e[2]*xkm3[2]
ak4 = e[0]*xkm4[0] + e[1]*xkm4[1] + e[2]*xkm4[2]
ak5 = e[0]*xkm5[0] + e[1]*xkm5[1] + e[2]*xkm5[2]
ak6 = e[0]*xkm6[0] + e[1]*xkm6[1] + e[2]*xkm6[2]
ak7 = e[0]*xkm7[0] + e[1]*xkm7[1] + e[2]*xkm7[2]
ak8 = e[0]*xkm8[0] + e[1]*xkm8[1] + e[2]*xkm8[2]
ak9 = e[0]*xkm9[0] + e[1]*xkm9[1] + e[2]*xkm9[2]

print("ak values")
print(ak0, ak1, ak2, ak3, ak4, ak5, ak6, ak7, ak8, ak9, sep='\n')
xk0 = [0,0,0]
xk1 = [0,0,0]
xk2 = [0,0,0]
xk3 = [0,0,0]
xk4 = [0,0,0]
xk5 = [0,0,0]
xk6 = [0,0,0]
xk7 = [0,0,0]
xk8 = [0,0,0]
xk9 = [0,0,0]
xk0[0] = m[0] + ak0*e[0]
xk0[1] = m[1] + ak0*e[1]
xk0[2] = m[2] + ak0*e[2]
xk1[0] = m[0] + ak1*e[0]
xk1[1] = m[1] + ak1*e[1]
xk1[2] = m[2] + ak1*e[2]
xk2[0] = m[0] + ak2*e[0]
xk2[1] = m[1] + ak2*e[1]
xk2[2] = m[2] + ak2*e[2]
xk3[0] = m[0] + ak3*e[0]
xk3[1] = m[1] + ak3*e[1]
xk3[2] = m[2] + ak3*e[2]
xk4[0] = m[0] + ak4*e[0]
xk4[1] = m[1] + ak4*e[1]
xk4[2] = m[2] + ak4*e[2]
xk5[0] = m[0] + ak5*e[0]
xk5[1] = m[1] + ak5*e[1]
xk5[2] = m[2] + ak5*e[2]
xk6[0] = m[0] + ak6*e[0]
xk6[1] = m[1] + ak6*e[1]
xk6[2] = m[2] + ak6*e[2]
xk7[0] = m[0] + ak7*e[0]
xk7[1] = m[1] + ak7*e[1]
xk7[2] = m[2] + ak7*e[2]
xk8[0] = m[0] + ak8*e[0]
xk8[1] = m[1] + ak8*e[1]
xk8[2] = m[2] + ak8*e[2]
xk9[0] = m[0] + ak9*e[0]
xk9[1] = m[1] + ak9*e[1]
xk9[2] = m[2] + ak9*e[2]
print("x hat values")
print(xk0, xk1, xk2, xk3, xk4, xk5, xk6, xk7, xk8, xk9, sep="\n")
