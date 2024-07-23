from django.shortcuts import render, redirect
from .models import Problem
from .forms import ProblemForm


def problems(request):
    problems = Problem.objects.all()
    context = {"problems": problems}
    return render(request, "helpdesk/problems.html", context)


def indproblem(request, id):
    problem = Problem.objects.get(id=id)
    context = {"problem": problem}
    return render(request, "helpdesk/indproblem.html", context)


def home(request):
    if request.method == 'POST':
        regnum = request.POST['regnum']
        problems = Problem.objects.filter(regnum=regnum)
        return render(request, 'helpdesk/home.html', {'problems': problems})
    return render(request, 'helpdesk/home.html')


def model_form(request):
  form = ProblemForm()
  if request.method=='POST':
    form = ProblemForm(request.POST)
    if form.is_valid():
      form.save()
      print("Successfully saved!")
      return redirect('problems')
    else:
      form = ProblemForm()
      print("Unsuccessful save")
  return render(request,'helpdesk/problemform.html',{'form':form})

