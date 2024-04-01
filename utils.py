# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
from PIL import Image
import os

def sidebar_api(secrets = False):
    api_key = None
    if secrets:
        os.environ['OPENAI_API_KEY'] = st.secrets["apikey"]
    if  api_key is None:
        api_key = st.sidebar.text_input("API Key", type="password")
    if api_key:
        os.environ['OPENAI_API_KEY'] = api_key
    else:
        st.sidebar.warning("Please enter your API key to proceed.")

def lyzr_template_end():
    with st.expander("ℹ️ - About this App"):
        st.markdown("This app uses RLHF to generate text from the meta prompt and user prompt.")
        st.link_button("Lyzr", url='https://www.lyzr.ai/', use_container_width = True)
        st.link_button("Book a Demo", url='https://www.lyzr.ai/book-demo/', use_container_width = True)
        st.link_button("Discord", url='https://discord.gg/nm7zSyEFA2', use_container_width = True)
        st.link_button("Slack", url='https://join.slack.com/t/genaiforenterprise/shared_invite/zt-2a7fr38f7-_QDOY1W1WSlSiYNAEncLGw', use_container_width = True)

def demo_page_config(layout = "centered"):
    st.set_page_config(
        page_title="Page Title on top",
        layout=layout,  # or "wide" 
        initial_sidebar_state="auto",
        page_icon="lyzr-logo-cut.png"
    )

def temp_directory():
    if not os.path.exists('tempDir'):
        os.makedirs('tempDir')

def style_app():
    # You can put your CSS styles here
    st.markdown("""
    <style>
    .app-header { visibility: hidden; }
    .css-18e3th9 { padding-top: 0; padding-bottom: 0; }
    .css-1d391kg { padding-top: 1rem; padding-right: 1rem; padding-bottom: 1rem; padding-left: 1rem; }
    </style>
    """, unsafe_allow_html=True)

def lyzr_demo_start(main = False):
    image = Image.open("lyzr-logo.png")
    st.image(image, width=150)
    if main:
        # App title and introduction
        st.title("App Title")
        st.markdown("### Welcome to the App Title!")
        st.markdown("Tiny intro on what the app does")

        # Instruction for the users
        st.markdown("#### (Start with an emoji here) Clear short instruction")
        st.caption('Note:.')

def lyzr_demo_end(text = "This app uses Lyzr Core."):
    with st.expander("ℹ️ - About this App"):
        st.markdown(f"""
        {text} For any inquiries or issues, please contact Lyzr.
        """)
        st.link_button("Lyzr", url='https://www.lyzr.ai/', use_container_width = True)
        st.link_button("Book a Demo", url='https://www.lyzr.ai/book-demo/', use_container_width = True)
        st.link_button("Discord", url='https://discord.gg/nm7zSyEFA2', use_container_width = True)
        st.link_button("Slack", url='https://join.slack.com/t/genaiforenterprise/shared_invite/zt-2a7fr38f7-_QDOY1W1WSlSiYNAEncLGw', use_container_width = True)
