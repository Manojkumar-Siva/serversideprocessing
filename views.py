from django.shortcuts import render

def areacalculation(request):
    context = {}
    context["area"] = "0"
    context["l"] = "0"
    context["w"] = "0"
    if request.method == "POST":
        l= request.POST.get("length","0")
        w = request.POST.get("width","0")
        area = ((int(l) * int(w)))
        context["area"]= area
        context["l"] = l
        context["w"] = w
    return render(request,"mathapp/area.html",context)
