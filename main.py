import speech_recognition as sr
import google.generativeai as palm
from gtts import gTTS
from playsound import playsound

# Configure PaLM API
palm.configure(api_key="AIzaSyCVMlxEccD1EE24gGWzProG7eNtS_-yMAI") 
model = "models/chat-bison-001"

class SpeechChatBot:
    def __init__(self):
        self.conversation = []
        
    def listen_and_recognize(self):
        with sr.Microphone() as source:
            print("Listening...")
            audio = self.recognizer.listen(source)
            
        try:
            text = self.recognizer.recognize_google(audio)
            print("You said:", text)
            return text
        except sr.UnknownValueError:
            print("Could not understand audio")
            return None
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
            return None

    def chat(self, user_message):
        # Add user message to conversation history
        self.conversation.append({"author": "user", "content": user_message})
        
        # Generate response
        response = palm.chat(
            model=model,
            messages=self.conversation,
            candidate_count=3
        ).candidates
        
        # Check if candidates exist before accessing the first one
        if response and response[0]["content"]:
            # Pick the first candidate response
            bot_message = response[0]["content"]
            
            # Add bot message to conversation history
            self.conversation.append({"author": "bot", "content": bot_message})
            
            print("Bot:", bot_message)
            # Speak the bot's response
            self.speak(bot_message)
        else:
            print("PaLM did not provide any candidates or content.")

    def speak(self, words_to_be_spoken):
        tts = gTTS(text=words_to_be_spoken)
        tts.save('response.mp3')
        playsound('response.mp3')

    def run(self):
        self.recognizer = sr.Recognizer()

        while True:
            user_input = self.listen_and_recognize()

            if user_input:
                if user_input.lower() == "quit":
                    print("CHAT ENDED")
                    break

                self.chat(user_input)

if __name__ == "__main__":
    chat_bot = SpeechChatBot()
    chat_bot.run()
