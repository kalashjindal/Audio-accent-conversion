# Importing the required modules.
"""
It takes an audio file in WAV format, performs speech recognition on it, performs speech synthesis
on the recognized text, and plays the output audio file
"""
import soundfile as sf
import sounddevice as sd
from pydub import AudioSegment
from pydub.playback import play
import speech_recognition as sr
from gtts import gTTS
import os

# Recording audio
def record_audio():
    """
    It records audio for a specified duration and saves it to a specified file.
    """
    try:
        duration = int(input("Enter recording duration in seconds: "))
        filename = input("Enter file name to save the recording: ")
        sample_rate = 44100
        channels = 1
        print(f"Recording audio for {duration} seconds...")
        audio = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=channels)
        sd.wait()
        sf.write(filename, audio, sample_rate)
        print(f"Recording saved as {filename}")
    except Exception as e:
        print(f"Error while recording audio: {str(e)}")



# Playing audio
def play_audio():
    """
    It lists all the .wav files in the current directory, prompts the user to select one, and then plays
    it
    :return: the audio and sample rate of the file.
    """
    audio_files = [f for f in os.listdir(".") if f.endswith(".wav")]
    if not audio_files:
        print("No audio files found in the current directory.")
        return

    print("Select an audio file to play:")
    for i, f in enumerate(audio_files):
        print(f"{i+1}. {f}")
    while True:
        try:
            choice = int(input("Enter your choice (1-{}): ".format(len(audio_files))))
            if choice < 1 or choice > len(audio_files):
                raise ValueError
            break
        except ValueError:
            print("Invalid choice. Please enter a number between 1 and {}.".format(len(audio_files)))
    
    filename = audio_files[choice-1]
    audio, sample_rate = sf.read(filename)
    print(f"Playing audio from {filename}...")
    sd.play(audio, sample_rate)
    sd.wait()
    print("Playback complete.")

# Speech recognition and synthesis
def speech_recognition_and_synthesis():
    """
    It takes an audio file in WAV format, performs speech recognition on it, performs speech synthesis
    on the recognized text, and plays the output audio file
    :return: the audio file that is being processed.
    """
    audio_files = [f for f in os.listdir() if f.endswith('.wav')]
    if not audio_files:
        print("No WAV audio files found in the current directory.")
        return
    
    print("Select an audio file to process:")
    for i, f in enumerate(audio_files):
        print(f"{i+1}. {f}")
    
    while True:
        try:
            choice = int(input("Enter your choice (1-%d): " % len(audio_files)))
            if choice < 1 or choice > len(audio_files):
                raise ValueError
            filename = audio_files[choice-1]
            break
        except ValueError:
            print("Invalid choice. Please try again.")
    
    dst_accents = {
        '1': 'en-GB',
        '2': 'es-ES',
        '3': 'fr-FR'
    }
    
    while True:
        print("Select a destination accent:")
        for i, accent in enumerate(dst_accents.values()):
            print(f"{i+1}. {accent}")
        
        try:
            choice = input("Enter your choice (1-%d): " % len(dst_accents))
            dst_accent = dst_accents[choice]
            break
        except KeyError:
            print("Invalid choice. Please try again.")
    
    # Load audio file
    audio_file = AudioSegment.from_file(filename, format="wav")

    # Convert audio file to WAV format
    audio_file.export("temp.wav", format="wav")

    # Load audio data from file
    r = sr.Recognizer()
    with sr.WavFile("temp.wav") as source:
        audio_data = r.record(source)

    # Perform speech recognition with source accent
    text = r.recognize(audio_data)

    # Perform speech synthesis with destination accent
    tts = gTTS(text, lang=dst_accent)
    tts.save("output_audio.mp3")

    # Convert MP3 file to WAV format
    audio_file = AudioSegment.from_file("output_audio.mp3", format="mp3")
    audio_file.export("output_audio.wav", format="wav")

    # Play output audio file
    output_audio = AudioSegment.from_file("output_audio.wav", format="wav")
    play(output_audio)

# Main function
def main():
    """
    It prints a menu, asks the user to enter a choice, and then calls the appropriate function based on
    the user's choice.
    """
    while True:
        print("\n\n*** AUDIO PROCESSING MENU ***")
        print("1. Record audio")
        print("2. Play audio")
        print("3. Speech recognition and synthesis")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")
        
        if choice == "1":
            record_audio()
        elif choice == "2":
            play_audio()
        elif choice == "3":
            speech_recognition_and_synthesis()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
            
            
# This is a common Python idiom. It is used to ensure that the code in the main() function is executed
# only when the script is run directly. If the script is imported as a module, the code in the main()
# function is not executed.
if __name__ == "__main__":
    main()
