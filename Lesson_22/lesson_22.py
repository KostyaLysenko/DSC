A={2,3,6,12,5,23,73, 73}

print(A)
print(len(A)) #потужність множини
B=set([1,2,5,7,12,10,8])
print(B)
x=3
C={1,2,5}
print(min(A))
print(max(A))

print(x in A)
print(x not in A)

#Special operations
print(A==B) #тотожність множин
print(A !=B)
print(A<B) #чи є А підмножиною В
print(C<B) #чи є С підмножиною В
print(A&B) #пересічення множин (7+shift)
print(A-B)
print(A^B)#симетрична різнiсть(6+shift)
# print(C:=A^B)

#Methods
print(A.isdisjoint(B))
print(C.issubset(B)) #C<B
print(A.issuperset(B)) #A>B
print(A.union(B,C))
print(A.intersection(B))
print(A.difference(B))
print(A.symmetric_difference(B))
print(A.update([100,200,300]))
print(A)

A.add(1000)
print(A)
A.remove(1000)
print(A)
A.discard(1000)
print(A)
A.pop()
print(A)






print(m:=15)
print(p:=16)
print(c:=19)
print(m_p:=7)
print(c_m:=9)
print(p_c:=6)
print(m_p_c:=4)
print(RES:=m+p-m_p+c-c_m-p_c+m_p_c)

# # **********************************
# MPC={1,2,3,4}
# print(MPC)
# MP={1,2,3,4,5,6,7}
# MC={1,2,3,4,8,9,10,11,12}
# PC={1,2,3,4,13,14}
# M={1,2,3,4,5,6,7,8,9,10,11,12,15,16,17}
# print(len(M))
# P={1,2,3,4,5,6,7,13,14,18,19,20,21,22,23,24}
# print(len(P))
# C={1,2,3,4,8,9,10,11,12,13,14,25,26,27,28,29,30,31,32}
# print(len(C))
# #Хоча б по одній п'ятірці отримало 32 учні тому що ми перечислили усіх учнів які отримували п'ятірки и останній елемент дорівнює їх кількості
# *************************************

ver=30
dosch=12
viter=8
holod=4
d_v=5
d_h=3
v_h=2
d_v_h=1
print(ver-(dosch+viter-d_v+holod-d_h-v_h+d_v_h))



