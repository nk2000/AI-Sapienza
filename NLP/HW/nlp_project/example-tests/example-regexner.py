
import pprint
import json

from stanfordcorenlp import StanfordCoreNLP

pp = pprint.PrettyPrinter(indent=2)


nlp = StanfordCoreNLP(r'/home/elvex/Templates/stanford-corenlp-full-2018-10-05')

res = nlp.annotate("Clean the kitchen.",
                   properties={
                       'annotators': 'regexner',
                       'outputFormat': 'json',
                       'regexner.mapping': '/home/elvex/Documents/mycode/npl/regexner.txt',
                       'timeout': 1000,
                   })

# Test
# print res

out = json.loads(res)

pp.pprint(out)
