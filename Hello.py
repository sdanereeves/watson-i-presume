# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
# Copyright (c) Secondary content - Steven D. Reeves IBM
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

# NOTE FROM THE AUTHOR - A WATSONX PROJECT ID IS REQUIRED FOR THE CODE TO WORK.
# ONCE A PROJECT ID IS ADDED THE CODE IF UNALTERED WILL EXECUTE.

import streamlit as st
from streamlit.logger import get_logger
import Tutorial1_use_case_NRAG
import getpass
import os


LOGGER = get_logger(__name__)

# Replace with your watsonx project id (look up in the project Manage tab)
watsonx_project_id = ""
# API Key is collected from user
#api_key = ""

# Use the full page instead of a narrow central column
st.set_page_config(layout="wide")

# New sdr
# sdr additional code
jpeg_image_path = "watsonx.jpg"
image_width = 250
st.image(jpeg_image_path, width=image_width)
# New sdr

# Streamlit app title
st.title("(BlackBelt) Dr. Watson I presume...")

# Write bold text
st.markdown('<font color="blue"><b><i>Enter your prompt!</i></b></font>', unsafe_allow_html=True)

#api_key = st.text_input("Enter You API Key...")
#st.write("You entered:", api_key)
api_key = st.text_input("Enter your API Key:", type="password")

question = st.text_area('Question',height=100)
button_clicked = st.button("Answer the question")
st.subheader("Response")

#prompt = "Answer the question provided in '''.  Give specific use cases. Question: ''' "
prompt = "Answer the question provided in '''.  Give specific use cases. Question: ''' "
endcap = "'''"
finalquestion=(prompt+question+endcap)

# Invoke the LLM when the button is clicked
if button_clicked:
    response = Tutorial1_use_case_NRAG.answer_questions_from_doc(api_key,watsonx_project_id,finalquestion)
    #response="This is the response."
    print("Response from the LLM:" + response)
    st.write(response)