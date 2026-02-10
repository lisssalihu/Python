import pandas as pd
import plotly
import streamlit as st
from streamlit import title

from Module18.app import total_books, unique_titles, average_price, top_titles

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
    'User Rating': new_user_rating,
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

filtered_books_df = books_df.copy()

if selected_author !="All":
    filtered_books_df = filtered_books_df[filtered_books_df['Author'] == selected_author]
if selected_year !="All":
    filtered_books_df = filtered_books_df[filtered_books_df['Year'] == selected_year]
if selected_ganre !="All":
    filtered_books_df = filtered_books_df[filtered_books_df['Genre'] == selected_author]

filtered_books_df = filtered_books_df[
    (filtered_books_df['User Rating']) >= min_rating) & (filtered_books_df['Price'] <= max_price)
]

st.subheader("Summary Statisctics")
total_books = filtered_books_df.shape[0]
unique_titles = filtered_books_df['User Rating'].mean()
average_price = filtered_books_df['Price'].mean()


col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Books", total_books)
col2.metric("Unique Titles", unique_titles)
col3.metric("Average Rating", average_rating)
col4.metric("Average Price", average_price)

st.subheader("Dataset Preview")
st.write(filtered_books_df.head())


col1, col2 = st.columns(2)

with col1:
    st.subheader("Top 10 selling books")
    top_titles = filtered_books_df['name'].value_counts().head(10)
    st.bar_chart(top_titles)
with col2:
    st.subheader("top 10 Authors")
    top_authors = filtered_books_df['Author'].value_counts().head(10)
    st.bar_chart(top_authors)

#Genre Distrubition Pie chart
st.subheader("Genre Distribution")
fig = px.pie(filtered_books_df, names='Genre', title='Most liked Genre (2009-2022)' color='Genre',
          color_discrete_sequence=px.colors.sequential.Plasma)
st.plotly_chart(fig)

st.subheader("Number od fiction vs Non-Fiction Books Over the Years")
size = filtered_books_df.groupby(['Year', 'Genre']).size().reset_index(name='Counts')
fig = px.bar(size, x='Year' ,y='Counts', color='Genre', title="Number of fiction vs Non fiction books from 2009-2022",
            color_discrete_sequence=px.colors.sequential.Plasma,


barmode='group')
st.plotly_chart(fig)


st.subheader("Top 15 authors by counts of books published (2009-2022")
top_authors = filtered_books_df['Authors'].value.counts().head(15).reset_index()
top_authors.columns = ['Author', 'Count']
fig = px.bar(top_authors, x='Count' , y='Author' , orientation='h'),
            title = 'Top 15 authors by counts of book published'
            label={'Count': 'Counts of books published' , 'Author': 'Author'},
            color = 'Count', color_continous_scale=px.colors.sequential.Plasma)
st.plotly_chart(fig)


st.subheader('Filter data by genre')
genre_filter = st.selectbox("Select genre", filtered_books_df['Genre'].unique())
filtered_books_df = filtered_books_df[filtered_books_df['Genre'] == genre_filter]
st.write(filtered_genre_df)
















