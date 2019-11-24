from modules import convert_to_dict as f


getList = f('presidents.csv')

index = []
name = []
for row in getList:
    index.append(row['Presidency'])
    name.append(row['President'])
print(index, 'first')
print(name, 'second')
combo = zip(index, name)
print(set(combo))