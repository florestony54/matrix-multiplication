a = [[1,3,5], [2,4,6]]
b = [[1,6],[2,5],[3,4]]
c = [[], [], [], []]
d = [[], [], [], [], [], [], [], [], []]
a_b_product = []
b_a_product = []

# Matrix multiplication of A*B
def a_times_b():
    for i in range(len(a[0])):
        c[0].append(a[0][i]*b[i][0])
        c[1].append(a[0][i]*b[i][1])
        c[2].append(a[1][i]*b[i][0])
        c[3].append(a[1][i]*b[i][1])

    for j in range(len(c)):
        """d[0].insert(i, sum(c[j]))
        d[1].insert(i, sum(c[j+2]))"""
        a_b_product.append(sum(c[j]))

    print("A*B is: " + str(a_b_product))
# Product matrix printed as a linear representation of a 2x2



#Matrix Multiplication of B*A
def b_times_a():
    for i in range(len(b[0])):
        d[0].append(b[0][i]*a[i][0])
        d[1].append(b[0][i]*a[i][1])
        d[2].append(b[0][i]*a[i][2])
        d[3].append(b[1][i]*a[i][0])
        d[4].append(b[1][i]*a[i][1])
        d[5].append(b[1][i]*a[i][2])
        d[6].append(b[2][i]*a[i][0])
        d[7].append(b[2][i]*a[i][1])
        d[8].append(b[2][i]*a[i][2])
        
       

    for j in range(len(d)):
        b_a_product.append(sum(d[j]))

    print("B*A is: " + str(b_a_product))
# Product matrix printed as a linear representation of a 3x3


