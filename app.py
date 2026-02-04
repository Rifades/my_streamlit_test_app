import streamlit as st
import pandas as pd

st.title("Todo List")
if 'my_todo_list' not in st.session_state:
    st.session_state.my_todo_list = []
col1, col2 = st.columns(2)
with col1:
    with st.form('My Form', clear_on_submit=True):
        b = st.text_input("Enter your todo item")
        a = st.form_submit_button("Add")
        if a and b:
            st.session_state.my_todo_list.append(b)
    c = col1.button("Clear")
    if c:
        st.session_state.my_todo_list = []
with col2:
    col2.write("Your Todo List:")
    for i in st.session_state.my_todo_list:
        col2.write(i)















