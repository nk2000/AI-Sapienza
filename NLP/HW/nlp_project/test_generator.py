import pprint
import string
import signal
import sys

def signal_handler(sig, frame):
    print('\nOut! closing CoreNLP.')
    nlp.close()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

from stanfordcorenlp import StanfordCoreNLP

pp = pprint.PrettyPrinter(indent=2)

nlp = StanfordCoreNLP(r'/home/simone/Scrivania/stanford-corenlp-full-2018-10-05')

rooms_test = ["clean the kitchen",
              "clean the bathroom",
              "clean the living room",
              "clean the kitchen and the bathroom",
              "clean the kitchen and the living room"]

modes_test = ["quick",
              "quickly", "clean quickly", 
              "fast", "do it fast", 
              "deep", "deep cleaning"]

days_test = ["monday", "on monday",
             "monday and friday", "on monday and on friday",
             "monday tuesday and saturday",
             "monday and friday and not saturday"]

times_test = ["19", "at 19",
              "the 12", "after 12"]

permanent_test = ["every day",
                  "each day",
                  "every monday",
                  "each monday"]

sentences = ["clean the kitchen quickly and the living room at 17 every monday",
             "clean the kitchen",
             "clean the kitchen quick",
             "clean the kitchen quickly", "clean quickly the kitchen",
             "deep clean the kitchen",
             "clean the kitchen quickly every Monday at 10",
             "clean the kitchen quickly and the living room at 17 every monday",
             "clean the kitchen at 10 every monday",
             "clean the bathroom today",
             "today and tomorrow at 18",
             "do it tomorrow"] + rooms_test + modes_test + days_test + times_test + permanent_test

# Python3
#def remove_punctuation(str):
#    translator = str.maketrans('', '', string.punctuation)
#    return str.translate(translator)
#sentences = map(remove_punctuation, sentences)

def remove_punctuation(sentence):
    return sentence.strip(string.punctuation)

def lower(sentence):
    return str.lower(sentence)

sentences = list(map(lower, sentences))
sentences = list(map(remove_punctuation, sentences))

print("N = {}".format(len(sentences)))
print("sentences = list(range(N))")
print("dep = list(range(N))")
print("tokens = list(range(N))")

for i in range(len(sentences)):
    dependency = nlp.dependency_parse(sentences[i])
    token = nlp.word_tokenize(sentences[i])

    print("sentences[{}] = '{}'". format(i, sentences[i]))
    print("dep[{}] = {}".format(i, dependency))
    print("tokens[{}] = {}".format(i, token))

# Do "python ./test_generator.py > generated.py"

nlp.close()