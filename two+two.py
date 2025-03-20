for t in range(10):
    for w in range(10):
        for o in range(10):
            for f in range(10):
                for u in range(10):
                    for r in range (10):
                        if t+t == o+10 and w+w== u and o+o==r and f == 1 and t!=w and t !=o and t!= f and t!=u and t!=r and w!= o and w!=f and w!= u and w!= r and o!=f and o!=u and o!=r and f!=u and f!=r and u != r : 
                            print(t,w,o,f,u,r)