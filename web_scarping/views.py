from django.shortcuts import render
from django.http import HttpResponse
from .forms import HomeForm
from .models import Home
from .selenium import Scrapping


# Create your views here.
def home(request):
	form = HomeForm(request.POST or None)
	if form.is_valid():
		output=Scrapping(form.cleaned_data['tag'])
		# text=form.cleaned_data["tag"]
		t=form.cleaned_data['tag']
		# form =HomeForm()
		dta=Home(tag=t,tag1=output[0],tag2=output[1],tag3=output[2],tag4=output[3],tag5=output[4],tag6=output[5],tag7=output[6],tag8=output[7],tag9=output[8],tag10=output[9])
		dta.save()
	else:
		form=HomeForm()

	
	return render(request,'home.html',{'form':form})




	



