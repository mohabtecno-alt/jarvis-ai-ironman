import json
import os
from datetime import datetime
import requests

class AdvancedFeatures:
    """
    Advanced features for JARVIS system
    Includes learning, predictions, and smart home integration
    """
    
    def __init__(self):
        self.learning_data = {}
        self.command_patterns = {}
        self.user_preferences = {}
        self.load_data()
    
    def load_data(self):
        """Load saved learning data"""
        try:
            if os.path.exists('jarvis_data.json'):
                with open('jarvis_data.json', 'r') as f:
                    data = json.load(f)
                    self.learning_data = data.get('learning_data', {})
                    self.user_preferences = data.get('preferences', {})
        except Exception as e:
            print(f"Error loading data: {e}")
    
    def save_data(self):
        """Save learning data"""
        try:
            data = {
                'learning_data': self.learning_data,
                'preferences': self.user_preferences,
                'last_updated': datetime.now().isoformat()
            }
            with open('jarvis_data.json', 'w') as f:
                json.dump(data, f, indent=4)
        except Exception as e:
            print(f"Error saving data: {e}")
    
    def learn_from_interaction(self, user_input, response):
        """Learn from user interactions"""
        if user_input not in self.learning_data:
            self.learning_data[user_input] = {
                'response': response,
                'count': 1,
                'last_used': datetime.now().isoformat()
            }
        else:
            self.learning_data[user_input]['count'] += 1
            self.learning_data[user_input]['last_used'] = datetime.now().isoformat()
        
        self.save_data()
    
    def get_weather(self, city="New York"):
        """Get weather information"""
        try:
            url = f"https://wttr.in/{city}?format=j1"
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                data = response.json()
                current_condition = data['current_condition'][0]['description']
                temperature = data['current_condition'][0]['temp_C']
                return f"The weather in {city} is {current_condition}, with a temperature of {temperature}°C."
        except Exception as e:
            return f"Could not fetch weather: {str(e)}"
        return "Weather service unavailable"
    
    def get_news_headlines(self):
        """Get top news headlines"""
        try:
            url = "https://newsapi.org/v2/top-headlines?country=us"
            # Note: You need to add your API key here
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                data = response.json()
                headlines = [article['title'] for article in data['articles'][:5]]
                return "\n".join(headlines)
        except Exception as e:
            return f"Could not fetch news: {str(e)}"
    
    def get_quote(self):
        """Get an inspirational quote"""
        try:
            url = "https://api.quotable.io/random"
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                data = response.json()
                return f"{data['content']} - {data['author']}"
        except Exception as e:
            return "Could not fetch quote"
    
    def set_user_preference(self, key, value):
        """Set user preference"""
        self.user_preferences[key] = value
        self.save_data()
    
    def get_user_preference(self, key, default=None):
        """Get user preference"""
        return self.user_preferences.get(key, default)
    
    def create_reminder(self, reminder_text, minutes=10):
        """Create a reminder"""
        reminder = {
            'text': reminder_text,
            'created': datetime.now().isoformat(),
            'time': minutes
        }
        if 'reminders' not in self.learning_data:
            self.learning_data['reminders'] = []
        self.learning_data['reminders'].append(reminder)
        self.save_data()
        return f"Reminder set: {reminder_text}"
    
    def get_most_used_commands(self):
        """Get most frequently used commands"""
        sorted_commands = sorted(
            self.learning_data.items(),
            key=lambda x: x[1]['count'],
            reverse=True
        )[:5]
        return sorted_commands
    
    def get_system_insights(self):
        """Get insights about system usage"""
        total_commands = sum(cmd['count'] for cmd in self.learning_data.values() 
                            if isinstance(cmd, dict) and 'count' in cmd)
        unique_commands = len(self.learning_data)
        
        insights = f"""
        SYSTEM INSIGHTS:
        ================
        Total Commands Processed: {total_commands}
        Unique Command Types: {unique_commands}
        Learning Database Size: {len(self.learning_data)} entries
        """
        return insights


class SmartHomeIntegration:
    """
    Integration with smart home devices
    """
    
    def __init__(self):
        self.devices = {}
        self.load_devices()
    
    def load_devices(self):
        """Load smart home device configuration"""
        try:
            if os.path.exists('devices.json'):
                with open('devices.json', 'r') as f:
                    self.devices = json.load(f)
        except Exception as e:
            print(f"Error loading devices: {e}")
    
    def add_device(self, device_name, device_type, ip_address, port=80):
        """Add a smart home device"""
        self.devices[device_name] = {
            'type': device_type,
            'ip': ip_address,
            'port': port,
            'status': 'offline'
        }
        self.save_devices()
        return f"Device {device_name} added successfully"
    
    def control_device(self, device_name, action):
        """Control a smart home device"""
        if device_name not in self.devices:
            return f"Device {device_name} not found"
        
        device = self.devices[device_name]
        # Here you would implement actual device control
        # This is a placeholder for the actual implementation
        return f"Device {device_name}: {action} executed"
    
    def save_devices(self):
        """Save device configuration"""
        try:
            with open('devices.json', 'w') as f:
                json.dump(self.devices, f, indent=4)
        except Exception as e:
            print(f"Error saving devices: {e}")
    
    def get_device_status(self, device_name):
        """Get status of a device"""
        if device_name not in self.devices:
            return f"Device {device_name} not found"
        return self.devices[device_name]
    
    def list_all_devices(self):
        """List all connected devices"""
        return self.devices
