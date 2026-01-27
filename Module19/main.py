import pandas as pd
import plotly
import streamlit as st

books_df = pd.read_csv('bestsellers_with_categories_2022_03_27.csv')

st.title("Bestselling books analysis")
st.write("This is a streamlit app")


st.sidebar.header("Add new book data")
with st.sidebar.form("book_form"):
    new_name = st.text_input("Book Name")
    new_author = st.text_input("Author")
    new_user_rating = st.slider("User rating" , 0.0 , 5.0, 0.1)
    new_reviews = st.number_input("Reviews", min_value=0, step=1)
    new_price = st.number_input("Year", min_value=2009, max_value=2026)
    new_genre = st.selectbox("Genre", books_df['Genre'].unique())
    submit_button = st.form_submit_button(label="Add Book")



if submit_button:
    new_data ={
    'Name': new_name,
    'Author': new_author,
    'User Rating': new_user_raing,
    'Reviews': new_reviews,
    'Price': new_price,
    'Year': new_year,
    'Ganre': new_genre

    }

    books_df= pd.concat([pd.DataFrame(New_data, index[0]), books_df] , ignore_index=True)
    books_df.to_csv('bestsellers_with_categories_2022_03_27.csv' , index=False)
    st.sidebar.succsess("new books aded")


st.sidebar.header("Filter Options")
selected_author = st.sidebar.selectbox("Select Author" , ["All"] + list(books_df['Author'].unique()))
selected_year = st.sidebar.selectbox("Select Year" , ["All"] + list(books_df['Year'].unique()))
selected_ganre = st.sidebar.selectbox("Select Ganre" , ["All"] + list(books_df['Ganre'].unique()))
min_rating = st.sidebar.slider("Maximum user rating", 0.0, 5.0, 0.1)
max_price = st.sidebar.slider("Max Price" , 0, books_df['Price'].max(), books_df['Price'].max())
