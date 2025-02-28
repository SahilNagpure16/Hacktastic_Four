import streamlit as st

def main():
    st.set_page_config(page_title='QR Attendance System', page_icon='✅', layout='centered')
    
    st.title('QR Attendance System')
    
    st.write("### Select your role:")
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("Join as a Student", use_container_width=True):
            st.success("You joined as a Student!")
    
    with col2:
        if st.button("Join as a Teacher", use_container_width=True):
            st.success("You joined as a Teacher!")

if _name_ == "_main_":
    main()