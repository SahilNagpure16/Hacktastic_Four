import gspread
from google.oauth2.service_account import Credentials
import streamlit as st


def attendence(name:str,sheet_id:str):
    
    scopes = [
    "https://www.googleapis.com/auth/spreadsheets"
    ]

    creds = Credentials.from_service_account_file("teacher.json", scopes=scopes)
    client = gspread.authorize(creds)

    # sheet_id = '1wunelFrIfT7YbiAvy0gac_lnII_AorQyIMn0RnCs9Pw'

    workbook = client.open_by_key(sheet_id)

    student_list = workbook.sheet1.col_values(2)
    if name in student_list:
        roll = student_list.index(name)
        workbook.sheet1.update_cell(roll+1,3,'Yes')
    else:
        st.error("error student not found")
    
    

    
    
attendence('CJ','1wunelFrIfT7YbiAvy0gac_lnII_AorQyIMn0RnCs9Pw')