import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
s="""Words are like the atoms of natural language. They’re the smallest unit of meaning that still makes sense on its own. Tokenizing your text by word allows you to identify words that come up particularly often. For example, if you were analyzing a group of job ads, then you might find that the word “Python” comes up often. That could suggest high demand for Python knowledge, but you’d need to look deeper to know more."""
sent_tokenize(s)

import nltk
nltk.download('punkt')
[nltk_data] Downloading package punkt to
[nltk_data]     C:\Users\krish\AppData\Roaming\nltk_data...
[nltk_data]   Unzipping tokenizers\punkt.zip.
True
sent_tokenize(s)
['Words are like the atoms of natural language.', 'They’re the smallest unit of meaning that still makes sense on its own.', 'Tokenizing your text by word allows you to identify words that come up particularly often.', 'For example, if you were analyzing a group of job ads, then you might find that the word “Python” comes up often.', 'That could suggest high demand for Python knowledge, but you’d need to look deeper to know more.']
word_tokenize(s)
['Words', 'are', 'like', 'the', 'atoms', 'of', 'natural', 'language', '.', 'They', '’', 're', 'the', 'smallest', 'unit', 'of', 'meaning', 'that', 'still', 'makes', 'sense', 'on', 'its', 'own', '.', 'Tokenizing', 'your', 'text', 'by', 'word', 'allows', 'you', 'to', 'identify', 'words', 'that', 'come', 'up', 'particularly', 'often', '.', 'For', 'example', ',', 'if', 'you', 'were', 'analyzing', 'a', 'group', 'of', 'job', 'ads', ',', 'then', 'you', 'might', 'find', 'that', 'the', 'word', '“', 'Python', '”', 'comes', 'up', 'often', '.', 'That', 'could', 'suggest', 'high', 'demand', 'for', 'Python', 'knowledge', ',', 'but', 'you', '’', 'd', 'need', 'to', 'look', 'deeper', 'to', 'know', 'more', '.']
s="vineeth's"
sent_tokenize(s)
["vineeth's"]
word_tokenize(s)
['vineeth', "'s"]
s="krishna'vineeth"
word_tokenize(s)
["krishna'vineeth"]
