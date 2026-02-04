import streamlit as st
import pandas as pd
'''
st.title("My First Streamlit App")
st.write("Hello, World!")

x = st.sidebar.slider("Select a value")
y = st.sidebar.checkbox("Please Tick the Box")
z = st.sidebar.text_input("Enter your Name")
a = st.sidebar.selectbox("Select Profession", ["Student", "Teacher", "Doctor", "Engineer"])
b = st.sidebar.file_uploader("Upload a file", type=["xlsx"])
st.write("Hello", z)
st.write("You are a", a)

if y: 
    st.write(x, "squared is", x * x)
else:
    st.write("Hello", z, "Please check the box")
if b :
    df = pd.read_excel(b)
    st.dataframe(df)
else:
    st.write("File not uploaded")

#col1, col2 = st.columns(2)

tab1, tab2 = st.tabs(["Dataset", "Map"])
data = {'col1': [1, 2, 3], 'col2': [4, 5, 6]}
df = pd.DataFrame(data)
map_data = pd.DataFrame(
    [[19.07, 72.87], [19.20, 72.85], [19.15, 72.90]],
    columns=['lat', 'lon'])
with tab1:
    st.header("Dataset")
    st.dataframe(df)

with tab2:
    st.header("Map")
    st.map(map_data)
'''

'''
st.title("Button Example")

if 'count' not in st.session_state:
    st.session_state.count = 0 

a = st.button("Click Me")

if a:
    st.session_state.count += 1

st.write("Current count:", st.session_state.count)
'''
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















