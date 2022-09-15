# Perform multiplication between two given matrices

def inputElements(mat,row,col):
    for i in range(row):
        print("Enter the datas of row number",i+1)
        mid=[]
        for j in range(col):
            mid.append(int(input()))
        mat.append(mid)

def displayElements(mat):
    for x in mat:
        for y in x:
            print(y,end='\t')
        print()

row1=int(input("Enter number of rows for the first matrix: "))
col1=int(input("Enter number of columns for the first matrix: "))
row2=int(input("Enter number of columns for the second matrix: "))
col2=int(input("Enter number of columns for the second matrix: "))
if col1!=row2:
    print("MULTIPLICATION BETWEEN THE MATRICES IS NOT POSSIBLE...!! X(")
else:
    mat1=[]
    mat2=[]
    matMul=[]
    mid=[]
    a=0
    b=0
    x=0
    y=0
    print("Enter the elements for first matrix:")
    inputElements(mat1,row1,col1)
    print("Enter the elements for second matrix:")
    inputElements(mat2,row2,col2)
    print("FIRST MATRIX:")
    displayElements(mat1)
    print("SECOND MATRIX:")
    displayElements(mat2)
    for i in range(row1):
        mid=[]
        for j in range(col2):
            sum=0
            while b<col1:
                sum+=mat1[a][b]*mat2[x][y]
                b+=1
                x+=1
            mid.append(sum)
            b=0
            x=0
            y+=1
        matMul.append(mid)
        a+=1
        y=0
    print("THE RESULT OF THE MULTIPLICATION OF THE GIVEN MATRICES IS:")
    displayElements(matMul)
