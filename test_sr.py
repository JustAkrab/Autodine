# testing speech recognition# NOTE: this example requires PyAudio because it uses the Microphone class
"""
import speech_recognition as sr

# obtain audio from the microphone
r = sr.Recognizer()

with sr.Microphone() as source:
    # r.adjust_for_ambient_noise(source, duration=10)
    print("Say something!")
    # r.adjust_for_ambient_noise(source, duration=1)
    while True:
        process = True

        audio = r.listen(source)

        # recognize speech using Google Speech Recognition
        try:
            # for testing purposes, we're just using the default API key
            # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
            # instead of `r.recognize_google(audio)`
            print(r.recognize_google(audio))
        except sr.UnknownValueError:
            # print("Google Speech Recognition could not understand audio")
            pass
        except sr.RequestError as e:
            pass
            # ("Could not request results from Google Speech Recognition service; {0}".format(e))   
"""     

# idea 1: drive-thru ordering.
# idea 2: finance management portfolio
# idea 3: fighting game


# Python program to translate
# speech to text and text to speech


import speech_recognition as sr
import pyttsx3 

# Initialize the recognizer 
r = sr.Recognizer() 

# Function to convert text to
# speech
def SpeakText(command):
	
	# Initialize the engine
	engine = pyttsx3.init()
	engine.say(command) 
	engine.runAndWait()

def get_text():
	
	# Exception handling to handle
	# exceptions at the runtime

	try:
		
		# use the microphone as source for input.
		with sr.Microphone() as source2:
			
			# wait for a second to let the recognizer
			# adjust the energy threshold based on
			# the surrounding noise level 
			r.adjust_for_ambient_noise(source2, duration=0.2)
			
			#listens for the user's input 
			audio2 = r.listen(source2, 10, 5)
			
			# Using google to recognize audio
			MyText = r.recognize_google(audio2)
			MyText = MyText.lower()
			print(MyText)
			return MyText
			# print("Did you say ",MyText)
			# print(MyText)
			# SpeakText(MyText)
			
	except sr.RequestError as e:
		print("Could not request results; {0}".format(e))
		return ""
		
	except sr.UnknownValueError:
		print("...")
		return ""
	
	
# Loop infinitely for user to
# speak

if __name__ == "__main__":
	while(1): 
		text_heard = get_text()