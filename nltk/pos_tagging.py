Python 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import nltk
from nltk.tokenize import word_tokenize
s="""By tokenizing, you can conveniently split up text by word or by sentence. This will allow you to work with smaller pieces of text that are still relatively coherent and meaningful even outside of the context of the rest of the text. It’s your first step in turning unstructured data into structured data, which is easier to analyze."""
s_words=word_tokenize(s)
s_words
['By', 'tokenizing', ',', 'you', 'can', 'conveniently', 'split', 'up', 'text', 'by', 'word', 'or', 'by', 'sentence', '.', 'This', 'will', 'allow', 'you', 'to', 'work', 'with', 'smaller', 'pieces', 'of', 'text', 'that', 'are', 'still', 'relatively', 'coherent', 'and', 'meaningful', 'even', 'outside', 'of', 'the', 'context', 'of', 'the', 'rest', 'of', 'the', 'text', '.', 'It', '’', 's', 'your', 'first', 'step', 'in', 'turning', 'unstructured', 'data', 'into', 'structured', 'data', ',', 'which', 'is', 'easier', 'to', 'analyze', '.']
nltk.pos_tag(s_words)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    nltk.pos_tag(s_words)
  File "C:\Users\krish\AppData\Roaming\Python\Python310\site-packages\nltk\tag\__init__.py", line 160, in pos_tag
    tagger = _get_tagger(lang)
  File "C:\Users\krish\AppData\Roaming\Python\Python310\site-packages\nltk\tag\__init__.py", line 106, in _get_tagger
    tagger = PerceptronTagger()
  File "C:\Users\krish\AppData\Roaming\Python\Python310\site-packages\nltk\tag\perceptron.py", line 168, in __init__
    find("taggers/averaged_perceptron_tagger/" + PICKLE)
  File "C:\Users\krish\AppData\Roaming\Python\Python310\site-packages\nltk\data.py", line 585, in find
    raise LookupError(resource_not_found)
LookupError: 
**********************************************************************
  Resource [93maveraged_perceptron_tagger[0m not found.
  Please use the NLTK Downloader to obtain the resource:

  [31m>>> import nltk
  >>> nltk.download('averaged_perceptron_tagger')
  [0m
  For more information see: https://www.nltk.org/data.html

  Attempted to load [93mtaggers/averaged_perceptron_tagger/averaged_perceptron_tagger.pickle[0m

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

    nltk.download('averaged_perceptron_tagger')
                                                                                               
[nltk_data] Downloading package averaged_perceptron_tagger to
[nltk_data]     C:\Users\krish\AppData\Roaming\nltk_data...
[nltk_data]   Unzipping taggers\averaged_perceptron_tagger.zip.
True
nltk.pos_tag(s_words)
                                                                                               
[('By', 'IN'), ('tokenizing', 'VBG'), (',', ','), ('you', 'PRP'), ('can', 'MD'), ('conveniently', 'RB'), ('split', 'VB'), ('up', 'RP'), ('text', 'NN'), ('by', 'IN'), ('word', 'NN'), ('or', 'CC'), ('by', 'IN'), ('sentence', 'NN'), ('.', '.'), ('This', 'DT'), ('will', 'MD'), ('allow', 'VB'), ('you', 'PRP'), ('to', 'TO'), ('work', 'VB'), ('with', 'IN'), ('smaller', 'JJR'), ('pieces', 'NNS'), ('of', 'IN'), ('text', 'NN'), ('that', 'WDT'), ('are', 'VBP'), ('still', 'RB'), ('relatively', 'RB'), ('coherent', 'JJ'), ('and', 'CC'), ('meaningful', 'JJ'), ('even', 'RB'), ('outside', 'IN'), ('of', 'IN'), ('the', 'DT'), ('context', 'NN'), ('of', 'IN'), ('the', 'DT'), ('rest', 'NN'), ('of', 'IN'), ('the', 'DT'), ('text', 'NN'), ('.', '.'), ('It', 'PRP'), ('’', 'VBD'), ('s', 'VB'), ('your', 'PRP$'), ('first', 'JJ'), ('step', 'NN'), ('in', 'IN'), ('turning', 'VBG'), ('unstructured', 'JJ'), ('data', 'NNS'), ('into', 'IN'), ('structured', 'VBN'), ('data', 'NNS'), (',', ','), ('which', 'WDT'), ('is', 'VBZ'), ('easier', 'JJR'), ('to', 'TO'), ('analyze', 'VB'), ('.', '.')]
nltk.help.upenn_tagset()
                                                                                               
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    nltk.help.upenn_tagset()
  File "C:\Users\krish\AppData\Roaming\Python\Python310\site-packages\nltk\help.py", line 27, in upenn_tagset
    _format_tagset("upenn_tagset", tagpattern)
  File "C:\Users\krish\AppData\Roaming\Python\Python310\site-packages\nltk\help.py", line 46, in _format_tagset
    tagdict = load("help/tagsets/" + tagset + ".pickle")
  File "C:\Users\krish\AppData\Roaming\Python\Python310\site-packages\nltk\data.py", line 752, in load
    opened_resource = _open(resource_url)
  File "C:\Users\krish\AppData\Roaming\Python\Python310\site-packages\nltk\data.py", line 877, in _open
    return find(path_, path + [""]).open()
  File "C:\Users\krish\AppData\Roaming\Python\Python310\site-packages\nltk\data.py", line 585, in find
    raise LookupError(resource_not_found)
LookupError: 
**********************************************************************
  Resource [93mtagsets[0m not found.
  Please use the NLTK Downloader to obtain the resource:

  [31m>>> import nltk
  >>> nltk.download('tagsets')
  [0m
  For more information see: https://www.nltk.org/data.html

  Attempted to load [93mhelp/tagsets/upenn_tagset.pickle[0m

  Searched in:
    - 'C:\\Users\\krish/nltk_data'
    - 'C:\\Program Files\\Python310\\nltk_data'
    - 'C:\\Program Files\\Python310\\share\\nltk_data'
    - 'C:\\Program Files\\Python310\\lib\\nltk_data'
    - 'C:\\Users\\krish\\AppData\\Roaming\\nltk_data'
    - 'C:\\nltk_data'
    - 'D:\\nltk_data'
    - 'E:\\nltk_data'
    - ''
**********************************************************************

ntlk.download('tagsets')
                                                           
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    ntlk.download('tagsets')
NameError: name 'ntlk' is not defined
nltk.download('tagsets')
                                                           
[nltk_data] Downloading package tagsets to
[nltk_data]     C:\Users\krish\AppData\Roaming\nltk_data...
[nltk_data]   Unzipping help\tagsets.zip.
True
nltk.help.upenn_tagset()
                                                           
$: dollar
    $ -$ --$ A$ C$ HK$ M$ NZ$ S$ U.S.$ US$
'': closing quotation mark
    ' ''
(: opening parenthesis
    ( [ {
): closing parenthesis
    ) ] }
,: comma
    ,
--: dash
    --
.: sentence terminator
    . ! ?
:: colon or ellipsis
    : ; ...
CC: conjunction, coordinating
    & 'n and both but either et for less minus neither nor or plus so
    therefore times v. versus vs. whether yet
CD: numeral, cardinal
    mid-1890 nine-thirty forty-two one-tenth ten million 0.5 one forty-
    seven 1987 twenty '79 zero two 78-degrees eighty-four IX '60s .025
    fifteen 271,124 dozen quintillion DM2,000 ...
DT: determiner
    all an another any both del each either every half la many much nary
    neither no some such that the them these this those
EX: existential there
    there
FW: foreign word
    gemeinschaft hund ich jeux habeas Haementeria Herr K'ang-si vous
    lutihaw alai je jour objets salutaris fille quibusdam pas trop Monte
    terram fiche oui corporis ...
IN: preposition or conjunction, subordinating
    astride among uppon whether out inside pro despite on by throughout
    below within for towards near behind atop around if like until below
    next into if beside ...
JJ: adjective or numeral, ordinal
    third ill-mannered pre-war regrettable oiled calamitous first separable
    ectoplasmic battery-powered participatory fourth still-to-be-named
    multilingual multi-disciplinary ...
JJR: adjective, comparative
    bleaker braver breezier briefer brighter brisker broader bumper busier
    calmer cheaper choosier cleaner clearer closer colder commoner costlier
    cozier creamier crunchier cuter ...
JJS: adjective, superlative
    calmest cheapest choicest classiest cleanest clearest closest commonest
    corniest costliest crassest creepiest crudest cutest darkest deadliest
    dearest deepest densest dinkiest ...
LS: list item marker
    A A. B B. C C. D E F First G H I J K One SP-44001 SP-44002 SP-44005
    SP-44007 Second Third Three Two * a b c d first five four one six three
    two
MD: modal auxiliary
    can cannot could couldn't dare may might must need ought shall should
    shouldn't will would
NN: noun, common, singular or mass
    common-carrier cabbage knuckle-duster Casino afghan shed thermostat
    investment slide humour falloff slick wind hyena override subhumanity
    machinist ...
NNP: noun, proper, singular
    Motown Venneboerger Czestochwa Ranzer Conchita Trumplane Christos
    Oceanside Escobar Kreisler Sawyer Cougar Yvette Ervin ODI Darryl CTCA
    Shannon A.K.C. Meltex Liverpool ...
NNPS: noun, proper, plural
    Americans Americas Amharas Amityvilles Amusements Anarcho-Syndicalists
    Andalusians Andes Andruses Angels Animals Anthony Antilles Antiques
    Apache Apaches Apocrypha ...
NNS: noun, common, plural
    undergraduates scotches bric-a-brac products bodyguards facets coasts
    divestitures storehouses designs clubs fragrances averages
    subjectivists apprehensions muses factory-jobs ...
PDT: pre-determiner
    all both half many quite such sure this
POS: genitive marker
    ' 's
PRP: pronoun, personal
    hers herself him himself hisself it itself me myself one oneself ours
    ourselves ownself self she thee theirs them themselves they thou thy us
PRP$: pronoun, possessive
    her his mine my our ours their thy your
RB: adverb
    occasionally unabatingly maddeningly adventurously professedly
    stirringly prominently technologically magisterially predominately
    swiftly fiscally pitilessly ...
RBR: adverb, comparative
    further gloomier grander graver greater grimmer harder harsher
    healthier heavier higher however larger later leaner lengthier less-
    perfectly lesser lonelier longer louder lower more ...
RBS: adverb, superlative
    best biggest bluntest earliest farthest first furthest hardest
    heartiest highest largest least less most nearest second tightest worst
RP: particle
    aboard about across along apart around aside at away back before behind
    by crop down ever fast for forth from go high i.e. in into just later
    low more off on open out over per pie raising start teeth that through
    under unto up up-pp upon whole with you
SYM: symbol
    % & ' '' ''. ) ). * + ,. < = > @ A[fj] U.S U.S.S.R * ** ***
TO: "to" as preposition or infinitive marker
    to
UH: interjection
    Goodbye Goody Gosh Wow Jeepers Jee-sus Hubba Hey Kee-reist Oops amen
    huh howdy uh dammit whammo shucks heck anyways whodunnit honey golly
    man baby diddle hush sonuvabitch ...
VB: verb, base form
    ask assemble assess assign assume atone attention avoid bake balkanize
    bank begin behold believe bend benefit bevel beware bless boil bomb
    boost brace break bring broil brush build ...
VBD: verb, past tense
    dipped pleaded swiped regummed soaked tidied convened halted registered
    cushioned exacted snubbed strode aimed adopted belied figgered
    speculated wore appreciated contemplated ...
VBG: verb, present participle or gerund
    telegraphing stirring focusing angering judging stalling lactating
    hankerin' alleging veering capping approaching traveling besieging
    encrypting interrupting erasing wincing ...
VBN: verb, past participle
    multihulled dilapidated aerosolized chaired languished panelized used
    experimented flourished imitated reunifed factored condensed sheared
    unsettled primed dubbed desired ...
VBP: verb, present tense, not 3rd person singular
    predominate wrap resort sue twist spill cure lengthen brush terminate
    appear tend stray glisten obtain comprise detest tease attract
    emphasize mold postpone sever return wag ...
VBZ: verb, present tense, 3rd person singular
    bases reconstructs marks mixes displeases seals carps weaves snatches
    slumps stretches authorizes smolders pictures emerges stockpiles
    seduces fizzes uses bolsters slaps speaks pleads ...
WDT: WH-determiner
    that what whatever which whichever
WP: WH-pronoun
    that what whatever whatsoever which who whom whosoever
WP$: WH-pronoun, possessive
    whose
WRB: Wh-adverb
    how however whence whenever where whereby whereever wherein whereof why
``: opening quotation mark
    ` ``
