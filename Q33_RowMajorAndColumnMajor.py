# Display a matrix in Row Major and Column Major order
row=int(input("Enter the number of rows: "))
column=int(input("Enter the number of columns: "))
number=[]
for i in range(row):
    a=[]
    print("Enter the elements of row number",i+1)
    for j in range(column):
        a.append(int(input()))
    number.append(a)
print("THE MATRIX IS:")
for x in number:
    for y in x:
        print(y,end='\t')
    print()
print("THE MATRIX IN ROW MAJOR ORDER IS:")
for x in number:
    for y in x:
        print(y,end=' ')
print("\nTHE MATRIX IN COLUMN MAJOR ORDER IS:")
for j in range(column):
    for i in range(row):
        print(number[i][j],end=' ')
