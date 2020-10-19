
# Function to remove stop words
def removeStopWords(document):
    cleanDocument = []
    termCount = {}
    for term in document:
        if term in termCount:
            termCount[term] += 1
        else:
            termCount[term] = 1
    countFrequency = {}
    for term in termCount:
        if termCount[term] in countFrequency:
            countFrequency[termCount[term]] += 1
        else:
            countFrequency[termCount[term]] = 1
    frequency = {}
    for ele in termCount:
        if termCount[ele] in frequency:
            frequency[termCount[ele]].append(ele)
        else:
            frequency[termCount[ele]] = [ele]
    freq = list(frequency.keys())
    freq.sort()
    for index in range(len(freq)//10,9*len(freq)//10+1):
        cleanDocument.extend(frequency[freq[index]])
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
    docId += 1  # Updating Document Id for all document