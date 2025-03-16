motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[1] = 'harley'
print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)

motorcycles.insert(0, 'kawasaki')
print(motorcycles)

del motorcycles[0]
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle) #Ducati is last on the list

last_owned = motorcycles.pop()
print (f"The last motorcycle I owned was a {last_owned.title()}") #Susuki is last after Ducati was removed.

first_owned = motorcycles.pop(0)
print(f"The first motorcycle I ever owned was a {first_owned.title()}") #Honda is now removed.

motorcycles = ['honda', 'harley', 'suzuki', 'ducati', 'yamaha']
print(motorcycles)

motorcycles.remove('yamaha')
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me")