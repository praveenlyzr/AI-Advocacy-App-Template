import os
# import lyzr     
from PIL import Image
import streamlit as st
from utils import *

demo_page_config(layout="wide") #remove variable to make it centered
temp_directory() #creates a temp directory for storing things
sidebar_api(secrets=True) #remove variable to utilize sidebar input. currently uses secrects.
style_app() #comment out if you dont have CSS file

# write all definitions of functions in utils

lyzr_demo_start(main=True) # Load and display the logo. change main = false if you dont want the main page text (will only show logo)

# Start of the main container
with st.container():
    st.text_area("Codes go here", value=os.environ['OPENAI_API_KEY'])

lyzr_demo_end() # Footer or any additional information. use var [text] to display any aditional info

#if you want to change anything use the utils folder.