import oneai  # install oneai
import spacy # install spacy
import en_core_web_sm

oneai.api_key = "042258be-d1e8-4bd0-9df1-ce48677e096d"


def text_to_summary(text):  # accepts string inputs
    pipeline = oneai.Pipeline(
        steps=[
            oneai.skills.Summarize(),
        ]
    )

    output = pipeline.run(text)
    return output.summary.text


def text_to_tag_array(text):  # accepts stirng input
    pipeline = oneai.Pipeline(
        steps=[
            oneai.skills.Topics(),
        ]
    )
    output = pipeline.run(text)
    return output.topics.values  # returns an array of tags as strings


def add_to_cluster(text):
    collection = oneai.clustering.Collection("questions")
    collection.add_items(text)

def spacy_tag(text1, text2):
    nlp = spacy.load("en_core_web_sm")
    doc1 = nlp(text1)
    doc2 = nlp(text2)

    return doc1.similarity(doc2)