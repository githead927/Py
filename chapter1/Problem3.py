import pyttsx3

# Initialize the pyttsx3 engine 63
engine = pyttsx3.init()

# Optional: List available voices to choose from
voices = engine.getProperty('voices')
for index, voice in enumerate(voices):
    print(f"Voice {index}: {voice.name} ({voice.id})")

# Set a specific voice based on your choice
# Replace the index below with a voice index from the list above that sounds close to JARVIS
engine.setProperty('voice', voices[63].id)  # Choose a different index if needed

# Adjust speaking rate and volume for effect
engine.setProperty('rate', 160)   # Adjust rate as desired
engine.setProperty('volume', 1.8) # Set volume to maximum

# The message JARVIS will say
message = "Hey Sakshi, I am GENE at your service , madame "
# Make JARVIS speak
engine.say(message)
engine.runAndWait()
