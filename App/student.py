import streamlit as st
import qrcode
from io import BytesIO

def generate_qr_code(data):
    qr = qrcode.make(data)
    img_bytes = BytesIO()
    qr.save(img_bytes, format='PNG')
    return img_bytes.getvalue()

def student_page():
    st.title("Student - Join a Class")
    class_code = st.text_input("Enter 6-digit Class Code:")
    name = st.text_input("Enter Your Name:")
    roll_no = st.text_input("Enter Your Roll Number:")
    
    if st.button("Generate QR Code"):
        if class_code and name and roll_no:
            student_data = f"Class:{class_code}|Name:{name}|Roll:{roll_no}"
            qr_code = generate_qr_code(student_data)
            st.image(qr_code, caption="Your Attendance QR Code", use_column_width=True)
        else:
            st.error("Please fill all fields correctly.")
    
    # Back Button using page_link
    st.page_link("main.py", label="🔙 Back to Home", icon="🏠")

if __name__ == "__main__":
    student_page()
