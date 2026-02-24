n,m = list(map(int, input().split()))
a_i = list(map(int, input().split()))
b_i = list(map(int, input().split()))
e = int(input())
e_max = 0
e1 = e
res_Danya = 0
res_Diana = 0
K = 0
a_i_sum = sum(a_i)
b_i_sum = sum(b_i)

##for i in range(e):
##    e_max += e-i
e_max = ((1+e)/2)*e
##print(e_max)

if e_max >= max(a_i) and e_max >= max(b_i):
    if a_i_sum > b_i_sum:
        print("Danya")
        print(str(a_i_sum) + ":" + str(b_i_sum))

    elif sum(a_i) < sum(b_i):
        print("Diana")
        print(str(b_i_sum) + ":" + str(a_i_sum))
    else:
        print("Draw")
        print(str(b_i_sum) + ":" + str(a_i_sum))

else:
    for x in range(n): #Danya
        while e1>0:
            if a_i[x]>=e1:
                res_Danya += e1
    ##            print("res_Danya increased by e1 =", e1)
            if a_i[x]<e1:
                res_Danya += a_i[x]
    ##            print("res_Danya increased by a_i[x] =", a_i[x])
            a_i[x]-=e1
            e1 -= 1
            if a_i[x]<=0:
                e1 = 0
    ##            print("hi")
        e1 = e
        if a_i[x]>0:
            break
        
    e1 = e
    for x in range(m): #Diana
    ##    print(b_i[x])
        while e1>0:
            if b_i[x]>=e1:
                res_Diana += e1
    ##            print("res_Diana increased by e1 =", e1)
            if b_i[x]<e1:
                res_Diana += b_i[x]
    ##            print("res_Diana increased by b_i[x] =", b_i[x])
            b_i[x]-=e1
            e1 -= 1
            if b_i[x]<=0:
                e1 = 0
    ##            print("hi2")

        e1 = e
    ##    print("b_i[x]",b_i[x])
        if b_i[x]>0:
            break



    if res_Danya > res_Diana:
        print("Danya")
        print(str(res_Danya) + ":" + str(res_Diana))
    if res_Danya < res_Diana:
        print("Diana")
        print(str(res_Diana) + ":" + str(res_Danya))
    if res_Danya == res_Diana:
        print("Draw")
        print(str(res_Diana) + ":" + str(res_Danya))
