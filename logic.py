def or_opr(a,b):
    c = []
    for i in range(0,4):
        c.append(a[i] | b[i])
    return c

def not_opr(a):
    c = []
    for i in range(0,4):
        c.append(1 - a[i])
    return c

def imp_opr(a,b):
    c = []
    for i in range(0,4):
        if ((a[i] == 1) and (b[i] == 0)):
            c.append(0)
        else:
            c.append(1)
    return c

def and_opr(a,b):
    c = []
    for i in range(0,4):
        if (a[i] == 1) and (b[i] == 1):
            c.append(1)
        else:
            c.append(0)
    return c

def dimp_opr(a,b):
    c = []
    for i in range(0,4):
        if (a[i] == b[i]):
            c.append(1)
        else:
            c.append(0)
    return c

if __name__ == "__main__":
    S = []
    M = []
    S.append([0,0,1,1])
    M.append("@")
    S.append([0,1,0,1])
    M.append("#") #@ to express phi and # to express sai
    C = []
#    C.append("or")
    C.append("not")
#    C.append("imp")
#    C.append("and")
    C.append("dimp")
    change = True
    while(change):
        change = False
        if "not" in C:
            for i in range(0,len(S)):
                ns = not_opr(S[i])
                if not (ns in S):
                    change = True
                    S.append(ns)
                    M.append("~"+M[i])

        for i in range(0,len(S)):
            for j in range(0,len(S)):
                s1 = S[i]
                s2 = S[j]
                m1 = M[i]
                m2 = M[j]
                for c in C:
                    ns = [0,0,1,1]
                    if (c == "or"):
                        ns = or_opr(s1,s2)
                        if not(ns in S):
                            change = True
                            S.append(ns)
                            M.append("(" + m1 + "|" + m2 + ")")
                    if (c == "imp"):
                        ns = imp_opr(s1,s2)
                        if not(ns in S):
                            change = True
                            S.append(ns)
                            M.append("(" + m1 + "->" + m2 + ")")
                    if (c == "and"):
                        ns = and_opr(s1,s2)
                        if not(ns in S):
                            change = True
                            S.append(ns)
                            M.append("(" + m1 + "&" + m2 + ")")
                    if (c == "dimp"):
                        ns = dimp_opr(s1,s2)
                        if not(ns in S):
                            change = True
                            S.append(ns)
                            M.append("(" + m1 + "<->" + m2 + ")")
                    
    count = 0
    for i in range(0, len(S)):
        count += 1
        print(S[i]),
        print("for " + M[i])

    print("Total logic result: " + str(count))