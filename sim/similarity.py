#import sklearn
from sklearn.feature_extraction.text import TfidfVectorizer

# adapted from http://stackoverflow.com/questions/8897593/similarity-between-two-text-documents
def file_text_similarity(text_files):
    files = [open(f) for f in text_files]
    doc_texts = [f.read() for f in files]
    return text_similarity(doc_texts)
        
    
def text_similarity(text_array):    
    #tfidf = sklearn.feature_extraction.text.TfidfVectorizer().fit_transform(text_array)
    tfidf = TfidfVectorizer().fit_transform(text_array)
    # no need to normalize since Vectorizer will return normalized tf-idf
    pairwise_similarity = tfidf * tfidf.T
    return pairwise_similarity