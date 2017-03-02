from textblob.classifiers import NaiveBayesClassifier
from textblob.blob import TextBlob
from nltk.corpus import stopwords

stop = stopwords.words('english')

pos_dict={}
neg_dict={}
with open('/Users/administrator/json_train.json', 'r') as fp: 
     cl = NaiveBayesClassifier(fp, format="json")
print "Done Training"

rp = open('/Users/administrator/test_data.txt','r')
res_writer = open('/Users/administrator/results.txt','w')
for line in rp:
    linelen = len(line)
    line = line[0:linelen-1]
    sentvalue = cl.classify(line)
    blob = TextBlob(line)
    sentence = blob.sentences[0]
    for word, pos in sentence.tags:
       if (word not in stop) and (len(word)>3 \
            and sentvalue == 'pos'): 
         if pos == 'NN' or pos == 'V':  
           pos_dict[word.lower()] = word.lower()
       if (word not in stop) and (len(word)>3 \
            and sentvalue == 'neg'): 
         if pos == 'NN' or pos == 'V':  
           neg_dict[word.lower()] = word.lower()

    res_writer.write(line+" => sentiment "+sentvalue+"\n")

    #print(cl.classify(line))
print "Lengths of positive and negative sentiments",len(pos_dict), len(neg_dict)  

