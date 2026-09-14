# JARVIS AI System - Complete Setup Guide

## 📋 Prerequisites

Before starting, ensure you have:
- Python 3.8 or later installed
- pip (comes with Python)
- A working microphone
- Internet connection
- At least 4GB RAM

## 🚀 Step-by-Step Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/mohabtecno-alt/jarvis-ai-ironman.git
cd jarvis-ai-ironman
```

### Step 2: Create Virtual Environment (Recommended)

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

**Note:** This may take a few minutes. PyAudio might require additional setup on some systems.

#### PyAudio Installation Troubleshooting

**Windows:**
```bash
pip install pipwin
pipwin install pyaudio
```

**macOS:**
```bash
brew install portaudio
pip install pyaudio
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt-get install portaudio19-dev
pip install pyaudio
```

### Step 4: Test Microphone

Create a test file `test_mic.py`:

```python
import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Listening...")
    audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print(f"Recognized: {text}")
    except:
        print("Could not understand")
```

Run it:
```bash
python test_mic.py
```

### Step 5: Launch JARVIS

```bash
python main.py
```

You should see:
1. The Iron Man-style interface loading
2. JARVIS greeting message
3. Status showing "STANDBY"

## 🎙️ First Run

1. **Wait for greeting**: JARVIS will greet you and show a message
2. **Speak clearly**: When the interface shows "LISTENING", speak your command
3. **Wait for response**: JARVIS will process and respond
4. **See the interface update**: Watch the visual feedback in real-time

## 🛠️ Configuration

### Adjust Voice Settings

Edit `jarvis_core.py`, line ~23:

```python
self.engine.setProperty('rate', 150)      # Speech speed (100-300)
self.engine.setProperty('volume', 0.9)    # Volume (0.0-1.0)
```

### Customize Interface Colors

Edit `interface.py`, lines ~30-40:

```python
self.CYAN = (0, 200, 255)      # Change to your color (RGB)
self.GOLD = (255, 184, 82)
self.RED = (220, 20, 60)
```

### Set User Name

Edit `main.py`, line ~20:

```python
self.user_name = "Your Name"   # JARVIS will use this in greetings
```

## 📚 Example Commands

### Information Queries
```
"Who is Elon Musk?"
"What is artificial intelligence?"
"Tell me about quantum computing"
```

### Web Actions
```
"Open Google"
"Google weather forecast"
"Open YouTube"
```

### System Commands
```
"What time is it?"
"Today's date?"
"Status report"
"Your system status?"
```

### Control
```
"Exit"
"Shutdown"
"Stop"
```

## 🐛 Troubleshooting

### Issue: "No module named 'pygame'"
**Solution:**
```bash
pip install pygame
```

### Issue: "Microphone not recognized"
**Solutions:**
1. Check Windows/Mac/Linux sound settings
2. Test with another application
3. Restart the application
4. Try: `python -m speech_recognition`

### Issue: "ModuleNotFoundError: No module named 'pyttsx3'"
**Solution:**
```bash
pip install pyttsx3
```

### Issue: "No internet connection" error
**Solution:**
- Check your internet connection
- Some features require internet
- Offline mode coming soon

### Issue: "Cannot find 'portaudio'"
**Solution:**
See PyAudio Installation Troubleshooting section above

### Issue: Interface runs slowly
**Solutions:**
1. Close background applications
2. Reduce screen resolution if needed
3. Update graphics drivers
4. Check system RAM usage

## 🔧 Advanced Setup

### Enable Weather API

1. Sign up at [weatherapi.com](https://weatherapi.com)
2. Get your API key
3. Add to `advanced_features.py`:

```python
API_KEY = "your_api_key_here"
```

### Set Up Smart Home Integration

1. Create `devices.json`:

```json
{
  "bedroom_light": {
    "type": "smart_light",
    "ip": "192.168.1.100",
    "port": 8080
  },
  "living_room_speaker": {
    "type": "speaker",
    "ip": "192.168.1.101",
    "port": 8080
  }
}
```

2. Modify `main.py` to include:

```python
from advanced_features import SmartHomeIntegration

self.smart_home = SmartHomeIntegration()
```

## 📊 Monitoring Performance

### Check Learning Data

View what JARVIS has learned:

```bash
cat jarvis_data.json
```

### View Command History

Add this to `main.py`:

```python
print(self.core.get_command_history())
```

## 🎓 Learning Resources

- **Speech Recognition**: [SpeechRecognition Docs](https://github.com/Uberi/speech_recognition)
- **Text-to-Speech**: [pyttsx3 Docs](https://pyttsx3.readthedocs.io/)
- **Pygame**: [Pygame Documentation](https://www.pygame.org/docs/)
- **Python Audio**: [PyAudio Documentation](https://people.csail.mit.edu/hubert/pyaudio/)

## 🚨 Common Issues Quick Reference

| Issue | Quick Fix |
|-------|----------|
| Microphone errors | Install portaudio dependencies |
| Module not found | Run `pip install -r requirements.txt` |
| Internet errors | Check connection, restart app |
| Slow performance | Close other apps, update drivers |
| Voice not working | Check microphone permissions |
| Interface doesn't show | Ensure 1400x900 resolution minimum |

## ✅ Verification Checklist

- [ ] Python 3.8+ installed
- [ ] All requirements installed
- [ ] Microphone working
- [ ] Internet connection active
- [ ] Can run `python main.py` without errors
- [ ] Interface displays correctly
- [ ] Microphone captures audio
- [ ] JARVIS responds to commands

## 🎉 You're All Set!

Enjoy your personal JARVIS system! For support, check the main README.md or open an issue on GitHub.

---

**Pro Tips:**
- Speak clearly for better recognition
- Keep microphone 6-12 inches from mouth
- Use simple, direct commands
- Check internet for best results
- Have fun experimenting!
