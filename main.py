import streamlit as st
import functions as fn

todos = fn.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    fn.write_todos(todos)


st.title("The Great Todo App")
st.subheader("This is the greatest todo app.")
st.write("This will surely increase your productivity.")

for i in todos:
    st.checkbox(i)

st.text_input(label="", placeholder="Add a new todo", on_change=add_todo, key="new_todo")