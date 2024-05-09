#change based on size in problem, remeber that these are not transposed need correct orientation
# [top, bottom}
import numpy as np
D1 = [[0,-1], [3,-2], [0,2], [-2,1], [2,-1]]
D2 = [[6,0], [3,2], [9,1], [7,4], [5,5]]
print("D values")
print(D1, D2, sep ="\n")
m1 = [0,0]
m2 = [0,0]
for esh in D1:
    m1[0] += esh[0]
    m1[1] += esh[1]
for esh in D2:
    m2[0] += esh[0]
    m2[1] += esh[1]
m1[0] = m1[0]/len(D1)
m1[1] = m1[1]/len(D1)
m2[0] = m2[0]/len(D2)
m2[1] = m2[1]/len(D2)
print("m values")
print(m1, m2, sep="\n")
xkm0 =[0,0]
xkm1 =[0,0]
xkm2 =[0,0]
xkm3 =[0,0]
xkm4 =[0,0]
xkm5 =[0,0]
xkm6 =[0,0]
xkm7 =[0,0]
xkm8 =[0,0]
xkm9 =[0,0]
xkm0[0] = D1[0][0]- m1[0]
xkm0[1] = D1[0][1]- m1[1]
xkm1[0] = D1[1][0]- m1[0]
xkm1[1] = D1[1][1]- m1[1]
xkm2[0] = D1[2][0]- m1[0]
xkm2[1] = D1[2][1]- m1[1]
xkm3[0] = D1[3][0]- m1[0]
xkm3[1] = D1[3][1]- m1[1]
xkm4[0] = D1[4][0]- m1[0]
xkm4[1] = D1[4][1]- m1[1]
xkm5[0] = D2[0][0]- m2[0]
xkm5[1] = D2[0][1]- m2[1]
xkm6[0] = D2[1][0]- m2[0]
xkm6[1] = D2[1][1]- m2[1]
xkm7[0] = D2[2][0]- m2[0]
xkm7[1] = D2[2][1]- m2[1]
xkm8[0] = D2[3][0] -m2[0]
xkm8[1] = D2[3][1] -m2[1]
xkm9[0] = D2[4][0] -m2[0]
xkm9[1] = D2[4][1] -m2[1]
print("(xk-m) values")
print(xkm0, xkm1, xkm2, xkm3, xkm4, xkm5, xkm6, xkm7, xkm8, xkm9, sep="\n")
print("S = [s11, s12],[s21, s22]")
aa1 = xkm0[0]**2 + xkm1[0]**2 + xkm2[0]**2 + xkm3[0]**2 + xkm4[0]**2 
ab1 = xkm0[0]*xkm0[1] + xkm1[0]*xkm1[1] + xkm2[0]*xkm2[1] + xkm3[0]*xkm3[1] + xkm4[0]*xkm4[1] 
bb1 = xkm0[1]**2 + xkm1[1]**2 + xkm2[1]**2 + xkm3[1]**2 + xkm4[1]**2
aa2 = xkm5[0]**2 + xkm6[0]**2 + xkm7[0]**2 + xkm8[0]**2 + xkm9[0]**2        
ab2 = xkm5[0]*xkm5[1] + xkm6[0]*xkm6[1] + xkm7[0]*xkm7[1] + xkm8[0]*xkm8[1] + xkm9[0]*xkm9[1]
bb2 = xkm5[1]**2 + xkm6[1]**2 + xkm7[1]**2 + xkm8[1]**2 + xkm9[1]**2
S1 = [[aa1, ab1], [ab1, bb1]]
S2 = [[aa2, ab2], [ab2, bb2]]
print(S1, S2, sep="\n")
S = [[0, 0], [0, 0]]
for esh1 in range(2):
    for esh2 in range(2):
        S[esh1][esh2] = S1[esh1][esh2] + S2[esh1][esh2]
print("S", S, sep='\n')
Si = np.linalg.inv(np.array(S))
print("S^-1", Si, sep='\n')
w = np.matmul(Si, (np.array(m1) - np.array(m2)))
print("w", w, sep='\n')
yk0 = w[0]*D1[0][0] + w[1]*D1[0][1]
yk1 = w[0]*D1[1][0] + w[1]*D1[1][1]  
yk2 = w[0]*D1[2][0] + w[1]*D1[2][1]
yk3 = w[0]*D1[3][0] + w[1]*D1[3][1]
yk4 = w[0]*D1[4][0] + w[1]*D1[4][1] 
yk5 = w[0]*D2[0][0] + w[1]*D2[0][1]
yk6 = w[0]*D2[1][0] + w[1]*D2[1][1]
yk7 = w[0]*D2[2][0] + w[1]*D2[2][1]
yk8 = w[0]*D2[3][0] + w[1]*D2[3][1]
yk9 = w[0]*D2[4][0] + w[1]*D2[4][1]
print("yk values")
print(yk0,yk1,yk2,yk3,yk4,yk5,yk6,yk7,yk8,yk9, sep="\n")
xk0 = [0,0]
xk1 = [0,0]
xk2 = [0,0]
xk3 = [0,0]
xk4 = [0,0]
xk5 = [0,0]
xk6 = [0,0]
xk7 = [0,0]
xk8 = [0,0]
xk9 = [0,0]
xk0[0] = yk0*w[0]
xk0[1] = yk0*w[1]
xk1[0] = yk1*w[0]
xk1[1] = yk1*w[1]
xk2[0] = yk2*w[0]
xk2[1] = yk2*w[1]
xk3[0] = yk3*w[0]
xk3[1] = yk3*w[1]
xk4[0] = yk4*w[0]
xk4[1] = yk4*w[1]
xk5[0] = yk5*w[0]
xk5[1] = yk5*w[1]
xk6[0] = yk6*w[0]
xk6[1] = yk6*w[1]
xk7[0] = yk7*w[0]
xk7[1] = yk7*w[1]
xk8[0] = yk8*w[0]
xk8[1] = yk8*w[1]
xk9[0] = yk9*w[0]
xk9[1] = yk9*w[1]
print("x hat values")
print(xk0, xk1, xk2, xk3, xk4, xk5, xk6, xk7, xk8, xk9, sep="\n")

