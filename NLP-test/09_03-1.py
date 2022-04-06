import gensim
import urllib.request

# 구글의 사전 훈련된 Word2Vec 모델을 로드.
# urllib.request.urlretrieve("https://s3.amazonaws.com/dl4j-distribution/GoogleNews-vectors-negative300.bin.gz", \
#                            filename="GoogleNews-vectors-negative300.bin.gz")
word2vec_model = gensim.models.KeyedVectors.load_word2vec_format('/home/song/git/gasang/GoogleNews-vectors-negative300.bin.gz', binary=True)

print(word2vec_model.vectors.shape)

print(word2vec_model.similarity('this', 'is'))
print(word2vec_model.similarity('post', 'book'))

print(word2vec_model['book'])






































