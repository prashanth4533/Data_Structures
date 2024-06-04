a="liril"
b=[1,2,3,4,5]
c=12345
d=[]
x=10
matrix=[[1,2,3],[4,5,6],[7,8,9]]
# palindrome
    # print("palindrome" if a == a[::-1] else "not a palindrome" )

#reverse
    #1 print(a[::-1])
       
    #2
        # b.reverse()
        # print(b)
        
    #3-for list
        # print(list(reversed(b)))

    #4-using loop
        # for i in a:
        #     d.insert(0,i)
        # print(d)
    
    #5-append 
        # for i in range(len(a)-1,-1,-1):
        #     d.append(a[i])
        # print(d)

#fact
    # fact = lambda x: 1 if x == 0 else x * fact(x-1)
    # print(fact(5))
#prime
    # print("prime" if all(c%i!=0 for i in range(2,int(c**0.5)+1)) and c>1 else "not prime")
    
#fib
    # fib= lambda x: x if x<=1 else fib(x-1) + fib(x-2)
    # print(fib(7))
    
#occurence of each char in str
    # print({char: a.count(char) for char in a})
    
#transpose a matrix - swaps  row and coloumns
    # print([[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))])

#unique - list is without duplicates
    # print("Unique" if len(b)==len(set(b)) else "not unique")
