#Get the user name first

x =raw_input('Enter your name:')
print('Hello ' + x)
y =raw_input('How are you doing today,' +x)

import Algorithmia

input = y
client = Algorithmia.client('simsmuMGjwhXqpi7hcakzab+RoG1')
algo = client.algo('nlp/SentimentAnalysis/0.1.2')
print algo.pipe(input)

