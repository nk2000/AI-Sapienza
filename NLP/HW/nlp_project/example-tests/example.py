
import json

from stanfordcorenlp import StanfordCoreNLP


nlp = StanfordCoreNLP(r'/home/elvex/Templates/stanford-corenlp-full-2018-10-05')

res = nlp.annotate("I love you. I hate him. You are nice. He is dumb",
                   properties={
                       #'annotators': 'relation',
                       'annotators': 'sentiment',
                       #'annotators': 'lemma, parse, truecase, depparse', 
                       #'annotators': 'tokenize, pos, ner, ssplit',
                       'outputFormat': 'json',
                       'timeout': 1000,
                   })


nlp.close()

# Test
# print res

out = json.loads(res)

for s in out["sentences"]:
    print("%d: '%s': %s %s" % (
        s["index"],
        " ".join([t["word"] for t in s["tokens"]]),
        s["sentimentValue"], s["sentiment"]))

# Output
# elvex@solaria:~/Documents/mycode/npl$ python ./example.py 
# 0: 'I love you .': 3 Positive
# 1: 'I hate him .': 1 Negative
# 2: 'You are nice .': 3 Positive
# 3: 'He is dumb': 1 Negative
