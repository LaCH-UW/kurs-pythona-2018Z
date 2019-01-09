from matplotlib import pyplot as plt

plt.rcdefaults()
plt.clf()

data = [2, 1, 1, 1, 207, 1, 59, 16, 3, 6]
names = ['Bolesław', 'Prus', 'Lalka', 'Tom', 'I', 'I.', 'Jak', 'wygląda', 'firma', 'J.']

plt.title("Liczba wystąpień słów")
for idx, value in enumerate(data):
    plt.bar(idx, value)

plt.xticks(range(len(names)), names, rotation=90)
plt.xlabel("Próbki")
plt.ylabel("Liczba wystąpień")

plt.show()
