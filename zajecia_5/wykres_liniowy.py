from matplotlib import pyplot as plt  # "import as" pozwala odwoływać się do zaimportowanej biblioteki przez inną nazwę

plt.rcdefaults()
plt.clf()

data = [2, 1, 1, 1, 207, 1, 59, 16, 3, 6]
names = ['Bolesław', 'Prus', 'Lalka', 'Tom', 'I', 'I.', 'Jak', 'wygląda', 'firma', 'J.']

plt.title("Liczba wystąpień słów")
plt.plot(data, linewidth=2)

plt.xticks(range(len(names)), names, rotation=90)
plt.xlabel("Próbki")
plt.ylabel("Liczba wystąpień")

plt.show()
# wykres możemy też zapisać do pliku (format jest autorozpoznawany po rozszerzeniu)
plt.savefig('out.png')