from json import load
from nltk.tokenize import TweetTokenizer
import re
import os
dir_path = os.path.dirname(os.path.realpath(__file__))
with open(dir_path+'/data.json', 'r') as f:
    data = load(f)

tknzr = TweetTokenizer()
def normalisasi (kalimat):
    kalimat = tknzr.tokenize(kalimat.lower())
    for i, k in enumerate(kalimat):
        if k in data['hapus']:
            kalimat[i] = ""
        elif k in data['ganti']:
            kalimat[i] = data['ganti'][k]
    kalimat = " ".join(kalimat)
    return re.sub(' +', ' ', kalimat.lstrip().rstrip())