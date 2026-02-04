import streamlit as st
import pandas as pd

st.title("Todo List")
if 'my_todo_list' not in st.session_state:
    st.session_state.my_todo_list = []
def delete_todo(todo):
    st.session_state.my_todo_list.pop(todo)
col1, col2 = st.columns(2)
with col1:
    with st.form('My Form', clear_on_submit=True):
        b = st.text_input("Enter your todo item")
        a = st.form_submit_button("Add")
        if a and b:
            st.session_state.my_todo_list.append(b)
            st.rerun()
    c = col1.button("Clear")
    if c:
        st.session_state.my_todo_list = []
        st.rerun()
with col2:
    col2.write("Your Todo List:")
    for i, task in enumerate(st.session_state.my_todo_list):
        c1, c2 = col2.columns(2)
        with c1:
            c1.write(f"**{i+1}.** {task}")
        with c2:
            c2.button("❌", key = f"delete_{i}", on_click = delete_todo, args = (i,))















