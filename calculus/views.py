from django.shortcuts import render
from . import ratios,grow_fact ,grow_plan,itog , inf_mon, inf_kva, inf_day,inf_coef,\
    income,bez_sutok, dev_mon,dev_kva,dev_day




def index(request):
    return render(request,'calculus/index.html')

def view_rat(request):
    data = ratios.summoner()
    return render(request,'calculus/index.html',{'data':data})

def view_grow_fact(request):
    data = grow_fact.summoner()
    return render(request,'calculus/index.html',{'data':data})

def view_grow_plan(request):
    data = grow_plan.summoner()
    return render(request,'calculus/index.html',{'data':data})


def view_itog(request):
    data = itog.summoner()
    return render(request,'calculus/index.html',{'data':data})


def view_inf_mon(request):
    data = inf_mon.summoner()
    return render(request,'calculus/index.html',{'data':data})


def view_inf_kva(request):
    data = inf_kva.summoner()
    return render(request,'calculus/index.html',{'data':data})


def view_inf_day(request):
    data = inf_day.summoner()
    return render(request,'calculus/index.html',{'data':data})

def view_inf_coef(request):
    data = inf_coef.summoner()
    return render(request,'calculus/index.html',{'data':data})


def view_income(request):
    data = income.summoner()
    return render(request,'calculus/index.html',{'data':data})


def view_bez_sutok(request):
    data = bez_sutok.summoner()
    return render(request,'calculus/index.html',{'data':data})



def view_dev_mon(request):
    data = dev_mon.summoner()
    return render(request,'calculus/index.html',{'data':data})

def view_dev_kva(request):
    data = dev_kva.summoner()
    return render(request,'calculus/index.html',{'data':data})

def view_dev_day(request):
    data = dev_day.summoner()
    return render(request,'calculus/index.html',{'data':data})