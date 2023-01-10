Python 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import nltk
from nltk.tokenize import word_tokenize
s = """A lot of the data that you could be analyzing is unstructured data and contains human-readable text. Before you can analyze that data programmatically, you first need to preprocess it. In this tutorial, you’ll take your first look at the kinds of text preprocessing tasks you can do with NLTK so that you’ll be ready to apply them in future projects. You’ll also see how to do some basic text analysis and create visualizations."""
s_words=word_tokenize(s)
s_words
['A', 'lot', 'of', 'the', 'data', 'that', 'you', 'could', 'be', 'analyzing', 'is', 'unstructured', 'data', 'and', 'contains', 'human-readable', 'text', '.', 'Before', 'you', 'can', 'analyze', 'that', 'data', 'programmatically', ',', 'you', 'first', 'need', 'to', 'preprocess', 'it', '.', 'In', 'this', 'tutorial', ',', 'you', '’', 'll', 'take', 'your', 'first', 'look', 'at', 'the', 'kinds', 'of', 'text', 'preprocessing', 'tasks', 'you', 'can', 'do', 'with', 'NLTK', 'so', 'that', 'you', '’', 'll', 'be', 'ready', 'to', 'apply', 'them', 'in', 'future', 'projects', '.', 'You', '’', 'll', 'also', 'see', 'how', 'to', 'do', 'some', 'basic', 'text', 'analysis', 'and', 'create', 'visualizations', '.']
s_pos_tags = nltk.pos_tag(s_words)
s_pos_tags
[('A', 'DT'), ('lot', 'NN'), ('of', 'IN'), ('the', 'DT'), ('data', 'NNS'), ('that', 'IN'), ('you', 'PRP'), ('could', 'MD'), ('be', 'VB'), ('analyzing', 'VBG'), ('is', 'VBZ'), ('unstructured', 'VBN'), ('data', 'NNS'), ('and', 'CC'), ('contains', 'VBZ'), ('human-readable', 'JJ'), ('text', 'NN'), ('.', '.'), ('Before', 'IN'), ('you', 'PRP'), ('can', 'MD'), ('analyze', 'VB'), ('that', 'DT'), ('data', 'NN'), ('programmatically', 'RB'), (',', ','), ('you', 'PRP'), ('first', 'RB'), ('need', 'VB'), ('to', 'TO'), ('preprocess', 'VB'), ('it', 'PRP'), ('.', '.'), ('In', 'IN'), ('this', 'DT'), ('tutorial', 'JJ'), (',', ','), ('you', 'PRP'), ('’', 'VBP'), ('ll', 'JJ'), ('take', 'VB'), ('your', 'PRP$'), ('first', 'JJ'), ('look', 'NN'), ('at', 'IN'), ('the', 'DT'), ('kinds', 'NNS'), ('of', 'IN'), ('text', 'JJ'), ('preprocessing', 'NN'), ('tasks', 'NNS'), ('you', 'PRP'), ('can', 'MD'), ('do', 'VB'), ('with', 'IN'), ('NLTK', 'NNP'), ('so', 'IN'), ('that', 'IN'), ('you', 'PRP'), ('’', 'VBP'), ('ll', 'JJ'), ('be', 'VB'), ('ready', 'JJ'), ('to', 'TO'), ('apply', 'VB'), ('them', 'PRP'), ('in', 'IN'), ('future', 'JJ'), ('projects', 'NNS'), ('.', '.'), ('You', 'PRP'), ('’', 'VBP'), ('ll', 'NNS'), ('also', 'RB'), ('see', 'VBP'), ('how', 'WRB'), ('to', 'TO'), ('do', 'VB'), ('some', 'DT'), ('basic', 'JJ'), ('text', 'NN'), ('analysis', 'NN'), ('and', 'CC'), ('create', 'NN'), ('visualizations', 'NNS'), ('.', '.')]
chunk = "NP: {<DT>?<JJ>*<NN>}"
chunk
'NP: {<DT>?<JJ>*<NN>}'
chunk_parser = nltk.RegexpParser(chunk)
tree = chunk_parser.parse(s_pos_tags)
tree.draw()
tree.draw()
