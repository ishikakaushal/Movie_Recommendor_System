import streamlit as st
import pickle
import pandas as pd
import requests
import time
import gzip

# ----------------------------
# 🎨 Page Config
# ----------------------------
st.set_page_config(page_title="🎬 Movie Recommender", layout="wide")

# ----------------------------
# 🌙 Custom Netflix Style Theme
# ----------------------------
st.markdown("""
    <style>
    .stApp {
        background-color: #141414;
        color: white;
    }
    h1, h2, h3, h4, h5, h6,label,p {
        color: white !important;
    }
    div{
    color: red;}
    img {
        border-radius: 12px;
        transition: transform 0.3s;
    }
    img:hover {
        transform: scale(1.05);
    }
    /* 🔴 Netflix Style Button */
    div.stButton > button:first-child {
        background-color: #E50914;
        color: white;
        border: none;
        padding: 0.6em 1.2em;
        border-radius: 8px;
        font-weight: bold;
        font-size: 16px;
        transition: all 0.3s;
    }
    div.stButton > button:hover {
        background-color: #b00610;
        transform: scale(1.03);
    }
    </style>
""", unsafe_allow_html=True)

# ----------------------------
# 🎞️ Fetch Poster Function (with strong fallback)
# ----------------------------
def fetch_poster(movie_id):
    api_key = "e56e0faccf88695332f536629114b67e"  # your TMDB API key
    base_url = "https://api.themoviedb.org/3/movie"
    fallback = "https://via.placeholder.com/500x750?text=Poster+Not+Available"

    for attempt in range(3):  # try up to 3 times
        try:
            url = f"{base_url}/{movie_id}?api_key={api_key}&language=en-US"
            response = requests.get(url, timeout=5)
            response.raise_for_status()
            data = response.json()

            poster_path = data.get("poster_path")
            if poster_path:
                full_url = f"https://image.tmdb.org/t/p/w500/{poster_path}"
                # check if image link actually exists
                img_check = requests.head(full_url)
                if img_check.status_code == 200:
                    return full_url
            # If no poster or invalid response
            return fallback
        except Exception as e:
            print(f"⚠️ API Error (Attempt {attempt + 1}): {e}")
            time.sleep(1)
    return fallback

# ----------------------------
# 🧠 Recommend Function
# ----------------------------
def recommend(movie):
    try:
        movie_index = movies[movies['title'] == movie].index[0]
    except IndexError:
        st.error("❌ Movie not found in database!")
        return [], []

    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), key=lambda x: x[1], reverse=True)[1:6]

    recommended_movies = []
    recommended_posters = []

    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_posters.append(fetch_poster(movie_id))

    return recommended_movies, recommended_posters

# ----------------------------
# 📦 Load Data
# ----------------------------
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
with gzip.open('similarity.pkl.gz', 'rb') as f:
    similarity = pickle.load(f)

# ----------------------------
# 🏠 App Layout
# ----------------------------
st.title("🎬 Movie Recommender System")

selected_movie_name = st.selectbox("Select a movie to get recommendations:", movies['title'].values)

if st.button('🍿 Show Recommendations'):
    with st.spinner('Fetching recommendations...'):
        names, posters = recommend(selected_movie_name)
        if names and posters:
            cols = st.columns(5)
            for idx, col in enumerate(cols):
                with col:
                    st.text(names[idx])
                    st.image(posters[idx], width='stretch')
        else:
            st.warning("No recommendations found!")

# ----------------------------
# ✅ Footer
# ----------------------------
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Made with ❤️ by Ishika Kaushal | Powered by TMDB API and Streamlit</p>", unsafe_allow_html=True)
