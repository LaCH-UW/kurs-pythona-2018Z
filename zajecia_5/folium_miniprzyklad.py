import folium
import webbrowser

m = folium.Map(location=[52.2117514, 20.9864695], zoom_start=17)

folium.Marker([52.211937, 20.984562], popup='Tu jesteśmy').add_to(m)

# Zapis do pliku:
m.save('folium.html')
# folium nie ma opcji "podglądu" używalnej w PyCharmie, więc możemy otworzyć zapisany plik:
webbrowser.open('folium.html')
