import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import sys
import json
from threading import Thread
from collections import deque

class JARVISCore:
    """
    Core AI engine for JARVIS system
    Handles voice recognition, processing, and response generation
    """
    
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 150)  # Speed of speech
        self.engine.setProperty('volume', 0.9)  # Volume level
        
        self.user_name = "Sir"
        self.commands_history = deque(maxlen=100)
        self.learning_data = {}
        self.is_listening = False
        
    def speak(self, text):
        """Convert text to speech"""
        print(f"\n[JARVIS]: {text}\n")
        self.engine.say(text)
        self.engine.runAndWait()
    
    def listen(self):
        """Listen and recognize speech from microphone"""
        try:
            with sr.Microphone() as source:
                self.recognizer.adjust_for_ambient_noise(source, duration=1)
                print("\n[LISTENING...]")
                audio = self.recognizer.listen(source, timeout=10)
                
            text = self.recognizer.recognize_google(audio)
            print(f"[USER]: {text}")
            return text.lower()
        
        except sr.UnknownValueError:
            self.speak("I could not understand that, Sir. Please repeat.")
            return None
        except sr.RequestError:
            self.speak("I'm having trouble connecting to the service. Please check your internet.")
            return None
        except Exception as e:
            print(f"Error: {e}")
            return None
    
    def get_greeting(self):
        """Return appropriate greeting based on time of day"""
        hour = datetime.datetime.now().hour
        
        if hour < 12:
            return f"Good morning, {self.user_name}. Systems online and ready."
        elif hour < 18:
            return f"Good afternoon, {self.user_name}. At your service."
        else:
            return f"Good evening, {self.user_name}. How may I assist you?"
    
    def get_time(self):
        """Get current time"""
        return datetime.datetime.now().strftime("%H:%M:%S")
    
    def get_date(self):
        """Get current date"""
        return datetime.datetime.now().strftime("%A, %B %d, %Y")
    
    def search_wikipedia(self, query):
        """Search Wikipedia for information"""
        try:
            results = wikipedia.summary(query, sentences=2)
            return results
        except wikipedia.exceptions.DisambiguationError as e:
            return f"Multiple results found. Please be more specific: {str(e)[:100]}"
        except wikipedia.exceptions.PageError:
            return f"No information found about {query}."
        except Exception as e:
            return f"Error searching Wikipedia: {str(e)}"
    
    def open_website(self, website):
        """Open a website in default browser"""
        try:
            if not website.startswith('http'):
                website = 'https://' + website
            webbrowser.open(website)
            return f"Opening {website}"
        except Exception as e:
            return f"Could not open website: {str(e)}"
    
    def process_command(self, command):
        """Process user commands"""
        self.commands_history.append(command)
        
        # Time and date commands
        if 'time' in command:
            return self.get_time()
        elif 'date' in command:
            return self.get_date()
        
        # Information commands
        elif 'who is' in command or 'what is' in command:
            query = command.replace('who is', '').replace('what is', '').strip()
            return self.search_wikipedia(query)
        
        # Web commands
        elif 'open' in command:
            website = command.replace('open', '').strip()
            return self.open_website(website)
        elif 'google' in command:
            query = command.replace('google', '').strip()
            return self.open_website(f"google.com/search?q={query}")
        
        # System commands
        elif 'shutdown' in command or 'exit' in command:
            return "SHUTDOWN_SEQUENCE"
        elif 'status report' in command:
            return self.get_system_status()
        
        # Greeting
        elif 'hello' in command or 'hi' in command or 'hey' in command:
            return self.get_greeting()
        
        else:
            return "Command not recognized. Please try again."
    
    def get_system_status(self):
        """Get system status report"""
        status = f"""
        JARVIS SYSTEM STATUS REPORT
        ============================
        Current Time: {self.get_time()}
        Current Date: {self.get_date()}
        System Status: OPTIMAL
        Memory Usage: Nominal
        Network Connection: Stable
        Voice Recognition: Active
        Text-to-Speech Engine: Active
        Processing Cores: Ready
        """
        return status

    def get_command_history(self):
        """Get list of recent commands"""
        return list(self.commands_history)
