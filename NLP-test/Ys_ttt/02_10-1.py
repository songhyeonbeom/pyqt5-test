import urllib.request
from soynlp import DoublespaceLineCorpus
from soynlp.word import WordExtractor


# urllib.request.urlretrieve("https://raw.githubusercontent.com/lovit/soynlp/master/tutorials/2016-10-20.txt", filename="2016-10-20.txt")


corpus = DoublespaceLineCorpus("2016-10-20.txt")
len(corpus)

i = 0
for document in corpus:
  if len(document) > 0:
    print(document)
    i = i+1
  if i == 3:
    break

word_extractor = WordExtractor()
word_extractor.train(corpus)
word_score_table = word_extractor.extract()





















