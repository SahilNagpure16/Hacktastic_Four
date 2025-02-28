### main.py ###
import streamlit as st

# Page Configuration
st.set_page_config(page_title='QR Attendance System', page_icon='✅', layout='centered')

# Remove Scrollbar with Custom CSS
st.markdown(
    """
    <style>
    ::-webkit-scrollbar {
        display: none;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title
st.title('QR Attendance System')

st.write("### Select your role:")

# Centering Buttons
col1, col2 = st.columns(2)

with col1:
    student_button = st.button("🎓 Join as a Student", use_container_width=True)

with col2:
    teacher_button = st.button("🧑‍🏫 Join as a Teacher", use_container_width=True)

# Navigation Logic
if student_button:
    st.query_params.update({"page": "student"})
    st.switch_page("pages/student.py")

if teacher_button:
    st.query_params.update({"page": "teacher"})
    st.switch_page("pages/teacher.py")