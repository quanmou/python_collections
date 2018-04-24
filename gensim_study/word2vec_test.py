from gensim.models import word2vec
import gensim

sentences = word2vec.Text8Corpus('words_set.txt')
model = word2vec.Word2Vec(sentences, size=50)

print(model['季后赛'])
print(model['主场'])
print(model.similarity('季后赛', '主场'))

for i in model.most_similar("男篮"):
    print(i[0], i[1])

print(model.doesnt_match("中超 俱乐部 小组赛 跳投 破门".split()))

model.save('sports_word2vec_model')
new_model1 = gensim.models.Word2Vec.load('sports_word2vec_model')

# model.save_word2vec_format('sports_word2vec_model.bin', binary=True)  # Decrepit, use model.wv.save_word2vec_format
# new_model2 = gensim.models.Word2Vec.load_word2vec_format('sports_word2vec_model.bin', binary=True)  # Decrepit

model.wv.save_word2vec_format('sports_word2vec_model.bin', binary=True)
new_model3 = gensim.models.KeyedVectors.load_word2vec_format('sports_word2vec_model.bin', binary=True)
