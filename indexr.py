
# Function to remove stop words
def removeStopWords(document):
    cleanDocument = document
    # Process
    return cleanDocument

# Create Corpus
corpus = []

'''
    Collection of Documents is called Corpus
'''

# Create Indexer
index = {}

# Create dictionary count
termDocCount = {}

# Indexing
docId = 1
    '''
        Document id starts from 1
    '''
for document in corpus:
    newDocument = removeStopWords(document)
    terms = {}  # Dictionary to store term count
    for term in newDocument:
        if term in terms:
            terms[term] += 1
        else:
            terms[term] = 1
    for term in terms:
        if term in index:
            index[term].append((docId,terms[term]))
            termDocCount[term] += 1
        else:
            index[term] = [(docId,terms[term])]
            termDocCount[term] = 1