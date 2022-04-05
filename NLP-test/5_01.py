# import numpy as np
# from numpy import dot
# from numpy.linalg import norm
#
# def cos_sim(A, B):
#   return dot(A, B)/(norm(A)*norm(B))
#
# doc1 = np.array([0,1,1,1])
# doc2 = np.array([1,0,1,1])
# doc3 = np.array([2,0,2,2])
#
# print('문서 1과 문서2의 유사도 :',cos_sim(doc1, doc2))
# print('문서 1과 문서3의 유사도 :',cos_sim(doc1, doc3))
# print('문서 2와 문서3의 유사도 :',cos_sim(doc2, doc3))
#

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

data = pd.read_csv('movies_metadata.csv', low_memory=False)
data.head(2)

data = data.head(20000)

print('overview 열의 결측값의 수:',data['overview'].isnull().sum())

data['overview'] = data['overview'].fillna('')


tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(data['overview'])
print('TF-IDF 행렬의 크기(shape) :',tfidf_matrix.shape)

cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
print('코사인 유사도 연산 결과 :',cosine_sim.shape)

title_to_index = dict(zip(data['title'], data.index))

# 영화 제목 Father of the Bride Part II의 인덱스를 리턴
idx = title_to_index['Father of the Bride Part II']
print(idx)

def get_recommendations(title, cosine_sim=cosine_sim):
    # 선택한 영화의 타이틀로부터 해당 영화의 인덱스를 받아온다.
    idx = title_to_index[title]

    # 해당 영화와 모든 영화와의 유사도를 가져온다.
    sim_scores = list(enumerate(cosine_sim[idx]))

    # 유사도에 따라 영화들을 정렬한다.
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # 가장 유사한 10개의 영화를 받아온다.
    sim_scores = sim_scores[1:11]

    # 가장 유사한 10개의 영화의 인덱스를 얻는다.
    movie_indices = [idx[0] for idx in sim_scores]

    # 가장 유사한 10개의 영화의 제목을 리턴한다.
    return data['title'].iloc[movie_indices]



print(get_recommendations('The Dark Knight Rises'))

