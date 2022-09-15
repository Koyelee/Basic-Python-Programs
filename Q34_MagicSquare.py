# Check a matrix is Magic Square or not
mat=[]
sum1=0
sum2=0
n=int(input("Enter the number of rows or columns: "))
print("Enter the elements:")
for i in range(n):
    a=[]
    print("Enter the values of row number",i+1,":")
    for j in range(n):
        a.append(int(input()))
    mat.append(a)
print("THE MATRIX IS:")
for x in mat:
    for y in x:
        print(y,end='\t')
    print()
# ROW CHECK
for x in mat:
    for y in x:
        sum1+=y
    if sum2==0:
        sum2=sum1
    else:
        if(sum1!=sum2):
            print("THE GIVEN MATRIX IS NOT A SQUARE MATRIX!")
            exit(1)
    sum1=0
# COLUMN CHECK
for i in range (n):
    for j in range(n):
        sum1+=mat[j][i]
    if(sum1!=sum2):
        print("THE GIVEN MATRIX IS NOT A SQUARE MATRIX!")
        exit(1)
    sum1=0
# LEFT DIAGONAL CHECK
for i in range(n):
    sum1+=mat[i][i]
if(sum1!=sum2):
    print("THE GIVEN MATRIX IS NOT A SQUARE MATRIX!")
    exit(1)
sum1=0
# RIGHT DIAGONAL CHECK
j=n-1
for i in range(n):
    sum1+=mat[i][j]
    j-=1
if(sum1!=sum2):
    print("THE GIVEN MATRIX IS NOT A SQUARE MATRIX!")
    exit(1)
    sum1=0
print("THE GIVEN MATRIX IS A SQUARE MATRIX...!")