# JARVIS AI - PyCharm Setup Guide

## Method 1: Clone Repository in PyCharm (Recommended)

### Step 1: Open PyCharm
- Launch PyCharm Professional or Community Edition

### Step 2: Get from Version Control
1. Click **File** → **New** → **Project from Version Control**
2. Or click **Get from VCS** on the Welcome screen

### Step 3: Enter Repository URL
1. Select **Git** from the dropdown
2. Enter URL: `https://github.com/mohabtecno-alt/jarvis-ai-ironman.git`
3. Choose your directory location (e.g., `C:\Users\YourName\PycharmProjects\jarvis-ai-ironman`)
4. Click **Clone**

### Step 4: Wait for Project to Load
- PyCharm will download and open the project
- The IDE will automatically detect Python files

---

## Method 2: Manual Setup (If Clone Fails)

### Step 1: Download as ZIP
1. Go to https://github.com/mohabtecno-alt/jarvis-ai-ironman
2. Click the green **Code** button
3. Select **Download ZIP**
4. Extract the ZIP file to your desired location

### Step 2: Open in PyCharm
1. Launch PyCharm
2. Click **File** → **Open**
3. Navigate to the extracted folder
4. Click **Open**
5. When prompted, click **Trust Project**

### Step 3: Configure Python Interpreter
1. Go to **File** → **Settings** (or **PyCharm** → **Preferences** on Mac)
2. Navigate to **Project: jarvis-ai-ironman** → **Python Interpreter**
3. Click the gear ⚙️ icon → **Add**
4. Select **Add Local Interpreter** → **Existing Environment** or **New Environment**
5. If creating new:
   - Choose **Virtualenv** or **Conda**
   - Set location: `venv` inside project folder
   - Python version: 3.8+
   - Click **OK**

---

## Step 4: Install Dependencies

### Option A: Using PyCharm UI
1. PyCharm may show a notification about missing packages
2. Click **Install requirements** if prompted
3. Or go to **Terminal** tab and see if it auto-installs

### Option B: Using Terminal in PyCharm
1. Open the **Terminal** tab at bottom of PyCharm
2. Run this command:

```bash
pip install -r requirements.txt
```

3. Wait for all packages to install (may take 3-5 minutes)

### Option C: Manual Installation
1. **Terminal** → **New Terminal**
2. Copy and paste each command:

```bash
pip install pygame==2.2.1
pip install pillow==10.0.0
pip install speech-recognition==3.10.0
pip install pyttsx3==2.90
pip install numpy==1.24.3
pip install requests==2.31.0
```

---

## Step 5: Fix PyAudio (Common Issue)

### If you get "No module named 'pyaudio'" error:

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

---

## Step 6: Configure PyCharm for JARVIS

### Set Up Run Configuration
1. Click **Run** → **Edit Configurations**
2. Click **+** (Add new configuration)
3. Select **Python**
4. Set these values:
   - **Name**: `JARVIS AI`
   - **Script path**: `/path/to/main.py` (select from browser)
   - **Python interpreter**: Select your project interpreter
   - **Working directory**: Project root folder
   - Click **OK**

### Now You Can Run:
1. Click the **Run** button (green ▶️) or press **Shift + F10**
2. Or right-click on `main.py` → **Run 'main'**

---

## Step 7: Configure Microphone & Audio

### Windows Users
1. **Settings** → **Sound settings**
2. Make sure your microphone is set as default
3. Test microphone volume

### macOS Users
1. **System Preferences** → **Sound** → **Input**
2. Select your microphone
3. Check input level

### Linux Users
1. Open **Sound Settings**
2. Select correct input device
3. Check ALSA/Pulse Audio config

### In PyCharm
If microphone doesn't work, run this in Terminal:
```bash
python test_mic.py
```

Create `test_mic.py` in project root:
```python
import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Listening... speak now!")
    audio = r.listen(source, timeout=10)
    try:
        text = r.recognize_google(audio)
        print(f"✓ Microphone works! Recognized: {text}")
    except Exception as e:
        print(f"✗ Error: {e}")
```

---

## Step 8: Debugging in PyCharm

### View Console Output
- Run the project and look at the **Run** tab at bottom
- All print statements appear here
- Check for error messages

### Set Breakpoints
1. Click on line number to add breakpoint (red dot appears)
2. Run with **Debug** button (🐛)
3. Step through code with **Step Over** (F10)

### View Variables
- When paused at breakpoint, see variables in **Variables** panel
- Hover over variables in code to see values

---

## Common PyCharm Issues & Fixes

### Issue: "Python interpreter not configured"
**Fix:**
1. File → Settings → Project → Python Interpreter
2. Click ⚙️ → Add
3. Create new virtual environment
4. Select Python 3.8+

### Issue: "Terminal doesn't recognize commands"
**Fix:**
1. Close terminal (X button)
2. Open new terminal
3. Make sure you see `(venv)` at start of line
4. If not, run: `venv\Scripts\activate` (Windows) or `source venv/bin/activate` (Mac/Linux)

### Issue: "ModuleNotFoundError" for any package
**Fix:**
1. Go to **File** → **Settings** → **Python Interpreter**
2. Click **+** button to add package
3. Search for package name
4. Click **Install**

### Issue: Microphone not working
**Fix:**
1. Check Windows/Mac/Linux sound settings
2. In PyCharm, run test_mic.py (see Step 7)
3. May need to run PyCharm as Administrator

### Issue: "pygame display mode error"
**Fix:**
1. Right-click on `main.py`
2. Select **Modify Run Configuration**
3. Add to **Environment variables**: `SDL_VIDEODRIVER=windows` (Windows)

---

## Verify Everything Works

### Checklist
- [ ] Project opens without errors
- [ ] Python interpreter selected
- [ ] All requirements installed (check Terminal)
- [ ] `main.py` is visible in project
- [ ] Can run `main.py` with Run button (▶️)
- [ ] JARVIS window opens with Iron Man interface
- [ ] Microphone responds (says "Listening...")
- [ ] Can speak commands

---

## Quick Start Commands (In PyCharm Terminal)

```bash
# Check Python version
python --version

# Check if all packages installed
pip list

# Run JARVIS
python main.py

# Test microphone
python test_mic.py

# Install missing package
pip install package_name
```

---

## Alternative: Use PyCharm's Built-in Package Manager

1. **File** → **Settings** → **Project: jarvis-ai-ironman** → **Python Interpreter**
2. You'll see list of installed packages
3. Click **+** to add new packages
4. Search for: `pygame`, `speech-recognition`, `pyttsx3`, etc.
5. Click **Install** for each

---

## Pro Tips

✅ **Use Virtual Environment**: Keeps project dependencies isolated  
✅ **Check Python Path**: Ensure interpreter matches project  
✅ **Monitor Console**: Watch for error messages during runtime  
✅ **Test Microphone Early**: Verify audio input before running full app  
✅ **Use Debugging**: Set breakpoints to understand flow  
✅ **Keep Requirements Updated**: Run `pip install --upgrade -r requirements.txt`  

---

## Need Help?

1. Check **Run** tab console for error messages
2. Use **Debug** mode to step through code
3. Check microphone permissions in OS settings
4. Verify internet connection (needed for image downloads)
5. Make sure screen resolution is at least 1400x900

## You're Ready! 🎉

Once setup is complete, run `main.py` and enjoy your JARVIS AI system with Iron Man interface!

---

**Still having issues?** Create a test file and run it to diagnose:

```python
# test_setup.py
print("✓ Python works")
import pygame
print("✓ Pygame installed")
import speech_recognition
print("✓ Speech Recognition installed")
import pyttsx3
print("✓ Text-to-Speech installed")
print("✓ All systems go! Run main.py now")
```
