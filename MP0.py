import random 
import os
import string
import sys
import re

stopWordsList = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours",
            "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its",
            "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that",
            "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having",
            "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
            "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
            "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
            "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
            "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
            "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

delimiters = " \t,;.?!-:@[](){}_*/"

def getIndexes(seed):
    random.seed(seed)
    n = 10000
    number_of_lines = 50000
    ret = []
    for i in range(0,n):
        ret.append(random.randint(0, 50000-1))
    return ret

def process(userID):
    indexes = getIndexes(userID)
    ret = []
    # TODO
    #f = open("output.txt","w")
    counts = dict()
    lines = sys.stdin.readlines()     
    dPattern = '|'.join(map(re.escape,delimiters))  
    for i in range(len(indexes)):
    # only process titles with certain indexes
            # break into lines and remove '\n'
            #f.write(str(indexes[i]))
            #f.write("\n")
            #f.write(lines[indexes[i]])
            line = lines[indexes[i]].strip()
            # break into words by delimiters
            for word in re.split(dPattern, line):
                # remove empty strings
                if word != '':
                    # covert to lowercase
                    word = word.lower()
                    if word not in stopWordsList:
                        counts[word]=counts.get(word,0)+1   
    #f.close
    sortKeys = sorted(sorted(counts), key=counts.get, reverse=True)
    ret = sortKeys[:20]
    for word in ret:
        print word

process(sys.argv[1])
