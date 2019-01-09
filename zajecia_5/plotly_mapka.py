import plotly.offline as py
import plotly.graph_objs as go

points = [
    ('Kraków',   (50.06465, 19.94498)),
    ('Warszawa', (52.22967, 21.01223)),
    ('Gdańsk',   (54.35202, 18.64664)),
]

data = []
for name, coords in points:
    data.append(go.Scattergeo(
        lon=[coords[1]],
        lat=[coords[0]],
        text='Niezwykle ważne miasto',
        marker=dict(
            size=15,
        ),
        name=name,
    ))

layout = go.Layout(
    title='Miasta w Polsce',
    geo=dict(
        resolution=50,
        projection=dict(type='mercator'),
        showland=True,
        showcountries=True,
        lonaxis=dict(range=[13, 25]),
        lataxis=dict(range=[48, 56]),
    ),
)

fig = go.Figure(layout=layout, data=data)

py.plot(fig)
