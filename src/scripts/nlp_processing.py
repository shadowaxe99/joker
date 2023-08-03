```python
import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag

def processInput(userInput):
    # Tokenize the user input
    tokens = nltk.word_tokenize(userInput)

    # Apply part of speech tagging
    pos_tags = nltk.pos_tag(tokens)

    # Extract relevant information from user input
    extracted_info = extract_information(pos_tags)

    return extracted_info

def extract_information(pos_tags):
    # Define a pattern to extract name and location
    pattern = 'NP: {<DT>?<JJ>*<NN>}'

    # Apply chunking to extract information
    cp = nltk.RegexpParser(pattern)
    cs = cp.parse(pos_tags)

    # Extract named entities
    named_entities = nltk.ne_chunk(pos_tags, binary=True)

    # Extract name and location from named entities
    name = ''
    location = ''
    for subtree in named_entities.subtrees(filter=lambda t: t.label() == 'NP'):
        entity = " ".join([token for token, pos in subtree.leaves()])
        if 'NNP' in [pos for token, pos in subtree.leaves()]:
            name = entity
        else:
            location = entity

    return {'name': name, 'location': location}
```