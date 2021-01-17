from django.shortcuts import render ,redirect
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
		if(len(output)<10):
			length_of_list=len(output)
			for i in range(length_of_list,10):
				output.append(0)
		# form =HomeForm()
		dta=Home(tag=t,tag1=output[0],tag2=output[1],tag3=output[2],tag4=output[3],tag5=output[4],tag6=output[5],tag7=output[6],tag8=output[7],tag9=output[8],tag10=output[9])
		dta.save()
		return redirect("home_view/")

	else:
		form=HomeForm()


	
	return render(request,'home.html',{'form':form})# Create your views here.

def home_view(request):
	objs=Home.objects.all()
	return render(request,'title.html',{'objs':objs})