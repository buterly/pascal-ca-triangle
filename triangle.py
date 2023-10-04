# n = int(input('Enter height of triangle: '))
n = 10

def pascalElement(n,r):
    x = 1
    y = 1
    for i in range(n,n-r,-1):
        x *= i
    for i in range(2,r+1):
        y *= i

    return x//y

# finding all the rows and storing in a list

triangle =  []

for i in range(n,-1,-1):
    row = []
    for j in range(i+1):
        row.append(pascalElement(i,j))
    triangle.append(row)

# print(triangle)


# create a list of gap
gaps = []
for i in range(n+1):
    rowGap = []
    for j in range(len(triangle[i])):
        rowGap.append(len(str(triangle[i][j])))
    gaps.append(rowGap)
# print(gaps)


# creating rows of final triangle
finalTriangle = []
fistRow = ' '.join([f'{elem}' for elem in triangle[0]])
finalTriangle.append(fistRow)


for i in range(1, n+1):
    row = ''
    for j in range(len(triangle[i])):
        row += f'{gaps[i-1][j]*" "}{triangle[i][j]}'
    # print(f'{row:^{sum(gaps[i-1])}}', sum(gaps[i-1]))
    finalTriangle.append(f'{row:^{len(finalTriangle[0])}}')
        
        
# printing

for rows in range(len(finalTriangle)-1,-1,-1):
    print(finalTriangle[rows])
    # print('hi')
        
# print(finalTriangle)

"""
        
      1
    1   1
   1  2  1
  1  3  3 1
 1 4  6  4 1
1 5 10 10 5 1  
  
        
        
"""



