from django.shortcuts import render
from gtts import gTTS

# Create your views here.
def index(request):
    text, l, name = "","",""
    if request.method == "POST":
        text = request.POST.get("text")
        name = request.POST.get("name")
        l = request.POST.get("l")
        
        tts = gTTS(text=text, lang=l)
        tts.save(f"media/tts/{name}.mp3")

    context = {
        "text":text,
        "l":l,
        "name":name,
    }
    return render(request,"tts/index.html",context)