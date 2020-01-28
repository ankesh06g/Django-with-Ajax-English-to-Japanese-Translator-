from django.shortcuts import render
from django.http import HttpResponse
from googletrans import Translator

def home(request):
    return render(request, 'index.html')

def translator(request):
    if request.method == 'POST':   

        # Taking input from user
        eng_text = request.POST['input_text']

        # Creatin class object
        translator = Translator()

        # Calling function translate
        jap_text = translator.translate(eng_text, dest='ja', src='en')

    # returns to AJAX request
    return HttpResponse(jap_text.text)

