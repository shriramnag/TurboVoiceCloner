# TurboVoiceCloner
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/shriramnag/TurboVoiceCloner/blob/main/TurboVoiceCloner.ipynb)
# 🎙️ TurboVoiceCloner
An Open-Source, High-Speed AI Voice Cloning Web App.

## ✨ Features
- **Turbo High Speed:** Optimized for Google Colab T4 GPU for near-instant voice generation.
- **Silence Remover:** Built-in automatic silence remover to provide clean audio output.
- **Free for Life:** Uses Coqui TTS (YourTTS) and RVC models, ensuring no subscription or hidden costs.
- **Unlimited Generation:** No limits on the number of clones or length of audio.
- **Mobile Friendly:** Access the web interface from any device via Gradio.

## 🛠️ Setup
1. Open Google Colab.
2. Clone this repository.
3. Install requirements: `pip install -r requirements.txt`.
4. Run `app.py`.

5. ## 🛠️ Troubleshooting (Python 3.12+ Fix)

If you are using Google Colab and encounter a `ModuleNotFoundError: No module named 'TTS'` or installation errors, it is because Colab's default Python (3.12) is not yet compatible with Coqui-TTS.

**Fix:** Run the following command in a Colab cell to force a compatible environment:

```python
# Force install Python 3.10 and Coqui-TTS
!sudo apt-get install python3.10 python3.10-dev python3.10-distutils -y
!wget [https://bootstrap.pypa.io/get-pip.py](https://bootstrap.pypa.io/get-pip.py) && python3.10 get-pip.py
!python3.10 -m pip install coqui-tts gradio==4.44.1 pydub



## 📜 Disclaimer
This project is for educational purposes only. Always ensure you have permission before cloning someone's voice.
