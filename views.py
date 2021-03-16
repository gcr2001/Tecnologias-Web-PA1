from database import *
import urllib
from utils import load_data, load_template, append_to_notes, build_response, remove_from_notes, update_notes

def index(request):

    if request.startswith('POST'):
        request = request.replace('\r', '')
        partes = request.split('\n\n')
        corpo = partes[1]
        params = {}