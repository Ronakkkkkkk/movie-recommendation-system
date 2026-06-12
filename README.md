# THE VAULT - Movie Recommendation System

A movie recommendation platform that combines TF-IDF based content filtering with live TMDB metadata to help users discover movies similar to their favorites.

The application consists of a Streamlit frontend and a FastAPI backend, providing a clean user experience and fast recommendation APIs.

---

## Overview

THE VAULT uses content-based filtering to generate movie recommendations. It leverages a locally trained TF-IDF model for similarity matching and enriches results with movie metadata fetched from TMDB.

Features include:

* Movie search powered by TMDB
* TF-IDF content-based recommendations
* Genre-based recommendations
* Detailed movie information pages
* Modern Streamlit interface
* FastAPI backend with REST endpoints
* Live movie posters, genres, release dates, and descriptions

---

## Architecture

```text
┌─────────────────┐
│   Streamlit UI  │
└────────┬────────┘
         │ HTTP Requests
         ▼
┌─────────────────┐
│   FastAPI API   │
└────────┬────────┘
         │
 ┌───────┴────────┐
 │                │
 ▼                ▼
TF-IDF Model    TMDB API
(Local Data)   (Live Data)
```

---

## Tech Stack

### Frontend

* Streamlit

### Backend

* FastAPI
* Uvicorn

### Machine Learning

* Scikit-Learn
* TF-IDF Vectorization
* Cosine Similarity

### Data Processing

* Pandas
* NumPy
* SciPy

### External Services

* TMDB API

---

## Project Structure

```text
movie-recommendation-system/
│
├── app.py
├── main.py
├── requirements.txt
│
├── df.pkl
├── indices.pkl
├── tfidf.pkl
├── tfidf_matrix.pkl
│
├── .env
└── README.md
```

---

## How It Works

1. Movie metadata is processed and transformed into TF-IDF vectors.
2. Cosine similarity is used to measure similarity between movies.
3. Similar movies are ranked based on similarity scores.
4. TMDB is used to fetch:

   * Posters
   * Genres
   * Release dates
   * Overviews
5. Recommendations are displayed through the Streamlit interface.

---

## Installation

### Clone the Repository

```bash
git clone https://github.com/Ronakkkkkkk/movie-recommendation-system.git

cd movie-recommendation-system
```

### Create a Virtual Environment

```bash
python -m venv venv
```

### Activate the Environment

Windows:

```bash
venv\Scripts\activate
```

Linux/macOS:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the project root:

```env
TMDB_API_KEY=your_tmdb_api_key
```

Get your API key from TMDB.

---

## Running the Backend

Start the FastAPI server:

```bash
uvicorn main:app --reload
```

Backend URL:

```text
http://127.0.0.1:8000
```

API Documentation:

```text
http://127.0.0.1:8000/docs
```

---

## Running the Frontend

In a separate terminal:

```bash
streamlit run app.py
```

Frontend URL:

```text
http://localhost:8501
```

---

## API Endpoints

| Endpoint           | Description                    |
| ------------------ | ------------------------------ |
| `/health`          | Health check                   |
| `/home`            | Home page movie feed           |
| `/tmdb/search`     | Search movies from TMDB        |
| `/movie/id/{id}`   | Get movie details              |
| `/recommend/tfidf` | TF-IDF recommendations         |
| `/recommend/genre` | Genre recommendations          |
| `/movie/search`    | Combined recommendation bundle |

---

## Dataset

Movie recommendations are generated using a locally processed movie metadata dataset and TF-IDF vectorization.

The model computes cosine similarity between movie vectors to identify related titles.

TMDB is used for fetching live movie metadata, posters, genres, release dates, and overviews.

---

## Live Demo

https://the-vault.streamlit.app

---

## Author

Ronak Sharma

GitHub:
https://github.com/Ronakkkkkkk
