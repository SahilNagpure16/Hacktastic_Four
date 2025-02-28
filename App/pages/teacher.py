import streamlit as st
import random
from attendence import attendence
from QRscanner import QRmodule


def extractName(data:str):
    

# Split the string by '|'
    parts = data.split('|')

    # Iterate through parts and find the one that starts with 'Name:'
    for part in parts:
        if part.startswith('Name:'):
            name = part.split(':')[1]
            break
    return name

def generate_class_code():
    return str(random.randint(100000, 999999))

def teacher_page():
    st.title("Teacher - Manage Attendance")
    
    if st.button("Generate Class Code"):
        class_code = generate_class_code()
        st.success(f"Generated Class Code: {class_code}")
        st.write("Share this code with students to join the class.")
    
    with st.form(key="string_input_form"):
    # Add a text input field
        user_input = st.text_input(
            label="Enter excel link here",
            placeholder="Link"
        )
        
        submit_button = st.form_submit_button(label="Submit")
    
    if user_input:   
        spreadsheet_id = user_input.split("/d/")[1].split("/")[0]
        st.write("Spreadsheet ID:", spreadsheet_id)
        studentname =  QRmodule()
        if studentname:
            studentname = extractName(studentname)
        
        attendence(studentname,spreadsheet_id)
        
        
    else:
        st.warning("please enter link")
        
        
    

    
    # Back Button using page_link
    st.page_link("main.py", label="🔙 Back to Home", icon="🏠")

if __name__ == "__main__":
    teacher_page()