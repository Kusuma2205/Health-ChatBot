from gtts import gTTS
from googletrans import Translator
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Disease
from .remedies import remedies
import base64
from io import BytesIO
import difflib

translator = Translator()

# Map for gTTS supported language codes
SUPPORTED_TTS_LANGS = {
    "en": "en",   # English
    "hi": "hi",   # Hindi
    "te": "te",   # Telugu
    "ta": "ta",   # Tamil
    "bn": "bn",   # Bengali
    "fr": "fr",   # French
    "es": "es",   # Spanish
}

def get_best_match(query, dictionary):
    """Find closest matching key from remedies.py"""
    query = query.lower().strip()
    matches = difflib.get_close_matches(query, dictionary.keys(), n=1, cutoff=0.6)
    if matches:
        return dictionary[matches[0]]
    return None

@api_view(["POST"])
def chat_view(request):
    user_message = request.data.get("message", "").strip()
    target_lang = request.data.get("language")  # frontend language

    if not user_message:
        return Response({"reply": "Please enter a symptom or disease."})

    # Detect input language
    if not target_lang:
        detected_lang = translator.detect(user_message).lang
    else:
        detected_lang = target_lang

    # Translate to English for searching
    try:
        english_text = translator.translate(user_message, dest="en").text.lower().strip()
    except Exception as e:
        print(f"Translation Error: {e}")
        return Response({"reply": "Sorry, translation failed."})

    # Try to fetch remedy
    reply = None
    try:
        disease = Disease.objects.get(name__icontains=english_text)
        reply = disease.remedy
    except Disease.DoesNotExist:
        reply = remedies.get(english_text)  # exact
        if not reply:
            reply = get_best_match(english_text, remedies)  # fuzzy

    if not reply:
        reply = "Sorry, I don't have information about that disease."

    # Translate reply back
    try:
        translated_reply = translator.translate(reply, dest=detected_lang).text
    except Exception as e:
        print(f"Reply Translation Error: {e}")
        translated_reply = reply

    # TTS
    audio_base64 = None
    try:
        if detected_lang in SUPPORTED_TTS_LANGS:
            tts = gTTS(translated_reply, lang=SUPPORTED_TTS_LANGS[detected_lang])
            audio_fp = BytesIO()
            tts.write_to_fp(audio_fp)
            audio_fp.seek(0)
            audio_base64 = base64.b64encode(audio_fp.read()).decode("utf-8")
    except Exception as e:
        print(f"TTS Error: {e}")

    return Response({
        "reply": translated_reply,
        "audio": audio_base64
    })
