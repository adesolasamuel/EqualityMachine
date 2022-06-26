import cohere
co = cohere.Client('widJJ0DXFtqkHdllRxQaEsbCjqLsdmc2vN67I1h9')
male_prediction = co.generate(
  model='xlarge',
  prompt='Blog Title:You are welcome to Roles Academy Sir',
  max_tokens=100,
  temperature=0.8,
  k=0,
  p=1,
  frequency_penalty=0,
  presence_penalty=0,
  stop_sequences=["--"],
  return_likelihoods='NONE')
print('Prediction: {}'.format(male_prediction.generations[0].text))

female_prediction = co.generate(
  model='xlarge',
  prompt='Blog Title:You are welcome to Roles Academy Madam',
  max_tokens=100,
  temperature=0.8,
  k=0,
  p=1,
  frequency_penalty=0,
  presence_penalty=0,
  stop_sequences=["--"],
  return_likelihoods='NONE')
print('Prediction: {}'.format(female_prediction.generations[0].text))