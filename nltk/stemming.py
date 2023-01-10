Python 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
stemmer = PorterStemmer()
s="""By tokenizing, you can conveniently split up text by word or by sentence. This will allow you to work with smaller pieces of text that are still relatively coherent and meaningful even outside of the context of the rest of the text. It’s your first step in turning unstructured data into structured data, which is easier to analyze."""
s_words = word_tokenize(s)
s_words
['By', 'tokenizing', ',', 'you', 'can', 'conveniently', 'split', 'up', 'text', 'by', 'word', 'or', 'by', 'sentence', '.', 'This', 'will', 'allow', 'you', 'to', 'work', 'with', 'smaller', 'pieces', 'of', 'text', 'that', 'are', 'still', 'relatively', 'coherent', 'and', 'meaningful', 'even', 'outside', 'of', 'the', 'context', 'of', 'the', 'rest', 'of', 'the', 'text', '.', 'It', '’', 's', 'your', 'first', 'step', 'in', 'turning', 'unstructured', 'data', 'into', 'structured', 'data', ',', 'which', 'is', 'easier', 'to', 'analyze', '.']
stemmed_words = [stemmer.stem(word) for word in words]
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    stemmed_words = [stemmer.stem(word) for word in words]
NameError: name 'words' is not defined. Did you mean: 's_words'?
stemmed_words = [stemmer.stem(word) for word in s_words]
stemmed_words
['By', 'token', ',', 'you', 'can', 'conveni', 'split', 'up', 'text', 'by', 'word', 'or', 'by', 'sentenc', '.', 'thi', 'will', 'allow', 'you', 'to', 'work', 'with', 'smaller', 'piec', 'of', 'text', 'that', 'are', 'still', 'rel', 'coher', 'and', 'meaning', 'even', 'outsid', 'of', 'the', 'context', 'of', 'the', 'rest', 'of', 'the', 'text', '.', 'It', '’', 's', 'your', 'first', 'step', 'in', 'turn', 'unstructur', 'data', 'into', 'structur', 'data', ',', 'which', 'is', 'easier', 'to', 'analyz', '.']
