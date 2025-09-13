n = int(input())
for i in range(1 , n + 1):
    row = ""
    if i == n:
        for j in range(1 , n + 1):
            row += "* "
        space = " " * (n - 2)
        row =space + row 
        print(row)
    else:
        space = " " * (n - 2) 
        row += space 
        mid = " " * (n - i)
        star = "* " * i 
        row += mid + star
        print(row)
for i in range(1 , n * 2 + 1):
    space = " " * (n - 2)
    row = space + "* " * n 
    print(row)
k = n  
for i in range(1 , n - 1):
    row = ""
    for j in range(1 , k + 1):
        row += "* "
    space = " " * (n - 2)
    row = space + row 
    k += 1 
    n -= 1
    print(row)
for i in range(1 , n - 1):
    k = n
    row = ""
    if i == n :
        space = "  " * n 
        row = space + "* "
        print(row)
    else:
        space = "  " * (n - 2)
        row += space
        mid = " " * (i)
        for j in range(1 , k + 1 ):
            row += "* "
        row += mid + star
        k -= 1
        n += 1
        print(row)
