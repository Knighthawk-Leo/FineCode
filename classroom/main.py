# TfidVectorizer to perform word embedding on data.
# cosine similarity to compute the Plagiarism.
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Reading all ".cpp" files and to load all the path ".cpp" files on project directory.
files = [doc for doc in 'media/classroom/resources/' if doc.endswith('.py')]
fileStore = [open(_file, encoding='utf-8').read()
                 for _file in files]

# Compute similarity between them.
def vectorize(Data): return TfidfVectorizer().fit_transform(Data).toarray()
def similarity(code_1, code_2): return cosine_similarity([code_1, code_2])

# Vectorize the data.
vectors = vectorize(fileStore)
s_vectors = list(zip(files, vectors))
plagiarismResults = set()

# Creating function to Compute similarity.
def PlagiarismChecker():
    global s_vectors
    for file_1, file_vector_1 in s_vectors:
        new_vectors = s_vectors.copy()
        current_index = new_vectors.index((file_1, file_vector_1))
        del new_vectors[current_index]
        for file_2, file_vector_2 in new_vectors:
            sim_score = similarity(file_vector_1, file_vector_2)[0][1]
            file_pair = sorted((file_1, file_2))
            score = (file_pair[0], file_pair[1], sim_score)
            plagiarismResults.add(score)
    return plagiarismResults


for data in PlagiarismChecker():
    print(data)
