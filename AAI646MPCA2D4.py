#change based on size in problem, remeber that these are not transposed need correct orientation
# [top, bottom}
import numpy as np
D1 = [[1,2], [-3,-1], [4,5], [-1,1]]
D2 = [[0,-2], [5,2], [-1,-4], [3,1]]
DT = D1 + D2
print("D values")
print(DT)
m = [0,0]
for esh in DT:
    m[0] += esh[0]
    m[1] += esh[1]
m[0] = m[0]/len(DT)
m[1] = m[1]/len(DT)
print("m value")
print(m)
xkm0 =[0,0]
xkm1 =[0,0]
xkm2 =[0,0]
xkm3 =[0,0]
xkm4 =[0,0]
xkm5 =[0,0]
xkm6 =[0,0]
xkm7 =[0,0]
xkm0[0] = DT[0][0]- m[0]
xkm0[1] = DT[0][1]- m[1]
xkm1[0] = DT[1][0]- m[0]
xkm1[1] = DT[1][1]- m[1]
xkm2[0] = DT[2][0]- m[0]
xkm2[1] = DT[2][1]- m[1]
xkm3[0] = DT[3][0]- m[0]
xkm3[1] = DT[3][1]- m[1]
xkm4[0] = DT[4][0]- m[0]
xkm4[1] = DT[4][1]- m[1]
xkm5[0] = DT[5][0]- m[0]
xkm5[1] = DT[5][1]- m[1]
xkm6[0] = DT[6][0]- m[0]
xkm6[1] = DT[6][1]- m[1]
xkm7[0] = DT[7][0]- m[0]
xkm7[1] = DT[7][1]- m[1]
print("(xk-m) values")
print(str(xkm0) + " " + str(xkm1) + " " + str(xkm2) + " " + str(xkm3) + " " + str(xkm4) + " " + str(xkm5) + " " + str(xkm6) + " " + str(xkm7))
print("S = [s11, s12],[s21, s22]")
aa = xkm0[0]**2 + xkm1[0]**2 + xkm2[0]**2 + xkm3[0]**2 + xkm4[0]**2 + xkm5[0]**2 + xkm6[0]**2 + xkm7[0]**2       
ab = xkm0[0]*xkm0[1] + xkm1[0]*xkm1[1] + xkm2[0]*xkm2[1] + xkm3[0]*xkm3[1] + xkm4[0]*xkm4[1] + xkm5[0]*xkm5[1] + xkm6[0]*xkm6[1] + xkm7[0]*xkm7[1]
bb = xkm0[1]**2 + xkm1[1]**2 + xkm2[1]**2 + xkm3[1]**2 + xkm4[1]**2 + xkm5[1]**2 + xkm6[1]**2 + xkm7[1]**2
S = [[aa, ab], [ab, bb]]
print(S)
#check eigenvalues on matlab
V, D = np.linalg.eig(S)
print("V array")
print(V)
print("D array")
print(D)
e = [0,0]
if V[0] > V[1]:
    e[0] = D[0][0]
    e[1] = D[1][0]
else:
    e[0] = D[0][1]
    e[1] = D[1][1]
print("e value")
print(e)
ak0 = e[0]*xkm0[0] + e[1]*xkm0[1]
ak1 = e[0]*xkm1[0] + e[1]*xkm1[1]
ak2 = e[0]*xkm2[0] + e[1]*xkm2[1]
ak3 = e[0]*xkm3[0] + e[1]*xkm3[1]
ak4 = e[0]*xkm4[0] + e[1]*xkm4[1]
ak5 = e[0]*xkm5[0] + e[1]*xkm5[1]
ak6 = e[0]*xkm6[0] + e[1]*xkm6[1]
ak7 = e[0]*xkm7[0] + e[1]*xkm7[1]
print("ak values")
print(ak0, ak1, ak2, ak3, ak4, ak5, ak6, ak7)
xk0 = [0,0]
xk1 = [0,0]
xk2 = [0,0]
xk3 = [0,0]
xk4 = [0,0]
xk5 = [0,0]
xk6 = [0,0]
xk7 = [0,0]
xk0[0] = m[0] + ak0*e[0]
xk0[1] = m[1] + ak0*e[1]
xk1[0] = m[0] + ak1*e[0]
xk1[1] = m[1] + ak1*e[1]
xk2[0] = m[0] + ak2*e[0]
xk2[1] = m[1] + ak2*e[1]
xk3[0] = m[0] + ak3*e[0]
xk3[1] = m[1] + ak3*e[1]
xk4[0] = m[0] + ak4*e[0]
xk4[1] = m[1] + ak4*e[1]
xk5[0] = m[0] + ak5*e[0]
xk5[1] = m[1] + ak5*e[1]
xk6[0] = m[0] + ak6*e[0]
xk6[1] = m[1] + ak6*e[1]
xk7[0] = m[0] + ak7*e[0]
xk7[1] = m[1] + ak7*e[1]
print("x hat values")
print(xk0, xk1, xk2, xk3, xk4, xk5, xk6, xk7)
