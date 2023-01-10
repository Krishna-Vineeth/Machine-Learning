Python 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import nltk
nltk.download("stopwords")
[nltk_data] Downloading package stopwords to
[nltk_data]     C:\Users\krish\AppData\Roaming\nltk_data...
[nltk_data]   Unzipping corpora\stopwords.zip.
True
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
s="Words are like the atoms of natural language. They’re the smallest unit of meaning that still makes sense on its own. Tokenizing your text by word allows you to identify words that come up particularly often. For example, if you were analyzing a group of job ads, then you might find that the word “Python” comes up often. That could suggest high demand for Python knowledge, but you’d need to look deeper to know more."
word_tokenize(s)
['Words', 'are', 'like', 'the', 'atoms', 'of', 'natural', 'language', '.', 'They', '’', 're', 'the', 'smallest', 'unit', 'of', 'meaning', 'that', 'still', 'makes', 'sense', 'on', 'its', 'own', '.', 'Tokenizing', 'your', 'text', 'by', 'word', 'allows', 'you', 'to', 'identify', 'words', 'that', 'come', 'up', 'particularly', 'often', '.', 'For', 'example', ',', 'if', 'you', 'were', 'analyzing', 'a', 'group', 'of', 'job', 'ads', ',', 'then', 'you', 'might', 'find', 'that', 'the', 'word', '“', 'Python', '”', 'comes', 'up', 'often', '.', 'That', 'could', 'suggest', 'high', 'demand', 'for', 'Python', 'knowledge', ',', 'but', 'you', '’', 'd', 'need', 'to', 'look', 'deeper', 'to', 'know', 'more', '.']
stop_words = set(stopwords.words("english"))
stop_words
{'into', 'shan', 'wasn', 'his', 'yours', "won't", 'but', 'through', 'she', 'themselves', 'myself', "you've", "you'll", 'if', 'nor', 'such', 'any', 'hers', 've', 'itself', 'mustn', 'while', 'as', "needn't", 'doing', 'just', 'because', "you'd", 'over', 'their', 'then', 'weren', 'haven', 'off', 'll', 's', 'isn', 'mightn', 'which', 'o', 'aren', 'here', 'my', 'few', 'himself', 'your', 'ain', 'no', 'theirs', 'whom', 'above', 'of', 'be', 'the', 'been', 'had', 'herself', 'd', 'who', 'out', 'only', 'other', "shan't", 'can', 'after', 'that', 'are', 'has', 'between', 'before', 'very', "you're", 'why', 'does', "weren't", 'is', 'what', 'all', 'shouldn', "should've", 'further', 'won', 'should', 'didn', 'now', 're', 'most', 'we', 'there', 'our', 'hadn', 'too', 'do', 'having', 'couldn', 'you', "mustn't", "it's", "don't", 'at', 'by', 'its', "isn't", 'these', 'wouldn', 'hasn', 'so', 'ourselves', 'until', 'about', 'm', 'y', "didn't", 'doesn', "hadn't", 'for', 'from', 'again', 'being', 'ours', 'them', 'under', 'once', 't', 'against', 'during', 'an', 'where', 'her', "hasn't", "that'll", 'a', "haven't", 'was', 'they', 'down', "shouldn't", "aren't", "mightn't", 'some', 'each', "she's", 'same', 'don', 'yourselves', "doesn't", 'i', 'it', 'own', "wouldn't", 'this', 'in', 'he', 'am', 'below', 'on', 'more', 'and', 'up', 'will', 'ma', 'yourself', 'when', "wasn't", 'both', 'needn', 'not', 'were', "couldn't", 'have', 'or', 'how', 'did', 'than', 'me', 'with', 'him', 'to', 'those'}
filtered_list=[]
s
'Words are like the atoms of natural language. They’re the smallest unit of meaning that still makes sense on its own. Tokenizing your text by word allows you to identify words that come up particularly often. For example, if you were analyzing a group of job ads, then you might find that the word “Python” comes up often. That could suggest high demand for Python knowledge, but you’d need to look deeper to know more.'
s_words=word_tokenize(s)
s_words
['Words', 'are', 'like', 'the', 'atoms', 'of', 'natural', 'language', '.', 'They', '’', 're', 'the', 'smallest', 'unit', 'of', 'meaning', 'that', 'still', 'makes', 'sense', 'on', 'its', 'own', '.', 'Tokenizing', 'your', 'text', 'by', 'word', 'allows', 'you', 'to', 'identify', 'words', 'that', 'come', 'up', 'particularly', 'often', '.', 'For', 'example', ',', 'if', 'you', 'were', 'analyzing', 'a', 'group', 'of', 'job', 'ads', ',', 'then', 'you', 'might', 'find', 'that', 'the', 'word', '“', 'Python', '”', 'comes', 'up', 'often', '.', 'That', 'could', 'suggest', 'high', 'demand', 'for', 'Python', 'knowledge', ',', 'but', 'you', '’', 'd', 'need', 'to', 'look', 'deeper', 'to', 'know', 'more', '.']
stop_words
{'into', 'shan', 'wasn', 'his', 'yours', "won't", 'but', 'through', 'she', 'themselves', 'myself', "you've", "you'll", 'if', 'nor', 'such', 'any', 'hers', 've', 'itself', 'mustn', 'while', 'as', "needn't", 'doing', 'just', 'because', "you'd", 'over', 'their', 'then', 'weren', 'haven', 'off', 'll', 's', 'isn', 'mightn', 'which', 'o', 'aren', 'here', 'my', 'few', 'himself', 'your', 'ain', 'no', 'theirs', 'whom', 'above', 'of', 'be', 'the', 'been', 'had', 'herself', 'd', 'who', 'out', 'only', 'other', "shan't", 'can', 'after', 'that', 'are', 'has', 'between', 'before', 'very', "you're", 'why', 'does', "weren't", 'is', 'what', 'all', 'shouldn', "should've", 'further', 'won', 'should', 'didn', 'now', 're', 'most', 'we', 'there', 'our', 'hadn', 'too', 'do', 'having', 'couldn', 'you', "mustn't", "it's", "don't", 'at', 'by', 'its', "isn't", 'these', 'wouldn', 'hasn', 'so', 'ourselves', 'until', 'about', 'm', 'y', "didn't", 'doesn', "hadn't", 'for', 'from', 'again', 'being', 'ours', 'them', 'under', 'once', 't', 'against', 'during', 'an', 'where', 'her', "hasn't", "that'll", 'a', "haven't", 'was', 'they', 'down', "shouldn't", "aren't", "mightn't", 'some', 'each', "she's", 'same', 'don', 'yourselves', "doesn't", 'i', 'it', 'own', "wouldn't", 'this', 'in', 'he', 'am', 'below', 'on', 'more', 'and', 'up', 'will', 'ma', 'yourself', 'when', "wasn't", 'both', 'needn', 'not', 'were', "couldn't", 'have', 'or', 'how', 'did', 'than', 'me', 'with', 'him', 'to', 'those'}
for word in s_words:
    if word.casefold() not in stop_words:
        filtered_list.append(word)

filtered_list
['Words', 'like', 'atoms', 'natural', 'language', '.', '’', 'smallest', 'unit', 'meaning', 'still', 'makes', 'sense', '.', 'Tokenizing', 'text', 'word', 'allows', 'identify', 'words', 'come', 'particularly', 'often', '.', 'example', ',', 'analyzing', 'group', 'job', 'ads', ',', 'might', 'find', 'word', '“', 'Python', '”', 'comes', 'often', '.', 'could', 'suggest', 'high', 'demand', 'Python', 'knowledge', ',', '’', 'need', 'look', 'deeper', 'know', '.']

# some words can be eliminated by the stop words so on required conditions we can modify the stopwords from source.