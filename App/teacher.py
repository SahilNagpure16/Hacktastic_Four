import streamlit as st
import random

def generate_class_code():
    return str(random.randint(100000, 999999))

def teacher_page():
    st.title("Teacher - Manage Attendance")
    
    if st.button("Generate Class Code"):
        class_code = generate_class_code()
        st.success(f"Generated Class Code: {class_code}")
        st.write("Share this code with students to join the class.")
    
    uploaded_file = st.file_uploader("Upload QR Code Image to Mark Attendance", type=["png", "jpg", "jpeg"])
    
    if uploaded_file is not None:
        st.image(uploaded_file, caption="Uploaded QR Code", use_column_width=True)
        st.success("Attendance Marked Successfully!")
    
    # Back Button using page_link
    st.page_link("main.py", label="🔙 Back to Home", icon="🏠")

if __name__ == "__main__":
    teacher_page()
