import sys
import matplotlib.pyplot as plt

data = []
length = []
i = 1

with open(f'{sys.argv[1]}', "r") as file:  # Вместо f'{sys.argv[1]}' нужно указать относительный путь из твоей директории или абсолютный в '...'. Если файл в той же директории, то 'file.txt'. Если в нутри той, которая внутри текущей, то 'folder/file.txt'
	for line in file:
		value = float(line.replace(',','.'))
		data.append(value)
		length.append(i)
		i += 1
    
plt.plot(length, data)

plt.xlabel('Номер измерения')
plt.ylabel('Напряжение, кванты')

plt.title("График измерений")

plt.show()
