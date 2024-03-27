import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    todo_input = st.session_state['new_todo']
    todos.append(todo_input + '\n')
    functions.write_todos(todos)


st.title('My Todo App')
st.subheader('This is my todo app.')
st.write('This app is to increase your productivity.')


for todo in todos:
    st.checkbox(todo)

st.text_input(label='Enter to apply', placeholder='Add new todo...', on_change=add_todo, key='new_todo')