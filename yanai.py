l = input()
n1 = int(l.split()[0])
m1 = int(l.split()[1])
ls1 = []
ins = 0
cp1 = 0
cpp1 = 0
lcp1 = []
lcpp1 = []
for i in range(n1):
    ls1.append(input())
    for j in ls1[ins]:
        if j != " ":
            break;
        cp1 = cp1 + 1
    if cp1 == len(ls1[ins]) - 1:
        cp1 = 0
    lcp1.append(cp1)

    for ii in range(len(ls1[ins]) - 1, -1, -1):
        lol = ls1[ins]
        if lol[ii] != " ":
            break;
        cpp1 = cpp1 + 1
    if cpp1 == len(ls1[ins]) - 1:
        cpp1 = 0
    lcpp1.append((cpp1))
    ins = ins + 1
    cpp1 = 0
    cp1 = 0

ll = input()
n2 = int(ll.split()[0])
m2 = int(ll.split()[1])
ls2 = []
cp2 = 0
cpp2 = 0
ins = 0
lcp2 = []
lcpp2 = []
lol = ""    
for i in range(n2):
    ls2.append(input())
    for j in ls2[ins]:
        if j != " ":
            break;
        cp2 = cp2 + 1
    if cp2 == len(ls2[ins]) - 1:
        cp2 = 0
    lcp2.append(cp2)

    for ii in range(len(ls2[ins]) - 1, -1, -1):
        lol = ls2[ins]
        if lol[ii] != " ":
            break;
        cpp2 = cpp2 + 1

    if cpp2 == len(ls2[ins]) - 1:
        cpp2 = 0

    lcpp2.append(cpp2)
    ins = ins + 1
    cp2 = 0
    cpp2 = 0

#if (n1 == n2 and m1 == m2) or (n1 == n2 and  n1 == m1) or (n1 == n2 and n2 == m1) or (n1 == m1 and m2 == n2) or (n1 == n2 and m1 == m2) or (n1 == m2 and n2 == m1) or (n2 == m2 and m1 == m2) or (n2 == m1 and m1 == m2) or (n2 == m1 and n2 == m2) or (n1 == m2 and m1 == m2) or (n1 == m2 and n2 == m2) or (n1 == m1 and m1 == m2) or (n1 == m1 and n2 == m1) or (n1 == m1 and n1 == m2) or (n1 == n2 and n1 == m2):
###1
k = 0
kk2 = 0
###2
s = n1 - 1
for i in range(n1):
    k1 = ls1[i]
    k2 = ls2[i]
    k11 = k1[lcp1[i]:len(k1) - lcpp1[i]]
    k22 = k2[lcp2[i]:len(k2) - lcpp2[i]]
    if(k11 == k22):
        k = k + 1

    k2 = ls2[s]
    k1 = ls1[i]
    k11 = k1[lcp1[i]:len(k1) - lcpp1[i]]
    k22 = k2[lcp2[s]:len(k2) - lcpp2[s]]

    if(str(k11) == str(k22)):
        kk2 = kk2 + 1
    s = s - 1
    #print(len(k11))
    #print(len(k22))
    #print()
    #print(k11)
    #print(k22)
    #print()
if(k == n1 or kk2 == n1):
    print("YES")
    exit()


#if (n1 == n2 and m1 == m2) or (n1 == n2 and  n1 == m1) or (n1 == n2 and n2 == m1) or (n1 == m1 and m2 == n2) or (n1 == n2 and m1 == m2) or (n1 == m2 and n2 == m1) or (n2 == m2 and m1 == m2) or (n2 == m1 and m1 == m2) or (n2 == m1 and n2 == m2) or (n1 == m2 and m1 == m2) or (n1 == m2 and n2 == m2) or (n1 == m1 and m1 == m2) or (n1 == m1 and n2 == m1) or (n1 == m1 and n1 == m2) or (n1 == n2 and n1 == m2):
###3
k3 = ""
s3 = 0
ktp = ""
kj = ""
lin = 0
lin3 = 0
k33 = ""
s33 = m2 - 1
ktpp = ""
ans = 0
anss = 0
kj3 = 0

for i in range(n1):
    k3 = ls1[i]
    k33 = ls1[i]
    for j in range(n2):
        kj = ls2[j]
        kj3 = ls2[j]
        try:
            ktp = kj[s3] + ktp
        except:
            ktp = " " + ktp
        try:
            ktpp = ktpp + kj3[s33]
        except:
            ktpp = ktpp
    for ii in range(len(ktp) - 1, -1, -1):
        if ktp[ii] != " ":
            break;
        lin = lin + 1
    ktp = ktp[0:(len(ktp) - lin)]
    for ii in range(len(ktpp) - 1, -1, -1):
        if ktpp[ii] != " ":
            break;
        lin3 = lin3 + 1
    ktpp = ktpp[0:(len(ktpp) - lin3)]
    s3 = s3 + 1
    s33 = s33 - 1
    lin = 0
    lin3 = 0
    if ktp == k3:
        ans = ans + 1
    if ktpp == k33:
        anss = anss + 1
    ktp = ""
    ktpp = ""

if ans == n1 or anss == n1:
    print("YES")
    exit()    

print("NO")