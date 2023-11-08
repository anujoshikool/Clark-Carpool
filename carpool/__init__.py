import googlemaps
from dotenv import load_dotenv
import os 
load_dotenv()

GOOGLE_API = os.environ.get('AIzaSyDGorPQ3msilPH1SjABXCd6waoCQq2UKTA')
GAS_API = os.environ.get('GAS_API') 

gmaps = googlemaps.Client(key= 'AIzaSyDGorPQ3msilPH1SjABXCd6waoCQq2UKTA')



