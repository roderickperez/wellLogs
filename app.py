# streamlit_app.py

import streamlit as st
from gsheetsdb import connect


from google.oauth2 import service_account


###################################
# Public

# Create a connection object.
conn = connect()

# Perform SQL query on the Google Sheet.
# Uses st.cache to only rerun when the query changes or after 10 min.
@st.cache(ttl=600)
def run_query(query):
    rows = conn.execute(query, headers=1)
    rows = rows.fetchall()
    return rows

sheet_url = st.secrets["public_gsheets_url"]
rows = run_query(f'SELECT * FROM "{sheet_url}"')

# Print results.
for row in rows:
    st.write(f"{row.name} has a :{row.pet}:")
    
    
    
########################
# Private

# Create a connection object.
credentials = service_account.Credentials.from_service_account_info(
    st.secrets["gcp_service_account"],
    scopes=[
        "https://www.googleapis.com/auth/spreadsheets",
    ],
)
conn = connect(credentials=credentials)

# Perform SQL query on the Google Sheet.
# Uses st.cache to only rerun when the query changes or after 10 min.
@st.cache(ttl=600)
def run_query(query):
    rows = conn.execute(query, headers=1)
    rows = rows.fetchall()
    return rows

sheet_url = st.secrets["private_gsheets_url"]
rows = run_query(f'SELECT * FROM "{sheet_url}"')

# Print results.
for row in rows:
    st.write(f"{row.name} has a :{row.pet}:")












#########################

# import streamlit as st
# from google.cloud import firestore
# from google.oauth2.service_account import Credentials
# from gsheetsdb import connect

# ########################
# from collections.abc import Iterable
# ###########################
# try:
#     from collections.abc import Iterable
# except ImportError:
#     from collections import Iterable


# #############################

# # db = firestore.Client.from_service_account_json("firestore-key.json")

# import json
# key_dict = json.loads(st.secrets["textkey"])
# creds = Credentials.from_service_account_info(key_dict)
# db = firestore.Client(credentials=creds, project="welllogwebapp-355315")

# # Streamlit widgets to let a user create a new post
# name = st.text_input("Well Name")
# xLoc = st.text_input("X Location")
# yLoc = st.text_input("Y Location")
# submit = st.button("Add New Well")

# # Once the user has submitted, upload it to the database
# if name and xLoc and yLoc and submit:
# 	doc_ref = db.collection("wells").document(name)
# 	doc_ref.set({
# 		"name": name,
# 		"xLoc": xLoc,
#         "yLoc": yLoc
# 	})

# # And then render each post, using some light Markdown
# wells_ref = db.collection("wells")

# for doc in wells_ref.stream():
#     well = doc.to_dict()
#     name = well["name"]
#     xLoc = well["xLoc"]
#     yLoc = well["yLoc"]

#     st.write("Well Name: ", name)
#     st.write("X Location: ", xLoc)
#     st.write("Y Location: ", yLoc)
    
    
    
    
# # Create a connection object (Private)
# credentials = Credentials.from_service_account_info(
#     st.secrets["gcp_service_account"],
#     scopes=[
#         "https://www.googleapis.com/auth/spreadsheets",
#     ],
# )
# conn = connect(credentials=credentials)

# # Perform SQL query on the Google Sheet.
# # Uses st.cache to only rerun when the query changes or after 10 min.
# @st.cache(ttl=600)
# def run_query(query):
#     rows = conn.execute(query, headers=1)
#     rows = rows.fetchall()
#     return rows

# sheet_url = st.secrets["private_gsheets_url"]
# rows = run_query(f'SELECT * FROM "{sheet_url}"')

# # Print results.
# for row in rows:
#     st.write(f"{row.name} has a :{row.pet}:")