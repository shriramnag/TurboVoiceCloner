# @title 🚀 FIXED: Turbo Voice Cloner (Silence Remover Fixed)
import os
import torch
import gradio as gr
from TTS.api import TTS
from pydub import AudioSegment, silence

# 1. Install/Verify Dependencies
print("Checking components...")
!pip install -q TTS pydub gradio

# 2. Setup Device and Model
device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Running on: {device}")

# TTS 5 Free Model Loading
if 'tts' not in locals():
    print("Loading TTS Engine (Turbo)...")
    tts = TTS("tts_models/multilingual/multi-dataset/your_tts").to(device)

# 3. Fixed Processing Function
def process_voice(text, reference_audio, remove_silence_toggle):
    if not reference_audio or not text:
        return None, "Error: Text और Voice Sample दोनों जरूरी हैं!"
    
    try:
        output_path = "temp_output.wav"
        final_output = "cloned_voice.wav"
        
        # Turbo Generation
        tts.tts_to_file(
            text=text, 
            speaker_wav=reference_audio, 
            language="en", 
            file_path=output_path
        )
        
        # 4. Silence Remover (FIXED LOGIC)
        if remove_silence_toggle:
            audio = AudioSegment.from_file(output_path)
            # Silence detect करके केवल आवाज वाला हिस्सा रखना
            chunks = silence.split_on_silence(
                audio, 
                min_silence_len=300, 
                silence_thresh=-40, 
                keep_silence=100
            )
            combined = AudioSegment.empty()
            for chunk in chunks:
                combined += chunk
            combined.export(final_output, format="wav")
        else:
            if os.path.exists(final_output): os.remove(final_output)
            os.rename(output_path, final_output)
            
        return final_output, "Success! Voice Generated at Turbo Speed."
    
    except Exception as e:
        return None, f"Error occurred: {str(e)}"

# 5. UI Design
with gr.Blocks(title="Turbo Voice Cloner") as demo:
    gr.Markdown("# 🎙️ Turbo Voice Cloner (Fixed Version)")
    
    with gr.Row():
        with gr.Column():
            input_text = gr.Textbox(label="Text यहाँ लिखें", placeholder="Hello friend...", lines=3)
            ref_audio = gr.Audio(label="Voice Sample अपलोड करें", type="filepath")
            silence_btn = gr.Checkbox(label="Silence Remover Button (Enabled)", value=True)
            generate_btn = gr.Button("🚀 GENERATE NOW", variant="primary")
            
        with gr.Column():
            audio_output = gr.Audio(label="Generated Audio")
            status_msg = gr.Label(label="Status")

    generate_btn.click(
        fn=process_voice, 
        inputs=[input_text, ref_audio, silence_btn], 
        outputs=[audio_output, status_msg]
    )

demo.launch(share=True, debug=True)
