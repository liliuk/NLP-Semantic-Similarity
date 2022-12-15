import spacy
nlp = spacy.load('en_core_web_md')

word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")

print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

## The results are as below:
## 0.5929930274321619
## 0.40415016164997786
## 0.22358825939615987
## It looks like cat and monkey have a lot of similarities as they are all animals. Monkey and banana have good similarities as I assume
## monkey eats banana. Cat and monkey have relative low similarities in the result.

## my own example
nlp = spacy.load('en_core_web_md')
object1 = nlp("table")
object2 = nlp("chair")
object3 = nlp("sofa")

print(object1.similarity(object2))
print(object3.similarity(object2))
print(object3.similarity(object1))

## The results are as below:
## 0.36323745282276176
## 0.5212732511738039
## 0.4168790721338001
## It seems that chair and sofa has the highest similarities, followed by table and sofa,
## and the pair which has the lowest similarity is table and chair.I am a bit surprised to be honest as I thought
## table and chair would have the most similarities. 

nlp = spacy.load('en_core_web_sm')
object1 = nlp("table")
object2 = nlp("chair")
object3 = nlp("sofa")

print(object1.similarity(object2))
print(object3.similarity(object2))
print(object3.similarity(object1))

## The results are as below:
## 0.7293916689220075
## 0.356513631335813
## 0.28756571292223343
## It's very interesting that the results from this is more in line with my expectations as table and chair has the highest similarites,
## followed by chair and sofa, and the pair which has the lowest similarities are table and sofa.
## The below warning appeared when 'en_core_web_sm' is used to do the similarity comparision.
## UserWarning: [W007] The model you're using has no word vectors loaded, so the result of the Doc.similarity method will 
## be based on the tagger, parser and NER, which may not give useful similarity judgements. 
## This may happen if you're using one of the small models, e.g. `en_core_web_sm`, 
## which don't ship with word vectors and only use context-sensitive tensors. 
## You can always add your own word vectors, or use one of the larger models instead if available.