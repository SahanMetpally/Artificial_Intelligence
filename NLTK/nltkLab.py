# -*- coding: utf-8 -*-
import nltk

# =============================================================================
# from nltk.corpus import state_union
# 
# for fileid in state_union.fileids():
#     men = 0;
#     women = 0;
#     people = 0;
#     for t in state_union.words(fileid):
#         if t.lower() == "men":
#             men += 1
#         elif t.lower() == "women":
#             women += 1
#         elif t.lower() == "people":
#             people += 1
#     print(fileid + ":   men: " + str(men) + "    women: " + str(women) + "    people: "+ str(people))
#                 
# =============================================================================


# =============================================================================
# import nltk
# nltk.download('wordnet')
# 
# from nltk.corpus import wordnet as wn
# def relations(noun):
#     noun_synset = wn.synset(noun)
#     print('Member Meronyms:\n ')
#     print(noun_synset.member_meronyms())
#     print('\nPart Meronyms:\n')
#     print(noun_synset.part_meronyms())
#     print('\nSubstance Meronyms:\n')
#     print(noun_synset.substance_meronyms())
#     print('\nMember Holonyms:\n')
#     print(noun_synset.member_holonyms())
#     print('\nPart Holonyms:\n')
#     print(noun_synset.part_holonyms())
#     print('\nSubstance Holonyms:\n')
#     print(noun_synset.substance_holonyms())
# relations('tree.n.01')
# =============================================================================

# =============================================================================
# nltk.download('gutenberg')
# emma = nltk.Text(nltk.corpus.gutenberg.words('austen-emma.txt'))
# emma.concordance('however')
# =============================================================================

# =============================================================================
# nltk.download('gutenberg')
# nltk.download('state_union')
# 
# g = nltk.Text(nltk.corpus.gutenberg.words('austen-emma.txt'))
# s = nltk.Text(nltk.corpus.state_union.words('1945-Truman.txt'))
# 
# print(g.concordance('life'))
# =============================================================================

# =============================================================================
# nltk.download('cmudict')
# count_distinct = 0
# dublettes = []
# prev = ''
# for entry in nltk.corpus.cmudict.entries():
#     if ((entry[0] == prev) and (entry[0] not in dublettes)):
#         dublettes.append(entry[0])
#     else: 
#         count_distinct = count_distinct + 1
#         prev = entry[0]
# print(count_distinct)
# print((len(dublettes) / count_distinct) * 100)
# =============================================================================

# =============================================================================
# nltk.download('stopwords')
# emma = nltk.Text(nltk.corpus.state_union.words('1945-Truman.txt'))
# =============================================================================
# =============================================================================
# def most_frequent_content_words(text):
#     stopwords = nltk.corpus.stopwords.words('english')
#     content_words = [w.lower() for w in text if w.lower() not in stopwords and any(c.isalpha() for c in w)]
#     fd = nltk.FreqDist(content_words)
#     return [w for w, num in fd.most_common(50)]
# print(most_frequent_content_words(emma))
# =============================================================================

# =============================================================================
# def most_frequent_bigrams(text):
#     stopwords = nltk.corpus.stopwords.words('english')
#     bigrams = [b for b in nltk.bigrams(text) if b[0] not in stopwords and b[1] not in stopwords and any(c.isalpha() for c in b[0]) and any(c.isalpha() for c in b[1])]
#     fd = nltk.FreqDist(bigrams)
#     return [b for b, num in fd.most_common(50)]
# 
# print(most_frequent_bigrams(emma))
# =============================================================================

# =============================================================================
# nltk.download('wordnet')
# 
# from nltk.corpus import wordnet as wn
# def average_polysemy(category):
#     seen_words = []
#     num_poly = 0
#     sum_poly = 0
#     for synset in wn.all_synsets(category):
#         if num_poly > 20000:
#             break;
#         for lemma in synset.lemmas():
#             lemma_name = lemma.name()
#             if lemma_name not in seen_words:
#                 seen_words.append(lemma_name)
#                 num_poly = num_poly + 1
#                 sum_poly = sum_poly + len(wn.synsets(lemma_name, category))
#     return sum_poly / num_poly
# 
# print(average_polysemy('r'))
# =============================================================================

# =============================================================================
# import urllib
# import BeautifulSoup
# import re
# 
# def find_topic(url, trigger):
#     text = urllib.urlopen(url).read()
#     index = text.rfind(trigger)
#     text = text[index:]
#     title_with_markup = re.findall(r'\<b\>.+?\<\/b\>', text)[0]
#     soup = BeautifulSoup(title_with_markup)
#     return soup.get_text()
# =============================================================================

import random

nltk.download('movie_reviews')
from nltk.corpus import movie_reviews
documents = [(list(movie_reviews.words(fileid)), category) for category in movie_reviews.categories() for fileid in movie_reviews.fileids(category)]
random.shuffle(documents)

all_words = nltk.FreqDist(w.lower() for w in movie_reviews.words())
word_features = all_words.keys()[:2000]
def document_features(document):
    document_words = set(document)
    features = {}
    for word in word_features:
        features['contains(%s)' % word] = (word in document_words)
    return features

featuresets = [(document_features(d), c) for (d,c) in documents]
train_set, test_set = featuresets[100:], featuresets[:100]
classifier = nltk.NaiveBayesClassifier.train(train_set)
print(nltk.classify.accuracy(classifier, test_set))
classifier.show_most_informative_features(30)


















