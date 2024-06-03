def fibonacciModified(t1, t2, n):
    #make a list of t
    t=[t1, t2]
    for i in range(2, n):
        t.append(t[i-2] + (t[i-1]**2))
    #the answer is the last value on the list  
    return t[n-1]
    
