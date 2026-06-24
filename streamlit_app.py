import streamlit as st

st.title("Todo App")

if "todos" not in st.session_state:
    st.session_state.todos = []

new_todo = st.text_input("Add a new todo", key="new_todo_input")
if st.button("Add") and new_todo:
    st.session_state.todos.append({"text": new_todo, "done": False})
    st.rerun()

for i, todo in enumerate(st.session_state.todos):
    col1, col2, col3 = st.columns([0.05, 0.8, 0.15])
    with col1:
        done = st.checkbox("", value=todo["done"], key=f"check_{i}")
        if done != todo["done"]:
            st.session_state.todos[i]["done"] = done
            st.rerun()
    with col2:
        text = todo["text"]
        if todo["done"]:
            st.markdown(f"~~{text}~~")
        else:
            st.write(text)
    with col3:
        if st.button("Delete", key=f"del_{i}"):
            st.session_state.todos.pop(i)
            st.rerun()

if st.session_state.todos:
    total = len(st.session_state.todos)
    done_count = sum(1 for t in st.session_state.todos if t["done"])
    st.caption(f"{done_count}/{total} completed")
