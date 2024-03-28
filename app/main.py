from fastapi import FastAPI
from transformers import pipeline
import requests


classifier = pipeline(
    model="lxyuan/distilbert-base-multilingual-cased-sentiments-student",
    return_all_scores=True
)

app = FastAPI()

params = {
    'placeid': 'XXX',
    'key': 'API_KEY',
    'fields': 'reviews',
    'language': 'ja'
}

GOOGLE_PLACES_URL = "https://maps.googleapis.com/maps/api/place/details/json"


@app.get("/")
async def root():
    return {'message': 'mindreader root'}
