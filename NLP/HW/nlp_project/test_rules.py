N = 38
sentences = list(range(N))
dep = list(range(N))
tokens = list(range(N))
sentences[0] = 'clean the kitchen quickly and the living room at 17 every monday'
dep[0] = [('ROOT', 0, 3), ('amod', 3, 1), ('det', 3, 2), ('advmod', 3, 4), ('cc', 3, 5), ('det', 8, 6), ('compound', 8, 7), ('conj', 3, 8), ('case', 10, 9), ('nmod', 8, 10), ('det', 12, 11), ('dep', 3, 12)]
tokens[0] = ['clean', 'the', 'kitchen', 'quickly', 'and', 'the', 'living', 'room', 'at', '17', 'every', 'monday']
sentences[1] = 'clean the kitchen'
dep[1] = [('ROOT', 0, 1), ('det', 3, 2), ('dobj', 1, 3)]
tokens[1] = ['clean', 'the', 'kitchen']
sentences[2] = 'clean the kitchen quick'
dep[2] = [('ROOT', 0, 3), ('amod', 3, 1), ('det', 3, 2), ('amod', 3, 4)]
tokens[2] = ['clean', 'the', 'kitchen', 'quick']
sentences[3] = 'clean the kitchen quickly'
dep[3] = [('ROOT', 0, 3), ('amod', 3, 1), ('det', 3, 2), ('advmod', 3, 4)]
tokens[3] = ['clean', 'the', 'kitchen', 'quickly']
sentences[4] = 'clean quickly the kitchen'
dep[4] = [('ROOT', 0, 4), ('amod', 4, 1), ('advmod', 4, 2), ('det', 4, 3)]
tokens[4] = ['clean', 'quickly', 'the', 'kitchen']
sentences[5] = 'deep clean the kitchen'
dep[5] = [('ROOT', 0, 2), ('amod', 2, 1), ('det', 4, 3), ('dobj', 2, 4)]
tokens[5] = ['deep', 'clean', 'the', 'kitchen']
sentences[6] = 'clean the kitchen quickly every monday at 10'
dep[6] = [('ROOT', 0, 3), ('amod', 3, 1), ('det', 3, 2), ('advmod', 6, 4), ('det', 6, 5), ('dep', 3, 6), ('case', 8, 7), ('nmod', 6, 8)]
tokens[6] = ['clean', 'the', 'kitchen', 'quickly', 'every', 'monday', 'at', '10']
sentences[7] = 'clean the kitchen quickly and the living room at 17 every monday'
dep[7] = [('ROOT', 0, 3), ('amod', 3, 1), ('det', 3, 2), ('advmod', 3, 4), ('cc', 3, 5), ('det', 8, 6), ('compound', 8, 7), ('conj', 3, 8), ('case', 10, 9), ('nmod', 8, 10), ('det', 12, 11), ('dep', 3, 12)]
tokens[7] = ['clean', 'the', 'kitchen', 'quickly', 'and', 'the', 'living', 'room', 'at', '17', 'every', 'monday']
sentences[8] = 'clean the kitchen at 10 every monday'
dep[8] = [('ROOT', 0, 3), ('amod', 3, 1), ('det', 3, 2), ('case', 5, 4), ('nmod', 3, 5), ('det', 7, 6), ('dep', 3, 7)]
tokens[8] = ['clean', 'the', 'kitchen', 'at', '10', 'every', 'monday']
sentences[9] = 'clean the bathroom today'
dep[9] = [('ROOT', 0, 3), ('amod', 3, 1), ('det', 3, 2), ('nmod:tmod', 3, 4)]
tokens[9] = ['clean', 'the', 'bathroom', 'today']
sentences[10] = 'today and tomorrow at 18'
dep[10] = [('ROOT', 0, 1), ('cc', 1, 2), ('conj', 1, 3), ('case', 5, 4), ('nmod', 1, 5)]
tokens[10] = ['today', 'and', 'tomorrow', 'at', '18']
sentences[11] = 'do it tomorrow'
dep[11] = [('ROOT', 0, 1), ('dobj', 1, 2), ('nmod:tmod', 1, 3)]
tokens[11] = ['do', 'it', 'tomorrow']
sentences[12] = 'clean the kitchen'
dep[12] = [('ROOT', 0, 1), ('det', 3, 2), ('dobj', 1, 3)]
tokens[12] = ['clean', 'the', 'kitchen']
sentences[13] = 'clean the bathroom'
dep[13] = [('ROOT', 0, 1), ('det', 3, 2), ('dobj', 1, 3)]
tokens[13] = ['clean', 'the', 'bathroom']
sentences[14] = 'clean the living room'
dep[14] = [('ROOT', 0, 1), ('det', 4, 2), ('compound', 4, 3), ('dobj', 1, 4)]
tokens[14] = ['clean', 'the', 'living', 'room']
sentences[15] = 'clean the kitchen and the bathroom'
dep[15] = [('ROOT', 0, 3), ('amod', 3, 1), ('det', 3, 2), ('cc', 3, 4), ('det', 6, 5), ('conj', 3, 6)]
tokens[15] = ['clean', 'the', 'kitchen', 'and', 'the', 'bathroom']
sentences[16] = 'clean the kitchen and the living room'
dep[16] = [('ROOT', 0, 3), ('amod', 3, 1), ('det', 3, 2), ('cc', 3, 4), ('det', 7, 5), ('compound', 7, 6), ('conj', 3, 7)]
tokens[16] = ['clean', 'the', 'kitchen', 'and', 'the', 'living', 'room']
sentences[17] = 'quick'
dep[17] = [('ROOT', 0, 1)]
tokens[17] = ['quick']
sentences[18] = 'quickly'
dep[18] = [('ROOT', 0, 1)]
tokens[18] = ['quickly']
sentences[19] = 'clean quickly'
dep[19] = [('ROOT', 0, 1), ('advmod', 1, 2)]
tokens[19] = ['clean', 'quickly']
sentences[20] = 'fast'
dep[20] = [('ROOT', 0, 1)]
tokens[20] = ['fast']
sentences[21] = 'do it fast'
dep[21] = [('ROOT', 0, 1), ('dobj', 1, 2), ('advmod', 1, 3)]
tokens[21] = ['do', 'it', 'fast']
sentences[22] = 'deep'
dep[22] = [('ROOT', 0, 1)]
tokens[22] = ['deep']
sentences[23] = 'deep cleaning'
dep[23] = [('ROOT', 0, 2), ('amod', 2, 1)]
tokens[23] = ['deep', 'cleaning']
sentences[24] = 'monday'
dep[24] = [('ROOT', 0, 1)]
tokens[24] = ['monday']
sentences[25] = 'on monday'
dep[25] = [('ROOT', 0, 2), ('case', 2, 1)]
tokens[25] = ['on', 'monday']
sentences[26] = 'monday and friday'
dep[26] = [('ROOT', 0, 1), ('cc', 1, 2), ('conj', 1, 3)]
tokens[26] = ['monday', 'and', 'friday']
sentences[27] = 'on monday and on friday'
dep[27] = [('ROOT', 0, 2), ('case', 2, 1), ('cc', 2, 3), ('case', 5, 4), ('conj', 2, 5)]
tokens[27] = ['on', 'monday', 'and', 'on', 'friday']
sentences[28] = 'monday tuesday and saturday'
dep[28] = [('ROOT', 0, 2), ('compound', 2, 1), ('cc', 2, 3), ('conj', 2, 4)]
tokens[28] = ['monday', 'tuesday', 'and', 'saturday']
sentences[29] = 'monday and friday and not saturday'
dep[29] = [('ROOT', 0, 1), ('cc', 1, 2), ('conj', 1, 3), ('cc', 1, 4), ('neg', 6, 5), ('conj', 1, 6)]
tokens[29] = ['monday', 'and', 'friday', 'and', 'not', 'saturday']
sentences[30] = '19'
dep[30] = [('ROOT', 0, 1)]
tokens[30] = ['19']
sentences[31] = 'at 19'
dep[31] = [('ROOT', 0, 2), ('case', 2, 1)]
tokens[31] = ['at', '19']
sentences[32] = 'the 12'
dep[32] = [('ROOT', 0, 2), ('det', 2, 1)]
tokens[32] = ['the', '12']
sentences[33] = 'after 12'
dep[33] = [('ROOT', 0, 2), ('case', 2, 1)]
tokens[33] = ['after', '12']
sentences[34] = 'every day'
dep[34] = [('ROOT', 0, 2), ('det', 2, 1)]
tokens[34] = ['every', 'day']
sentences[35] = 'each day'
dep[35] = [('ROOT', 0, 2), ('det', 2, 1)]
tokens[35] = ['each', 'day']
sentences[36] = 'every monday'
dep[36] = [('ROOT', 0, 2), ('det', 2, 1)]
tokens[36] = ['every', 'monday']
sentences[37] = 'each monday'
dep[37] = [('ROOT', 0, 2), ('det', 2, 1)]
tokens[37] = ['each', 'monday']

#~~~~~~~ copy/paste generated code from test_generated.py in the upper part.
from rules_cleaning import CleaningRules
from dependency     import Dependency

dd = Dependency(sentences[0], dep[0], tokens[0])

rule = CleaningRules(dd)

for i in range(N):
    print("~~~~~~~~~~~~\nSentence {}:".format(i))
    print(sentences[i])
    
    if len(tokens[i]) == 1:
        print("Permanent: ", rule.apply("permanent"))
        print("Mode: ", rule.apply("mode"))
        print("Time: ", rule.apply("time"))
    else:
        print(rule.apply(None))
    

    if i == N-1: break
    dd = Dependency(sentences[i+1], dep[i+1], tokens[i+1])
    rule.update(dd)

