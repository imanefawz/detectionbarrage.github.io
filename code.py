import streamlit as st
import geopandas as gpd
import numpy as np
import leafmap.foliumap as leafmap

st.set_page_config(
    page_title="Barrage Sidi Mohamed Ben Abdellah",
    page_icon="💧",
    layout="centered",  
)
st.markdown("<h2 style='font-size:32px; text-align:center;'>Barrage Sidi Mohamed Ben Abdellah</h2>", unsafe_allow_html=True)

m = leafmap.Map()


# Vérifier si les colonnes attributs existent pour les jours sélectionnés
selected_column2017 = f'https://github.com/imanefawz/detectionbarrage.github.io/blob/main/2017/envi'
selected_column2023 = f'https://github.com/imanefawz/detectionbarrage.github.io/blob/main/2023/envi'
# Configurer et exécuter la boucle d'événements avec asyncio

m.split_map(
        left_layer=selected_column2017 , right_layer=selected_column2023 ,
        left_label='annee 2017',
        right_label='annee 2023',
        left_position=  "topleft",
        right_position = "topright",
    )




labels = ['Eau','Vegetation', 'Sol nu','Bati']
# color can be defined using either hex code or RGB (0-255, 0-255, 0-255)
colors = [
    (0, 0, 255),   #  la classe 1
    (0, 255, 0),    #  la classe 2
    (255, 255, 0),    #  la classe 3
    (255, 0, 0),     ]    
  

m.add_legend(title='Legend', labels=labels, colors=colors)  
m.to_streamlit(height=600)
