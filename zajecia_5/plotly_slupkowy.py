import plotly.offline as py
import plotly.graph_objs as go

data = [2, 1, 1, 1, 207, 1, 59, 16, 3, 6]
names = ['Bolesław', 'Prus', 'Lalka', 'Tom', 'I', 'I.', 'Jak', 'wygląda', 'firma', 'J.']

bars = []
for d, n in zip(data, names):
    bars.append(go.Bar(
        x=[n],
        y=[d],
        width=0.5,
        opacity=0.7,
        name=n,
    ))

fig = go.Figure(data=bars)

py.plot(fig)
# Zapis do pliku:
# py.plot(fig, filename='plotly.html')
