# SpeechChatBot with Gemini Pro API

This repository contains a Python implementation of a Speech-to-Speech chatbot using the Google Gemini Pro API. The chatbot listens to your spoken input, processes it using the Gemini Pro model, and responds with spoken output.

## Prerequisites

- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/)
- [gTTS (Google Text-to-Speech)](https://pypi.org/project/gTTS/)
- [pydub](https://pypi.org/project/pydub/)
- [Google Gemini Pro API Key](https://console.cloud.google.com/)

## Setup

1. Clone this repository to your local machine.

   ```bash
   git clone https://github.com/SAKETH11111/Talk-to-Gemini-pro
   ```

2. Make sure you have the following Python packages installed:

   - SpeechRecognition
   - google-generativeai
   - gtts
   - pydub

   Install them using the provided `requirements.txt` file.

   ```bash
   pip install -r requirements.txt
   ```

3. Obtain your Gemini Pro API key from the [Google AI Studio](https://makersuite.google.com/app/apikey). Replace `"Your_Gemini_Pro_API_Key"` in the code with your actual API key.

## Usage

1. Run the script:

   ```bash
   python main.py
   ```

2. Start speaking when prompted, and the chatbot will respond using the Gemini Pro model.

3. Continue the conversation as long as you'd like. To end the chat, simply say "quit."

## Note

- Ensure that your microphone is correctly configured and accessible by the script.
- Adjust the script according to your specific use case or integrate it into a larger project.

## License

This project is licensed under the [GNU General Public License](LICENSE).

Feel free to explore, modify, and contribute to enhance the functionality of this SpeechChatBot! If you encounter any issues or have suggestions, please open an [issue](https://github.com/SAKETH11111/Talk-to-Gemini-pro/issues).

Happy chatting! 🎙️🤖
