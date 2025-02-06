# Import Libraries
import streamlit as st
import pandas as pd
from PIL import Image
icon = Image.open("Pokeball.png")
# Page configuration is always first, unless a variable needs to be stated first.
st.set_page_config(page_title='Kanto Region',page_icon=icon,layout='wide')

# Set up
hide_table_row_index = """
            <style>
            thead tr th:first-child {display:none}
            tbody th {display:none}
            </style>
            """
st.markdown(hide_table_row_index, unsafe_allow_html=True)

# Import the Pokedex data
@st.cache
def data():
    pokedex = pd.read_excel('Pokedex.xlsx',index_col=False).fillna('')
    pokedex['Type1'] = pokedex['Type1'].str.lower().str.capitalize()
    pokedex['Type2'] = pokedex['Type2'].str.lower().str.capitalize()

    return pokedex

def info():
    global col
    for c in pokedex.columns:
         col.text(f'''{c}: {pokedex[c].loc[index]}''')
    
def showImg():
    global disp
    pokemon = Image.open(f"images/{pokedex['Name'].loc[index]}.jpg")
    disp.image(pokemon)
    # ♀ and ♂ for nidoran

header = st.container()
with header:
    st.title("Who's that Pokemon?")
    st.write('### Kanto Edition')
    st.text(
        '''
        The Kanto Region consists of 151 Pokemon.
        On this webpage, you'll be able to explore the different types of Kanto Pokemon.
        '''
    )

about = st.container()
with about:
    st.write('### About')
    st.text('''
        Below you can explore the Kanto Pokedex by index.
        The features describe the Pokemon's:
        + Name
        + Type(s)
        + Species
        + Height
        + Weight
        + Entry
        + Abilities

        ''')
    #   Another option is for users to select the features
    #   they want for context.

setting = st.container()
with setting:
    pokedex = data()
    st.write('### Pokedex')
    number = st.slider('Select Pokedex Index',min_value=1,max_value=151,value=25,step=1)
    index = number-1   # User chooses how

test = st.container()
with test:
    st.write('##### Features')
    pokedex = data()

    col,disp = st.columns([3.5,0.75])
    info()
    showImg()
