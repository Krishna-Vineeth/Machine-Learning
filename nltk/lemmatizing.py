Python 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import nltk
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
lemmatizer
<WordNetLemmatizer>
lemmatizer.lemmatize("gloves")
Traceback (most recent call last):
  File "C:\Users\krish\AppData\Roaming\Python\Python310\site-packages\nltk\corpus\util.py", line 83, in __load
    root = nltk.data.find("{}/{}".format(self.subdir, zip_name))
  File "C:\Users\krish\AppData\Roaming\Python\Python310\site-packages\nltk\data.py", line 585, in find
    raise LookupError(resource_not_found)
LookupError: 
**********************************************************************
  Resource [93mwordnet[0m not found.
  Please use the NLTK Downloader to obtain the resource:

  [31m>>> import nltk
  >>> nltk.download('wordnet')
  [0m
  For more information see: https://www.nltk.org/data.html

  Attempted to load [93mcorpora/wordnet.zip/wordnet/[0m

  Searched in:
    - 'C:\\Users\\krish/nltk_data'
    - 'C:\\Program Files\\Python310\\nltk_data'
    - 'C:\\Program Files\\Python310\\share\\nltk_data'
    - 'C:\\Program Files\\Python310\\lib\\nltk_data'
    - 'C:\\Users\\krish\\AppData\\Roaming\\nltk_data'
    - 'C:\\nltk_data'
    - 'D:\\nltk_data'
    - 'E:\\nltk_data'
**********************************************************************


During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    lemmatizer.lemmatize("gloves")
  File "C:\Users\krish\AppData\Roaming\Python\Python310\site-packages\nltk\stem\wordnet.py", line 38, in lemmatize
    lemmas = wordnet._morphy(word, pos)
  File "C:\Users\krish\AppData\Roaming\Python\Python310\site-packages\nltk\corpus\util.py", line 120, in __getattr__
    self.__load()
  File "C:\Users\krish\AppData\Roaming\Python\Python310\site-packages\nltk\corpus\util.py", line 85, in __load
    raise e
  File "C:\Users\krish\AppData\Roaming\Python\Python310\site-packages\nltk\corpus\util.py", line 80, in __load
    root = nltk.data.find("{}/{}".format(self.subdir, self.__name))
  File "C:\Users\krish\AppData\Roaming\Python\Python310\site-packages\nltk\data.py", line 585, in find
    raise LookupError(resource_not_found)
LookupError: 
**********************************************************************
  Resource [93mwordnet[0m not found.
  Please use the NLTK Downloader to obtain the resource:

  [31m>>> import nltk
  >>> nltk.download('wordnet')
  [0m
  For more information see: https://www.nltk.org/data.html

  Attempted to load [93mcorpora/wordnet[0m

  Searched in:
    - 'C:\\Users\\krish/nltk_data'
    - 'C:\\Program Files\\Python310\\nltk_data'
    - 'C:\\Program Files\\Python310\\share\\nltk_data'
    - 'C:\\Program Files\\Python310\\lib\\nltk_data'
    - 'C:\\Users\\krish\\AppData\\Roaming\\nltk_data'
    - 'C:\\nltk_data'
    - 'D:\\nltk_data'
    - 'E:\\nltk_data'
**********************************************************************

nltk.download('wordnet')
                                          
[nltk_data] Downloading package wordnet to
[nltk_data]     C:\Users\krish\AppData\Roaming\nltk_data...
[nltk_data]   Unzipping corpora\wordnet.zip.
True
lemmatizer.lemmatize("gloves")
                                          
'glove'
lemmatizer.lemmatize("working")
                                          
'working'
lemmatizer.lemmatize("structured")
                                          
'structured'
s="""By tokenizing, you can conveniently split up text by word or by sentence. This will allow you to work with smaller pieces of text that are still relatively coherent and meaningful even outside of the context of the rest of the text. It’s your first step in turning unstructured data into structured data, which is easier to analyze."""
                                          
from nltk.tokenize import word_tokenize
                                          
s_words=word_tokenize(s)
                                          
s_words
                                          
['By', 'tokenizing', ',', 'you', 'can', 'conveniently', 'split', 'up', 'text', 'by', 'word', 'or', 'by', 'sentence', '.', 'This', 'will', 'allow', 'you', 'to', 'work', 'with', 'smaller', 'pieces', 'of', 'text', 'that', 'are', 'still', 'relatively', 'coherent', 'and', 'meaningful', 'even', 'outside', 'of', 'the', 'context', 'of', 'the', 'rest', 'of', 'the', 'text', '.', 'It', '’', 's', 'your', 'first', 'step', 'in', 'turning', 'unstructured', 'data', 'into', 'structured', 'data', ',', 'which', 'is', 'easier', 'to', 'analyze', '.']
lemmatized_words = [lemmatizer.lemmatize(word) for word in s_words]
                                          
lemmatized_words
                                          
['By', 'tokenizing', ',', 'you', 'can', 'conveniently', 'split', 'up', 'text', 'by', 'word', 'or', 'by', 'sentence', '.', 'This', 'will', 'allow', 'you', 'to', 'work', 'with', 'smaller', 'piece', 'of', 'text', 'that', 'are', 'still', 'relatively', 'coherent', 'and', 'meaningful', 'even', 'outside', 'of', 'the', 'context', 'of', 'the', 'rest', 'of', 'the', 'text', '.', 'It', '’', 's', 'your', 'first', 'step', 'in', 'turning', 'unstructured', 'data', 'into', 'structured', 'data', ',', 'which', 'is', 'easier', 'to', 'analyze', '.']
lemmatizer.lemmatize("worst", pos="a")
                                          
'bad'
lemmatizer.lemmatize("worst")
                                          
'worst'
