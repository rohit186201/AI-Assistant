Voice Assistant (Arester) using Python

Overview
This Python script implements a voice-controlled assistant named Arester. Arester uses the SpeechRecognition library to recognize voice commands and responds accordingly. It can perform various tasks such as searching Wikipedia, opening websites, playing music on Spotify, checking the current time, and sending emails.

Requirements
Python 3.x
pyttsx3
SpeechRecognition
Wikipedia-API
webbrowser
smtplib
os
Installation
Clone the repository:

bash
git clone https://github.com/your-username/voice-assistant.git
Install the required packages:

bash
pip install pyttsx3 SpeechRecognition wikipedia-api
Create a file named config.py and add your email password:

python
password = "your_email_password"
Replace "your_email_password" with the actual password.

Usage
Run the script:

bash
Copy code
python voice_assistant.py
Arester will greet you and wait for voice commands.

Speak commands such as:

"Wikipedia [your query]"
"Open YouTube"
"Play music"
"What's the time?"
"Email to [recipient]"
"Quit"
Additional Notes
The script uses the Google Speech Recognition API for voice recognition, so an internet connection is required.
Make sure to provide the correct path to the Spotify and Chrome executables on your system.
Feel free to customize the script or add more functionality based on your requirements.
