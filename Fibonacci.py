FIB=1597

num_1,num_2=0,1


while num_2 <=FIB:
    print(num_1, num_2, end=" ")
    num_1=num_1+num_2
    num_2=num_1+num_2
