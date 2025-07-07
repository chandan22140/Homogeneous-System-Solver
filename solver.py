def scaling_ro(A, rn, c):
    for i in range(len(A[rn])):
        A[rn][i]  = round(c*A[rn][i], 5)

def rowreplace_ro(A, i, j, c1, c2):
    for k in range(len(A[i])):
        A[i][k]  = round(c1*A[i][k]+c2*A[j][k], 5 )

def row_exchange_ro(A, i, j):    
    A[i], A[j] =  A[j], A[i]        

# take input from file
f = open("inpMATHassgn.txt", "r")
s = f.read().split("\n")
r = int(s[0])
c = int(s[1])

m  =  []
for line in s[2:]:  
    m.append(list(map(float, line.split())))
# find RREF
wp = 0
p = []
count = 0
for i in range(r):
    pivot_found = False

    while pivot_found != True:
        for k in range(i,r):
            if m[k][wp]!=0:
                pivot_found = True
                count += 1
                # k is pivot ele row
                # wp is pivot ele position in that row
                
                if k!=i:
                    row_exchange_ro(m, i, k)
                p.append((i,wp))
                # (i,wp) is pivot position  
                #   
                break
        else:
            wp+=1
            
        if wp>=c:
            break
    if wp>=c:
        break
    else:
        for l in range(i+1,r):
            rowreplace_ro(m, l, i, 1, -(m[l][wp])/(m[i][wp]))
print("PIVOT POSITION:")
print(p)
for i,j in p:
    for k in range(i):
        rowreplace_ro(m, k, i, 1, -m[k][j]/m[i][j])
for i,j in p:
    if m[i][j]!=1:
        scaling_ro(m, i, 1/m[i][j])



print("RREF:")
for i in m:
    i = list(map(str, i))
    print("  ".join(i))
print("")

p_ = list(range(c))
for i in p:
    if i[1] in p_:
        p_.remove(i[1])

s = []
for i  in p_:
    sum = [0]*c
    sum[i]+=1
    for j in p:
        sum[j[1]]-=m[j[0]][i]
    s.append((i, sum))

print("SOLUTION:")

print(f'{[0]*c}', end="")
for u,v in s:
    print(f'+x_{u+1}*{v}', end="")

f.close()

# m = [[0,1,0,2,-1,0,5], [0,0,1,2,3,0,7],[0,0,0,0,0,1,8]]
# p = [(0,1),(1,2), (2,5)]
# c=7

# p_ = list(range(c))
# for i in p:
#     if i[1] in p_:
#         p_.remove(i[1])

# s = []
# for i  in p_:
#     sum = [0]*c
#     sum[i]+=1
#     for j in p:
#         sum[j[1]]-=m[j[0]][i]
#     s.append((i, sum))

# print(f'{[0]*c}', end="")
# for u,v in s:
#     print(f'+x_{u}*{v}', end="")
