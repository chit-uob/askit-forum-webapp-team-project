import oneai                                  #install oneai

oneai.api_key = "042258be-d1e8-4bd0-9df1-ce48677e096d"

def summariseToString (text):                 # accepts string inputs
    pipeline = oneai.Pipeline(
      steps = [
            oneai.skills.Summarize(),
      ]
    )

    output = pipeline.run(text)
    return output.summary.text

def tagToArray (text):                        # accepts stirng input 
    pipeline = oneai.Pipeline(
      steps = [
        oneai.skills.Topics(),
      ]
    )
    output = pipeline.run(text)
    return output.topics.values               # returns an array of tags as strings

def addToCluster(text):
  collection = oneai.clustering.Collection("questions")
  collection.add_items(text)