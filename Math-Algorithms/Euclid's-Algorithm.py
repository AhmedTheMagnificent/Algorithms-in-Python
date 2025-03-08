def Euclid(x, y):
    assert x >= 0 and y >= 0 and x + y > 0
    
    while x > 0 and y > 0:
        if x >= y:
            x %= y 
        else:
            y %= x
            
    return x + y

print(Euclid(1980, 1848))


