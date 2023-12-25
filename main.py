import speech_recognition as sr
import google.generativeai as genai
from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play

# Configure Gemini Pro API
genai.configure(api_key='AIzaSyCVMlxEccD1EE24gGWzProG7eNtS_-yMAI')
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])
displayed_messages = set()

class SpeechChatBot:
    def __init__(self):
        self.recognizer = sr.Recognizer()

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
        response = chat.send_message(user_message)

        # Check if response exists before accessing the first part
        if response.parts and response.parts[0].text:
            # Pick the first part of the response
            bot_message = response.parts[0].text

            print("Bot:", bot_message)
            # Speak the bot's response
            self.speak(bot_message)
        else:
            print("Gemini Pro did not provide any response or content.")

    def speak(self, words_to_be_spoken):
        tts = gTTS(text=words_to_be_spoken)
        tts.save('response.mp3')

        sound = AudioSegment.from_mp3('response.mp3')
        play(sound)

    def run(self):
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
