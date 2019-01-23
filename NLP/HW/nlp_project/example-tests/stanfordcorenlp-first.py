''' stanfordcorenlp by Lynten Guo. 
    A Python wrapper to Stanford CoreNLP server, version 3.9.1. PyPI page: 
    pip install stanfordcorenlp
    https://github.com/Lynten/stanford-corenlp
'''
import pprint

# Simple usage
from stanfordcorenlp import StanfordCoreNLP

pp = pprint.PrettyPrinter(indent=2)

nlp = StanfordCoreNLP(r'/home/elvex/Templates/stanford-corenlp-full-2018-10-05')

sentence = 'Clean the kitchen at 5pm every Monday.'
#'Guangdong University of Foreign Studies is located in Guangzhou.'

print('Tokenize:')
pp.pprint(nlp.word_tokenize(sentence))

print('Part of Speech:')
pp.pprint(nlp.pos_tag(sentence))

print('Named Entities:')
pp.pprint(nlp.ner(sentence))

print('Constituency Parsing:')
pp.pprint(nlp.parse(sentence))

print('Dependency Parsing:')
pp.pprint(nlp.dependency_parse(sentence))


nlp.close() # Do not forget to close! The backend server will consume a lot memery.

''' OUT
elvex@solaria:~/Documents/mycode/npl$ python ./stanfordcorenlp-first.py 
Tokenize:
[ u'Guangdong',
  u'University',
  u'of',
  u'Foreign',
  u'Studies',
  u'is',
  u'located',
  u'in',
  u'Guangzhou',
  u'.']
Part of Speech:
[ (u'Guangdong', u'NNP'),
  (u'University', u'NNP'),
  (u'of', u'IN'),
  (u'Foreign', u'NNP'),
  (u'Studies', u'NNPS'),
  (u'is', u'VBZ'),
  (u'located', u'JJ'),
  (u'in', u'IN'),
  (u'Guangzhou', u'NNP'),
  (u'.', u'.')]
Named Entities:
[ (u'Guangdong', u'ORGANIZATION'),
  (u'University', u'ORGANIZATION'),
  (u'of', u'ORGANIZATION'),
  (u'Foreign', u'ORGANIZATION'),
  (u'Studies', u'ORGANIZATION'),
  (u'is', u'O'),
  (u'located', u'O'),
  (u'in', u'O'),
  (u'Guangzhou', u'CITY'),
  (u'.', u'O')]
Constituency Parsing:
u'(ROOT\n  
    (S\n
        (NP\n      
            (NP (NNP Guangdong) (NNP University))\n      
            (PP (IN of)\n   
                (NP (NNP Foreign) (NNPS Studies)))
        )\n    
        (VP 
            (VBZ is)\n      
            (ADJP (JJ located)\n        
                  (PP (IN in)\n     
                  (NP (NNP Guangzhou)))))\n    (. .)))'
Dependency Parsing:
[ (u'ROOT', 0, 7),
  (u'compound', 2, 1),
  (u'nsubjpass', 7, 2),
  (u'case', 5, 3),
  (u'compound', 5, 4),
  (u'nmod', 2, 5),
  (u'auxpass', 7, 6),
  (u'case', 9, 8),
  (u'nmod', 7, 9),
  (u'punct', 7, 10)]
'''
