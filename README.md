# EqualityMachine
Project Submission for Hackathon
# Inspiration
The inspiration for this project came from the day-to-day computers we interact with. If you want to enter a supermarket, a computer voice probably a female voice might welcome you, interacting with the ATM, the same thing, a female voice, EqualityMachine was built to give this machines opportunity on how every gender should be approached. 

# What it does
EqualityMachine is a computer bot or robot that interacts with a human without being gender-biased. It can be a welcoming voice into a supermarket or ATM voice. Through the use of a camera and machine learning from Google Cloud, it can know human gender and using Natural Language Processing, it will automatically generate the right mode of approaching the human.

In this project, I'm using a case study of a school Roles Academy, EqualityMachine is installed in the reception, it welcomes the visitors and gives a short summary of the academy. The machine is able to detect the visitor's gender and will greet and give a short summary of the academy. If it sees a man, it communicates in a male voice and if it sees a woman, it communicates using a female voice.


# How we built it
EqualityMachine runs majorly on two software, Google Cloud Machine Learning and Cohere Natural Language Processing. The Hardware parts make use of Raspberry Pi, A Camera module, and an external loudspeaker as output.

## The Hardware 
The Hardware consists of a Raspberry Pi interfaced with a Camera module and a Bluetooth loudspeaker using the pulse Audio Linux library. Raspbian which is a Linux design distribution was loaded on the Raspberry pi and all configurations were made.

## The Software
First, we trained our model using the Google Cloud Teachable Machine platform, the model was served pictures of male and female figures and the final model was exported as a TensorFlow Lite model. 
After training the model, we then proceed to Cohere NLP platform and use the Generate service offered by the Cohere.ai platform to give a sample headline of the company greetings which is "Welcome to Roles Academy sir" for a male visitor and "Welcome to Roles Academy Madam" for a female visitor. The platform then automatically generates a paragraph of greetings and a description of our sampled company (Roles Academy), the description matches the description of a typical Academy as the company name implies.

 Sample output from Cohere: 
_Prediction: .
You are welcome to Roles Academy Sir.
About Company:Roles Academy is a premier institute for the preparation of IIT-JEE, AIEEE, and other engineering entrance examinations. Roles Academy has a rich experience of training students for various engineering entrance examinations. The academy has produced top ranks in various engineering entrance examinations._


An API key to communicate with Cohere was generated on the Web platform and Cohere python module was pip installed on the Raspberry pi. The code for this machine was fully written in python and it uses some libraries like Cohere, pyttzx3, gTTS for text to speech conversions, OpenCV for image processing, and the Camera module.



## Challenges we ran into
The first challenge the team faced was setting up the hardware since it is not easy working remotely while creating a hardware project but tasks were efficiently split among team members using GitHub.

The Raspberry pi lacks a loudspeaker onboard, therefore using an external Bluetooth loudspeaker comes with some problems due to compatibility, we were able to overcome this using the PulseAudio Linux library.

Being the first time working with Cohere.ai, it wasn't easy setting up the Generate service and working with the preset python code for interacting with cohere.

Our Machine is proposed to be able to recognize and differentiate between male and female, due to the shortage of male and female training datasets, we trained the model with a very limited amount of datasets available.

## Accomplishments that we're proud of
Given just limited time, having the project fully working is the first achievement we are proud of.
It was our first time working with cohere, it was a little bit challenging but we learned a lot.

## What we learned
Working with new technologies like PulseAudio, Cohere.ai, and Google Cloud machine learning platform.
We learned more about hardware structures and working principles.

## What's next for EqualityMachine
Training EqualityMachine with more datasets to better differentiate between genders.

Building a software version of the machine which can work in a Web browser and also as a standalone application.

Improving on the male voice, at present, it's a little bit waggy. 

