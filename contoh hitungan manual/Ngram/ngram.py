from nltk.tokenize import TweetTokenizer
import re
from nltk.util import ngrams

delimiter = ["atau"]

def token(kata, delimiter = delimiter):
    # kata = re.sub(r'[^a-zA-Z0-9\s]', ' ', kata)
    # print()
    delimiter = list(set(["dan"]+delimiter))
    pointer = 0
    hasil_token = list()
    deli = list()   
    for i, huruf in enumerate(kata):
        if huruf in delimiter:
            deli.append(i)
    for i in deli:
        h = kata[pointer:i]
        pointer = i+1
        hasil_token.append(h)
    h = kata[pointer:]
    hasil_token.append(h)
    return hasil_token

def token_kata (kata, delimiter = delimiter):
    tknzr = TweetTokenizer(strip_handles=True, reduce_len=True)
    t_kata = tknzr.tokenize(kata)
    return token(t_kata, delimiter = delimiter)

def ngram (s, n):
    output = ngrams(s, n)
    n=list()
    for i in output:
        n.append("_".join(i))
    return n

def token_kata (kata, delimiter = delimiter):
    tknzr = TweetTokenizer(strip_handles=True, reduce_len=True)
    t_kata = tknzr.tokenize(kata)
    return token(t_kata, delimiter = delimiter)

def ngramku(kata, n=10, delimiter = delimiter):
    token_ = token_kata (kata, delimiter = delimiter)
    # print(token_)
    new_list = list()

    for i in token_:
        # print(i)
        if n==1:
            # ix = " ".join(i)
            ix = ngram (i, n)
            new_list.append(i+ix)
        else:
            ix = list()
            # ix_join = " ".join(i)
            ix_join = list()
            
            for loop in range(2,n+1):
                # print(ix_join)
                ix += ngram (i, loop)
            new_list.append(" ".join(i+ix))
    # return new_list
    return {"token":" ".join(new_list).split(), "string":" ".join(new_list)}
              
