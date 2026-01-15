import streamlit as st

def main():
    st.title("Hello, World!")

if st.button("Click me"):
    st.write("Button clicked!")
st.checkbox("Check me")
if st.checkbox("Check me to show some text"):
    st.write("You're seeing this text beacuse you checked the checkbox")

user_input = st.text_input("enter text", "Sample text")
st.write("You have entered: ", user_input)
age = st.number_input("Enter your are", min_value=0, max_value=100)
st.write(f"Your age is: {age}")

message = st.text_area("Enter a message")
st.write(f"Your message: {message}")

choice = st.radio("Pick one", ["Choice 1", "Choice 2", "Choice 3"])
st.write(f"You chose: {choice}")
if st.button("Succses"):
    st.success("Operation was succsessful")

if __name__ == "__main__":
    main()