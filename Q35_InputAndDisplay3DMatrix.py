# Input and Display a 3D Matrix
print("Enter the dimensions of the 3d Matrix:")
length=int(input())
breadth=int(input())
height=int(input())
matrix=[]
print("Enter the elements:")
for x in range(length):
    a=[]
    print("Enter the elements for row number",x+1,":")
    for y in range(breadth):
        b=[]
        print("Enter the elements for column number",y+1,":")
        for z in range(height):
            b.append(int(input()))
        a.append(b)
    matrix.append(a)
print("THE 3D MATRIX IS:")
for x in matrix:
    for y in x:
        for z in y:
            print(z,end='\t')
        print()
    print()
