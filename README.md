🎬 Movie Recommender System

A smart, modern, Netflix-style Movie Recommendation Web App built using Machine Learning + Streamlit.
It recommends movies based on similarity scores and fetches posters dynamically using TMDB API.

🚀 Live Website:
👉 https://movierecommendorsystem-llwtzhvz8w3okajt4jst8r.streamlit.app/

⭐ Features

✔ Beautiful Netflix-style dark theme
✔ Search movies using dropdown
✔ Get Top 5 recommended movies instantly
✔ Posters displayed in a single row
✔ Hover animations for posters
✔ Custom red Netflix-style buttons
✔ API error handling (poster not found, missing images, etc.)
✔ Fully deployed using Streamlit Cloud

🧠 Tech Stack
Frontend + Backend

Python

Streamlit (UI + deployment)

Pandas

Requests (for API calls)

Pickle (loading ML models)

Machine Learning

Content-based recommendation using:

Cosine similarity

Vectorized tags

Movie metadata

📦 Project Structure
|-- app.py
|-- movies.pkl
|-- similarity.pkl
|-- requirements.txt
|-- README.md

🖥 How It Works

User selects a movie from the dropdown

App finds its index in the dataset

Gets similarity scores for all movies

Sorts and selects top 5 most similar movies

Fetches posters using TMDB API

Displays all recommended posters in a row

🎨 UI / UX Design

Full dark Netflix-inspired theme

Custom CSS:

Red buttons

Poster hover zoom

Black containers

White text

Designed to look clean & stylish on Streamlit Cloud

🌐 Deployment (Streamlit Cloud)

Your app is deployed on Streamlit Cloud:

🔗 Live App:
https://movierecommendorsystem-llwtzhvz8w3okajt4jst8r.streamlit.app/

To deploy your own version:

Push code to GitHub

Visit: https://share.streamlit.io

Connect repository

Select app.py

Deploy!

🧪 How to Run Locally
pip install -r requirements.txt
streamlit run app.py

🧰 Requirements
streamlit
pandas
requests
pickle

👩‍💻 Author

Ishika Kaushal
A ML enthusiast & developer learning AI, ML, and web app deployment.

