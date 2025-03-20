twenty = list(range(1, 21))
print(twenty)

one_hundred = list(range(1,101))
print(one_hundred)

print(sum(one_hundred))

thirty=[]
for odd_thirty in range(1,31,2):
   thirty.append(odd_thirty)

print(thirty)

fourty=[]
for even_fourty in range(2,40,2):
   fourty.append(even_fourty)

print(fourty)

fifty = []
for threes_fifty in range(3,50,3):
    fifty.append(threes_fifty)

print(fifty)

cube = []
for cube_10 in range(1,11):
    cubes = cube_10**3
    cube.append(cubes)

print(cube)

cube_list = [value**3 for value in range(1,11)]
print(cube_list)