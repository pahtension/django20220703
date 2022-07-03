from django.shortcuts import render
from googletrans import Translator
import googletrans

translator = Translator()
# Create your views here.
# ll = {}
# for k,v in googletrans.LANGUAGES:
#     name = translator.translate(v,src="en",dest=k).text
#     ll[k] = name

ll = googletrans.LANGUAGES
ll["ko"] = "korean(한국어)"

def index(request):
    text,text2,l1,l2 = "","","",""
    if request.method == "POST":
        text = request.POST.get("text")
        l1 = request.POST.get("l1")
        l2 = request.POST.get("l2")
        text2 = translator.translate(text, src=l1, dest=l2).text
    context = {
        "text":text,
        "text2":text2,
        "l1":l1,
        "l2":l2,
        "ndict":ll,
    }
    return render(request, "trans/index.html",context)