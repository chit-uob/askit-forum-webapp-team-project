import oneai

# summerize
oneai.api_key = "8160a564-eabc-4c42-ab9c-f08030480892"
oneai.multilingual = True
text = "test"

pipeline = oneai.Pipeline(
  steps = [
		oneai.skills.Summarize(),
  ]
)

output = pipeline.run(text)

pipeline = oneai.Pipeline(
  steps = [
		oneai.skills.Topics(),
  ]
)

output = pipeline.run(text)