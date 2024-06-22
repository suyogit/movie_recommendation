import streamlit as st
import pickle




similarity=pickle.load(open('similarity.pkl', 'rb'))
movies_df= pickle.load(open('movies.pkl', 'rb'))
movies_list= movies_df['title'].values

def  recommend(movie):
    movie_index=movies_df[movies_df['title']==movie].index[0]
    distances= similarity[movie_index]
    movies_list= sorted(list(enumerate(distances)),reverse=True, key=lambda x:x[1])[1:6]
    recommended_movies= []
    for i in movies_list:
        recommended_movies.append(movies_df.iloc[i[0]].title)

    return recommended_movies

st.title('Movie Recommendation System')
selected_movie= st.selectbox('Choose a movie',movies_list)



if st.button('Recommend'):
    recomendations=recommend(selected_movie)
    for i in recomendations:
        st.write(i)