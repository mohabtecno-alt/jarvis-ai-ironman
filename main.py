import pygame
import sys
from jarvis_core import JARVISCore
from interface import IronManInterface
from threading import Thread
import time
import requests
from urllib.parse import quote
import os

class JARVISSystem:
    """
    Main JARVIS system that combines AI engine with Iron Man interface
    """
    
    def __init__(self):
        self.core = JARVISCore()
        self.interface = IronManInterface()
        self.running = True
        self.user_name = "Sir"
        self.is_first_run = True
        
    def get_image_for_topic(self, topic):
        """Download an image for the given topic"""
        try:
            # Create images directory if it doesn't exist
            if not os.path.exists('images'):
                os.makedirs('images')
            
            # Use Unsplash API (free image service)
            search_query = quote(topic)
            url = f"https://source.unsplash.com/400x400/?{search_query}"
            
            filename = f"images/{topic.replace(' ', '_')}.jpg"
            
            # Download image
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                with open(filename, 'wb') as f:
                    f.write(response.content)
                return filename
        except Exception as e:
            print(f"Error downloading image: {e}")
        
        return None
    
    def process_user_input(self, user_input):
        """Process user input and generate response"""
        self.interface.set_processing(True)
        self.interface.set_status("PROCESSING")
        
        # Process command through JARVIS core
        response = self.core.process_command(user_input)
        
        # Get image based on user input
        if 'who is' in user_input or 'what is' in user_input:
            topic = user_input.replace('who is', '').replace('what is', '').strip()
            image_path = self.get_image_for_topic(topic)
            if image_path:
                self.interface.set_image(image_path)
        
        self.interface.set_processing(False)
        
        return response
    
    def listen_for_commands(self):
        """Listen for voice commands in a separate thread"""
        while self.running:
            self.interface.set_listening(True)
            self.interface.set_status("LISTENING")
            
            user_input = self.core.listen()
            self.interface.set_listening(False)
            
            if user_input:
                response = self.process_user_input(user_input)
                
                if response == "SHUTDOWN_SEQUENCE":
                    self.interface.set_message("INITIATING SHUTDOWN SEQUENCE")
                    self.core.speak("Shutting down. See you next time, " + self.user_name)
                    self.running = False
                    break
                
                self.interface.set_message(response)
                self.core.speak(response)
            
            time.sleep(1)
    
    def run(self):
        """Main run loop"""
        # Welcome message
        welcome_msg = self.core.get_greeting()
        self.interface.set_message(welcome_msg)
        self.core.speak(welcome_msg)
        
        # Start listening thread
        listen_thread = Thread(target=self.listen_for_commands, daemon=True)
        listen_thread.start()
        
        # Main interface loop
        running = True
        while running and self.running:
            self.interface.update()
            running = self.interface.handle_events()
            self.interface.render()
            self.interface.clock.tick(self.interface.fps)
        
        self.running = False
        self.interface.close()
        print("\nJARVIS System Shutdown Complete.")

def main():
    try:
        jarvis = JARVISSystem()
        jarvis.run()
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
