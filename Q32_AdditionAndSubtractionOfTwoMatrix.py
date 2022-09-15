# Addition and Subtraction of two matrices.
def insertValues(mat,row,col):
    for i in range(row):
        a=[]
        print("Enter the values of row number",i+1,":")
        for j in range(col):
            a.append(int(input()))
        mat.append(a)

def displayElements(mat):
    for x in mat:
        for y in x:
            print(y,end='\t')
        print()

mat1=[]
mat2=[]
addmat=[]
submat=[]
row1=int(input("Enter the number of rows of the first matrix: "))
column1=int(input("Enter the number of columns of the first matrix: "))
row2=int(input("Enter the number of rows of the second matrix: "))
column2=int(input("Enter the number of columns of the second matrix: "))
while True:
    if row1!=row2 and column1!=column2:
        print("\nROW AND COLUMN NUMBERS OF THE MATRICES ARE NOT EQUAL. ENTER THEIR VALUES AGAIN...")
        row1=int(input("Enter the number of rows of the first matrix: "))
        column1=int(input("Enter the number of columns of the first matrix: "))
        row2=int(input("Enter the number of rows of the second matrix: "))
        column2=int(input("Enter the number of columns of the second matrix: "))
    elif row1!=row2:
        print("\nROW NUMBERS OF THE MATRICES ARE NOT EQUAL. ENTER THEIR VALUES AGAIN...")
        row1=int(input("Enter the number of rows of the first matrix: "))
        row2=int(input("Enter the number of rows of the second matrix: "))
    elif column1!=column2:
        print("\nCOLUMN NUMBERS OF THE MATRICES ARE NOT EQUAL. ENTER THEIR VALUES AGAIN...")
        column1=int(input("Enter the number of columns of the first matrix: "))
        column2=int(input("Enter the number of columns of the second matrix: "))
    else:
        break
print("Enter the elements of First Matrix:")
insertValues(mat1,row1,column1)
print("Enter the elements of Second Matrix:")
insertValues(mat2,row2,column2)
print("THE FIRST MATRIX IS:")
displayElements(mat1)
print("THE SECOND MATRIX IS:")
displayElements(mat2)
for (x,y) in zip(mat1,mat2):
    addmid=[]
    submid=[]
    for (m,n) in zip(x,y):
        addmid.append(m+n)
        submid.append(m-n)
    addmat.append(addmid)
    submat.append(submid)
print("THE RESULT OF THE ADDITION OF THE TWO MATRICES IS:")
displayElements(addmat)
print("THE RESULT OF THE SUBTRACTION OF THE TWO MATRICES IS:")
displayElements(submat)
