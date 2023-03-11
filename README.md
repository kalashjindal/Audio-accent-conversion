# Audio Accent Conversion with Python 👨‍💻

This Python program performs audio processing on WAV files. It includes options for recording audio, playing audio files, and performing speech recognition and synthesis.

## Requirements

- Python 3.6 or above
- soundfile
- sounddevice
- pydub
- speech_recognition
- gTTS

## Usage

1. Clone the repository and navigate to the project directory in the terminal.
2. Run the program with `python accent_conversion.py`.
3. Choose from the menu options to record audio, play audio files, or perform speech recognition and synthesis.

## Features

### Record audio

This option records audio for a specified duration and saves it to a specified file. The audio is saved in WAV format.

### Play audio

This option lists all the WAV files in the current directory, prompts the user to select one, and then plays it.

### Speech recognition and synthesis

This option takes an audio file in WAV format, performs speech recognition on it, performs speech synthesis on the recognized text, and plays the output audio file. The user is prompted to select the input audio file, as well as the desired output language accent.

## Author

👤 **Kalashjindal**

- Github: [@kalashjindal](https://github.com/kalashjindal)

## Acknowledgements

- [OpenAI](https://openai.com/)
- [pydub](http://pydub.com/)
- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/)
- [gTTS](https://pypi.org/project/gTTS/)
