import Algorithmia

input = 'If I see you smiling. Does that mean you are happy or sad?'
client = Algorithmia.client('simsmuMGjwhXqpi7hcakzab+RoG1')
algo = client.algo('nlp/SentimentAnalysis/0.1.2')
print algo.pipe(input)
