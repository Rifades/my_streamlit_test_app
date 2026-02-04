import streamlit as st
import pandas as pd

st.title("Todo List")
if 'my_todo_list' not in st.session_state:
    st.session_state.my_todo_list = []
col1, col2 = st.columns(2)
with col1:
    b = col1.text_input("Enter your todo item")
    a = col1.button("Add")
    c = col1.button("Clear")

if a and b:
    st.session_state.my_todo_list.append(b)
if c:
    st.session_state.my_todo_list = []
with col2:
    col2.write("Your Todo List:")
    for i in st.session_state.my_todo_list:
        col2.write(i)















