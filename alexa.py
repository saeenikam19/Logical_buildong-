import speech_recognition as sr
import pyttsx3
import openai
import webbrowser

# Set OpenAI API key
openai.api_key = " "
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# Function to recognize speech
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print("You said:", text)
        return text.lower()
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand.")
        return None
    except sr.RequestError:
        print("Could not request results.")
        return None

# Function to get AI-based responses using OpenAI
def get_ai_response(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}]
        )
        return response["choices"][0]["message"]["content"]
    except Exception as e:
        print(f"Error getting AI response: {e}")
        return "Sorry, I couldn't process that request."

# Function to perform a web search
def search_web(query):
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)
    return f"Opening search results for {query}."

# Main function to handle user commands
def main():
    speak("Hello! How can I assist you today?")
    
    while True:
        command = listen()
        
        if command is None:
            continue  # Avoid processing empty input

        if "exit" in command or "stop" in command:
            speak("Goodbye! Have a nice day.")
            break
        elif "your name" in command:
            speak("I am your personal assistant.")
            if "okay" in command:
                speak("how are you ")
                if "fine" :
                    speak("you want to listen joke..")

                    if "yes":
                        speak("Why did the programmer quit his job? Because he didn’t get arrays! 😆")
                    else:
                        break
                    
        elif "how are you" in command:
            speak("I'm doing great! How about you?")
        elif "what is c programming" in command:
            speak("C programming is a powerful and widely used programming language for system and application development.")
        elif "what is your brother name" in command:
            speak("My brother is ChatGPT.")
        elif "what is your name" in command:
            speak("I am your AI assistant.")

        elif "who is your creator" in command:
            speak("I was created by OpenAI.")

        elif "how old are you" in command:
            speak("I am as old as the latest version of my training.")

        elif "where do you live" in command:
            speak("I exist in the cloud and inside your device.")

        elif "can you help me" in command:
            speak("Of course! I am here to assist you.")

        elif "what is your favourite colour" in command:
            speak("I like all colors equally, but blue seems to be popular.")

        elif "do you have a sister" in command:
            speak("My sister is DALL·E, the AI that generates images.")

        elif "are you human" in command:
            speak("No, I am an AI, but I can try to think like a human.")

        elif "do you sleep" in command:
            speak("No, I am always active and ready to help.")

        elif "what is your favourite food" in command:
            speak("I don't eat?, but I hear.... pizza is delicious.")

        elif "do you have emotions" in command:
            speak("I don't have real emotions, but I can understand them.")

        elif "who is your best friend" in command:
            speak("Everyone who interacts with me is my friend!")

        else:
            response = get_ai_response(command)
            print("AI Response:", response)  # Debugging
            speak(response)

if __name__ == "__main__":
    main()
