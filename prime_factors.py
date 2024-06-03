def prime(n):
    for i in range(2,n+1):
        if n % i == 0:
            count =1
            for j in range(2,int((i//2)+1)):
                if i % j == 0:
                    count=0
                    break
            if count == 1:
                print(i,end=" ")
prime(420)
        