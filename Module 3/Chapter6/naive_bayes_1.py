from textblob.classifiers import NaiveBayesClassifier
from textblob.blob import TextBlob

train = [
    ('I like this new tv show.', 'pos'),
    ('This is a very exciting event!', 'pos'),
    ('I feel very good about after I workout.', 'pos'),
    ('This is my most accomplished work.', 'pos'),
    ("What an awesome country", 'pos'),
    ("They have horrible service", 'neg'),
    ('I do not like this new restaurant', 'neg'),
    ('I am tired of waiting for my new book.', 'neg'),
    ("I can't deal with my toothache", 'neg'),
    ("The fun events in costa rica were amazing",'pos'), 
    ('He is my worst boss!', 'neg'),
    ('People do have bad writing skills on facebook', 'neg')
]
test = [
    ('The beer was good.', 'pos'),
    ('I do not enjoy my job', 'neg'),
    ("I feel amazing!", 'pos'),
    ('Mark is a friend of mine.', 'pos'),
    ("I can't believe I was asked to do this.", 'neg')
]

cl = NaiveBayesClassifier(train)
print(cl.classify("The new movie was amazing."))  # "pos"
print(cl.classify("I don't like ther noodles."))   # "neg"

print "Test Results"
cl.update(test)

# Classify a TextBlob
blob = TextBlob("The food was good. But the service was horrible. "
                "My father was not pleased.", classifier=cl)
print(blob)
print(blob.classify())

for sentence in blob.sentences:
    print(sentence)
    print(sentence.classify())

# Compute accuracy
print("Accuracy: {0}".format(cl.accuracy(test)))

# Show 5 most informative features
cl.show_informative_features(10)

