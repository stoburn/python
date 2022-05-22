motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)
motorcycles.append('kawasaki')
print(motorcycles)
motorcycles.insert(0, 'harley davidson')
print(motorcycles)
del motorcycles[0]
print(motorcycles)
popped_motorcycles = motorcycles.pop()
print(motorcycles)
print(popped_motorcycles)
popped_motorcycles = motorcycles.pop(0)
print(motorcycles)
print(popped_motorcycles)
motorcycles.remove('suzuki')
print(motorcycles)
