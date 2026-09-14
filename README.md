# J.A.R.V.I.S - AI System with Iron Man Interface

![JARVIS](https://img.shields.io/badge/Status-Active-brightgreen)
![Python](https://img.shields.io/badge/Python-3.8+-blue)
![License](https://img.shields.io/badge/License-MIT-green)

## Overview

JARVIS is an advanced AI assistant system inspired by Tony Stark's AI from Iron Man, featuring:

- **Voice Recognition & Text-to-Speech**: Natural language interaction
- **Iron Man-style HUD Interface**: Real-time holographic visual feedback
- **Dynamic Image Display**: Shows images related to conversation topics
- **Advanced AI Processing**: Wikipedia search, web browsing, time/date management
- **Machine Learning**: Learns from interactions and adapts responses
- **Smart Home Integration**: Control IoT devices
- **Real-time Status Monitoring**: System performance visualization

## Features

### Core AI Engine
- 🎙️ Voice recognition with Google Speech-to-Text
- 🔊 Text-to-speech with natural voice output
- 🧠 Wikipedia integration for knowledge queries
- 🌐 Web browser automation
- ⏰ Time and date management
- 📊 System status reporting

### Iron Man Interface
- 🎨 Holographic HUD design with animated elements
- 💫 Pulsing core with hexagonal patterns
- 📡 Audio wave visualization
- 🖼️ Real-time image display for topics
- 📊 Multi-panel system monitoring
- ⌨️ Keyboard controls for easy interaction

### Advanced Features
- 🤖 Machine learning from interactions
- 🌦️ Weather information
- 📰 News headlines
- 💭 Inspirational quotes
- 🔔 Reminder system
- 🏠 Smart home device control

## Installation

### Requirements
- Python 3.8 or higher
- pip (Python package installer)
- Microphone for voice input
- Internet connection

### Setup Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/mohabtecno-alt/jarvis-ai-ironman.git
   cd jarvis-ai-ironman
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run JARVIS**
   ```bash
   python main.py
   ```

## Usage

### Voice Commands

Once JARVIS starts, speak commands clearly:

**Information Requests**
- "Who is Albert Einstein?"
- "What is machine learning?"
- "Tell me about Python programming"

**Web Actions**
- "Open Google"
- "Google machine learning"
- "Open github.com"

**System Commands**
- "What time is it?"
- "What is today's date?"
- "Status report"
- "Exit" or "Shutdown"

**Greetings**
- "Hello"
- "Hi"
- "Hey JARVIS"

### Keyboard Controls
- **ESC**: Exit the application
- **ALT+F4**: Close window

## Interface Guide

### Main Display Elements

1. **Central Core**: Pulsing holographic core representing JARVIS AI
2. **Audio Waves**: Visible when listening to voice input
3. **Scanning Lines**: Red when processing, green when listening
4. **Information Panels**:
   - **Systems**: CPU, Memory, Status
   - **Audio**: Frequency, Volume, Mode
   - **Network**: Connection, Latency, Bandwidth
5. **Message Display**: Current responses from JARVIS
6. **Image Display**: Photos related to current topic

## Configuration

### User Preferences

Modify preferences in the `jarvis_data.json` file:

```json
{
  "preferences": {
    "user_name": "Sir",
    "voice_speed": 150,
    "voice_volume": 0.9
  }
}
```

### Smart Home Devices

Add devices in `devices.json`:

```json
{
  "living_room_light": {
    "type": "light",
    "ip": "192.168.1.100",
    "port": 80
  }
}
```

## File Structure

```
jarvis-ai-ironman/
├── main.py              # Main application entry point
├── jarvis_core.py       # Core AI engine
├── interface.py         # Iron Man interface
├── advanced_features.py # Machine learning & smart home
├── requirements.txt     # Python dependencies
├── jarvis_data.json     # Learning data (auto-generated)
├── devices.json         # Smart home config
└── images/              # Downloaded topic images
```

## API Keys

For full functionality, you may need API keys for:

1. **Weather API** (Optional)
   - Sign up at https://www.weatherapi.com/
   - Add API key to environment variables

2. **News API** (Optional)
   - Sign up at https://newsapi.org/
   - Add API key to environment variables

## Troubleshooting

### Microphone Issues
- Check microphone permissions
- Test with other audio applications
- Ensure microphone is connected

### Speech Recognition Errors
- Speak clearly and at normal pace
- Reduce background noise
- Check internet connection (uses Google's API)

### Interface Display Issues
- Ensure adequate screen resolution (1400x900 recommended)
- Update graphics drivers
- Check pygame installation

### Image Download Problems
- Check internet connection
- Verify `images/` directory exists
- Try different search topics

## Advanced Customization

### Change Interface Colors

Edit `interface.py` color constants:

```python
self.CYAN = (0, 200, 255)
self.GOLD = (255, 184, 82)
self.RED = (220, 20, 60)
```

### Modify AI Behavior

Extend `jarvis_core.py` with new commands:

```python
elif 'custom command' in command:
    return "Custom response"
```

## Performance Tips

- Close background applications for better performance
- Ensure stable internet connection
- Use microphone close to mouth for accurate recognition
- Run on system with at least 4GB RAM

## Future Enhancements

- [ ] Natural Language Processing improvements
- [ ] Facial recognition integration
- [ ] Advanced emotion detection
- [ ] IoT device dashboard
- [ ] Mobile app companion
- [ ] Cloud synchronization
- [ ] Multi-language support
- [ ] Custom voice profiles

## License

MIT License - See LICENSE file for details

## Credits

Inspired by:
- Iron Man AI System (Marvel)
- Modern AI Assistants
- Open-source community

## Support

For issues, questions, or suggestions:
1. Open an issue on GitHub
2. Check existing documentation
3. Review troubleshooting section

## Disclaimer

This project is for educational and entertainment purposes. It's not affiliated with Marvel or Disney.

---

**"I am Iron Man" - Tony Stark** 🦾
