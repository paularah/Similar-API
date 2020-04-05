import spacy


def checkSimilarity(arr):
    nlp = spacy.load('en_core_web_sm')
    score = []
    pair = []
    for i in range(len(arr)):
        for j in range(len(arr)):
            text1 = nlp(arr[i])
            text2 = nlp(arr[j])
            ratio = text1.similarity(text2)
            score.append(ratio)
            pair.append([i, j])
    return score, pair


def rankScore(score, pair):
    similar_pair = []
    for values in range(len(score)):
        if values > 0.6:
            similar_pair.append(pair[values])
    return similar_pair


def call_model(arr):
    score, pair = checkSimilarity(arr)
    similar_pair = rankScore(score, pair)
    if len(similar_pair) == 0:
        return "Similarity within threshold"
    return pair
