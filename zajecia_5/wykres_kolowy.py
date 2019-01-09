from matplotlib import pyplot as plt

plt.rcdefaults()
plt.clf()

data = [2, 1, 1, 1, 59, 1, 27, 16, 3, 6]
names = ['Bolesław', 'Prus', 'Lalka', 'Tom', 'I', 'I.', 'Jak', 'wygląda', 'firma', 'J.']

plt.title("Liczba wystąpień słów")
plt.pie(data, labels=names)
plt.axis('equal')

plt.show()
