from django.shortcuts import render
from .forms import ImageUploadForm

#for Deep Learning model
import keras
from keras.applications.resnet50 import ResNet50
from keras.applications.resnet50 import preprocess_input, decode_predictions
from keras.preprocessing import image
import numpy as np


# Create your views here.
def home(request):
    return render(request, 'home.html')

def imageupload(request):
    return render(request, 'imageupload.html')

def result(request):
    form = ImageUploadForm(request.POST, request.FILES)
    if form.is_valid():
        handle_uploaded_file(request.FILES['image'])

        #the pre-trained Deep Learning model
        model = ResNet50(weights='imagenet')
        img_path = 'img.jpg' #storing the uploaded image
        #to load,process and predict
        img = keras.utils.load_img(img_path, target_size=(224, 224))
        x = keras.utils.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        x = preprocess_input(x)

        preds = model.predict(x)
        print('Predicted:', decode_predictions(preds, top=3)[0])

        #to show it in the result page
        html = decode_predictions(preds, top=3)[0]
        res = []
        for e in html:
            res.append((e[1],np.round(e[2]*100,2))) # shows in %
        return render(request,'result.html',{'res':res})
    
    return render(request,'result.html')

def handle_uploaded_file(f):
    with open('img.jpg', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)