from django.shortcuts import render
from django.http import HttpResponse
from .models import Calculator
# Create your views here.

def index(response):
	val = Calculator.objects.all()
	inp = "inp"
	inp2 = 0
	inp4 = 0
	inp5 = 0
	inp6 = 0
	inp7 = 0
	inp8 = 0
	inp9 = 0
	v2 = 0
	v4 = 0
	v5 = 0
	v6 = 0
	v7 = 0
	v8 = 0
	v9 = 0

	ttlv = 0
	ttln = 0

	if response.method == 'POST':
		
		if response.POST.get("done"):
			def update(n,l):
				try:
					v = response.POST.get(str(n))
					inp = str(int(v)*l)
				except:
					inp = 0
				return inp
			try:
				inp2 = update(2,2000)
				inp4 = update(4,500)
				inp5 = update(5,200)
				inp6 = update(6,100)
				inp7 = update(7,50)
				inp8 = update(8,20)
				inp9 = update(9,10)

				ttln = int(inp2)+int(inp4)+int(inp5)+int(inp6)+int(inp7)+int(inp8)+int(inp9)
			except ValueError:
				pass

			try:
				v2 = response.POST.get("2")
				v4 = response.POST.get("4")
				v5 = response.POST.get("5")
				v6 = response.POST.get("6")
				v7 = response.POST.get("7")
				v8 = response.POST.get("8")
				v9 = response.POST.get("9")

				ttlv = int(v2)+int(v4)+int(v5)+int(v6)+int(v7)+int(v8)+int(v9)

			except:
				pass

		else :
			# inp = 0
			pass
		return render(response, "main/home.html",{ 
	        "val" : val,
	        "inp" : inp,
	        "inp2" : inp2,
	        "inp4" : inp4,
	        "inp5" : inp5,
	        "inp6" : inp6,
	        "inp7" : inp7,
	        "inp8" : inp8,
	        "inp9" : inp9,
	        "v2" : v2,
	        "v4" : v4,
	        "v5" : v5,
	        "v6" : v6,
	        "v7" : v7,
	        "v8" : v8,
	        "v9" : v9,
	        "ttlv" : ttlv,
	        "ttln" : ttln,
	    })
	context = { 
        "val" : val,
        "inp" : inp,
        "inp2" : inp2,
        "inp4" : inp4,
        "inp5" : inp5,
        "inp6" : inp6,
        "inp7" : inp7,
        "inp8" : inp8,
        "inp9" : inp9,
        "v2" : v2,
        "v4" : v4,
        "v5" : v5,
        "v6" : v6,
        "v7" : v7,
        "v8" : v8,
        "v9" : v9,
        "ttlv" : ttlv,
        "ttln" : ttln,
    }
	return render(response, "main/home.html", context)