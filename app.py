import streamlit as st
from google.cloud import firestore
from google.oauth2.service_account import Credentials

# db = firestore.Client.from_service_account_json("firestore-key.json")

import json
key_dict = json.loads(st.secrets["textkey"])
creds = Credentials.from_service_account_info(key_dict)
db = firestore.Client(credentials=creds, project="welllogwebapp-355315")

# Streamlit widgets to let a user create a new post
name = st.text_input("Well Name")
xLoc = st.text_input("X Location")
yLoc = st.text_input("Y Location")
submit = st.button("Add New Well")

# Once the user has submitted, upload it to the database
if name and xLoc and yLoc and submit:
	doc_ref = db.collection("wells").document(name)
	doc_ref.set({
		"name": name,
		"xLoc": xLoc,
        "yLoc": yLoc
	})

# And then render each post, using some light Markdown
wells_ref = db.collection("wells")

for doc in wells_ref.stream():
    well = doc.to_dict()
    name = well["name"]
    xLoc = well["xLoc"]
    yLoc = well["yLoc"]

    st.write("Well Name: ", name)
    st.write("X Location: ", xLoc)
    st.write("Y Location: ", yLoc)