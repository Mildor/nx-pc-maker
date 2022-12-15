from django.shortcuts import render
from .models import *
from django.forms import ModelForm
from django import forms
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, resolve
from django.contrib.auth.models import User
from django.contrib.auth import logout


def exit(request):
  logout(request)
  return HttpResponseRedirect(reverse('home'))


def myConfigsIC(request):
  if request.user.is_authenticated:
    return myConfigs(request)
  else:
    return ordinateur(request)


def myConfigs(request):
  if request.method == "POST":
    ordinateur_form_var = OrdinateurForm(request.POST)
    if ordinateur_form_var.is_valid():
      ordinateur_form_user = ordinateur_form_var.save(commit=False)
      ordinateur_form_user.user = User.objects.get(pk=request.user.id)
      ordinateur_form_user.save()
      ordinateur_form_var.save_m2m()
  ordinateurs = Ordinateur.objects.all().filter(user=User.objects.get(id=request.user.id))
  form = OrdinateurForm()
  return render(request, 'ordinateur.html',
                {'ordinateurs': ordinateurs, 'new_ordinateur': form, 'cur_user': request.user})


def home(request):
  return render(request, 'home.html')


def motherBoard(request):
  if request.method == "POST":
    mb_form_var = MotherBoardForm(request.POST)
    if mb_form_var.is_valid():
      mb_form_var.save()
  motherBoards = MotherBoard.objects.all().order_by('id')
  form = MotherBoardForm()
  return render(request, 'motherBoard.html', {'motherBoards': motherBoards, 'new_mb': form})


def stockage(request):
  if request.method == "POST":
    stock_form_var = StockageForm(request.POST)
    if stock_form_var.is_valid():
      stock_form_var.save()
  stockages = Stockage.objects.all().order_by('type')
  form = StockageForm()
  return render(request, 'stockage.html', {'stockages': stockages, 'new_stock': form})


def processeur(request):
  if request.method == "POST":
    proco_form_var = ProcesseurForm(request.POST)
    if proco_form_var.is_valid():
      proco_form_var.save()
  processeurs = Processeur.objects.all().order_by('marque')
  form = ProcesseurForm()
  return render(request, 'processeur.html', {"processeurs": processeurs, 'new_proco': form})


def ram(request):
  if request.method == "POST":
    ram_form_var = RAMForm(request.POST)
    if ram_form_var.is_valid():
      ram_form_var.save()
  rams = RAM.objects.all().order_by('marque')
  form = RAMForm()
  return render(request, 'ram.html', {"rams": rams, 'new_ram': form})


def gpu(request):
  if request.method == "POST":
    gpu_form_var = GPUForm(request.POST)
    if gpu_form_var.is_valid():
      gpu_form_var.save()
  gpus = GPU.objects.all().order_by('marque')
  form = GPUForm()
  return render(request, 'gpu.html', {'gpus': gpus, 'new_gpu': form})


def ordinateur(request):
  if request.method == "POST":
    ordinateur_form_var = OrdinateurForm(request.POST)
    if ordinateur_form_var.is_valid():
      ordinateur_form_user = ordinateur_form_var.save(commit=False)
      ordinateur_form_user.user = User.objects.get(pk=request.user.id)
      ordinateur_form_user.save()
      ordinateur_form_var.save_m2m()
  ordinateurs = Ordinateur.objects.all()
  form = OrdinateurForm()
  return render(request, 'ordinateur.html',
                {'ordinateurs': ordinateurs, 'new_ordinateur': form, 'cur_user': request.user})


class OrdinateurForm(ModelForm):
  def __init__(self, *args, **kwargs):
    super(OrdinateurForm, self).__init__(*args, **kwargs)
    for visible in self.visible_fields():
      visible.field.widget.attrs['data-cy'] = "Ordinateur_"+visible.label
    self.fields["alimentation"].label = "Alimentation"
    self.gpu = forms.MultipleChoiceField(widget=forms.SelectMultiple, choices=GPU.objects.all(), required=False)
    self.stockage = forms.MultipleChoiceField(widget=forms.SelectMultiple, choices=Stockage.objects.all(),
                                              required=False)
    self.processeur = forms.MultipleChoiceField(widget=forms.SelectMultiple, choices=Processeur.objects.all(),
                                                required=False)
    self.ram = forms.MultipleChoiceField(widget=forms.SelectMultiple, choices=RAM.objects.all(), required=False)
    self.motherBoard = forms.MultipleChoiceField(widget=forms.SelectMultiple, choices=MotherBoard.objects.all(),
                                                 required=False)

  class Meta:
    model = Ordinateur
    fields = ("alimentation", "gpu", "stockage", "processeur", "ram", 'motherBoard')


class MotherBoardForm(ModelForm):
  def __init__(self, *args, **kwargs):
    super(MotherBoardForm, self).__init__(*args, **kwargs)
    for visible in self.visible_fields():
      visible.field.widget.attrs['data-cy'] = "motherboard_"+visible.label
    self.fields["marque"].label = "Marque"
    self.fields["chipset"].label = "Chipset"

  class Meta:
    model = MotherBoard
    fields = ("marque", "chipset")


class GPUForm(ModelForm):
  def __init__(self, *args, **kwargs):
    super(GPUForm, self).__init__(*args, **kwargs)
    for visible in self.visible_fields():
      visible.field.widget.attrs['data-cy'] = "gpu_"+visible.label
    self.fields["marque"].label = "Marque"
    self.fields["modele"].label = "Modele"

  class Meta:
    model = GPU
    fields = ("marque", "modele")


class StockageForm(ModelForm):
  def __init__(self, *args, **kwargs):
    super(StockageForm, self).__init__(*args, **kwargs)
    for visible in self.visible_fields():
      visible.field.widget.attrs['data-cy'] = "stockage_"+visible.label
    self.fields["type"].label = "Type"
    self.fields["taille"].label = "Taille"

  class Meta:
    model = Stockage
    fields = ("type", "taille")


class ProcesseurForm(ModelForm):
  def __init__(self, *args, **kwargs):
    super(ProcesseurForm, self).__init__(*args, **kwargs)
    for visible in self.visible_fields():
      visible.field.widget.attrs['data-cy'] = "processeur_"+visible.label
    self.fields["marque"].label = "Marque"
    self.fields["categorie"].label = "Categorie"
    self.fields["modele"].label = "Modele"

  class Meta:
    model = Processeur
    fields = ("marque", "categorie", 'modele')


class RAMForm(ModelForm):
  def __init__(self, *args, **kwargs):
    super(RAMForm, self).__init__(*args, **kwargs)
    for visible in self.visible_fields():
      visible.field.widget.attrs['data-cy'] = "ram_"+visible.label
    self.fields["marque"].label = "Marque"
    self.fields["frequence"].label = "Frequence"
    self.fields["taille"].label = "Taille"

  class Meta:
    model = RAM
    fields = ("marque", "frequence", 'taille')


def deleteIC(request, param):
  if request.user.is_authenticated:
    return eval(str(resolve(request.path).url_name) + "(request, param)")
  else:
    return render(request, 'accesDenied.html')


def ordinateurIC(request, param):
  if request.user.is_superuser or (
    request.user.is_authenticated and request.user == Ordinateur.objects.get(id=param).user):
    return eval(str(resolve(request.path).url_name) + "(request, param)")
  else:
    return render(request, 'accesDenied.html')


def delGpu(request, param):
  GPU.objects.get(id=param).delete()
  return HttpResponseRedirect(reverse('gpu'))


def delMotherBoard(request, param):
  MotherBoard.objects.get(id=param).delete()
  return HttpResponseRedirect(reverse('motherBoard'))


def delCpu(request, param):
  Processeur.objects.get(id=param).delete()
  return HttpResponseRedirect(reverse('processeur'))


def delRam(request, param):
  RAM.objects.get(id=param).delete()
  return HttpResponseRedirect(reverse('ram'))


def delStockage(request, param):
  Stockage.objects.get(id=param).delete()
  return HttpResponseRedirect(reverse('stockage'))


def delOrdinateur(request, param):
  Ordinateur.objects.get(id=param).delete()
  return HttpResponseRedirect(reverse('ordinateur'))


def updateIC(request, param):
  if request.user.is_authenticated:
    return eval(str(resolve(request.path).url_name) + "(request, param)")
  else:
    return render(request, 'accesDenied.html')


def updateMotherBoard(request, param):
  mb = MotherBoard.objects.get(id=param)
  mb_form_var = MotherBoardForm(instance=mb)
  if request.method == "POST":
    mb_form_var = MotherBoardForm(request.POST, instance=mb)
    if mb_form_var.is_valid():
      mb_form_var.save()
      return HttpResponseRedirect(reverse('motherBoard'))
  return render(request, 'updateMotherBoard.html', {'new_mb': mb_form_var})


def updateStockage(request, param):
  stock = Stockage.objects.get(id=param)
  stock_form_var = StockageForm(instance=stock)
  if request.method == "POST":
    stock_form_var = StockageForm(request.POST, instance=stock)
    if stock_form_var.is_valid():
      stock_form_var.save()
      return HttpResponseRedirect(reverse('stockage'))
  return render(request, 'updateStockage.html', {'new_stock': stock_form_var})


def updateGpu(request, param):
  gpu = GPU.objects.get(id=param)
  gpu_form_var = GPUForm(instance=gpu)
  if request.method == "POST":
    gpu_form_var = GPUForm(request.POST, instance=gpu)
    if gpu_form_var.is_valid():
      gpu_form_var.save()
      return HttpResponseRedirect(reverse('gpu'))
  return render(request, 'updateGpu.html', {'new_gpu': gpu_form_var})


def updateOrdinateur(request, param):
  ordinateur = Ordinateur.objects.get(id=param)
  ordinateur_form_var = OrdinateurForm(instance=ordinateur)
  if request.method == "POST":
    ordinateur_form_var = OrdinateurForm(request.POST, instance=ordinateur)
    if ordinateur_form_var.is_valid():
      ordinateur_form_var.save()
      return HttpResponseRedirect(reverse('ordinateur'))
  return render(request, 'updateOrdinateur.html', {'new_ordinateur': ordinateur_form_var})


def updateProcesseur(request, param):
  cpu = Processeur.objects.get(id=param)
  proco_form_var = ProcesseurForm(instance=cpu)
  if request.method == "POST":
    proco_form_var = ProcesseurForm(request.POST, instance=cpu)
    if proco_form_var.is_valid():
      proco_form_var.save()
      return HttpResponseRedirect(reverse('processeur'))
  return render(request, 'updateProcesseur.html', {'new_proco': proco_form_var})


def updateRam(request, param):
  ram = RAM.objects.get(id=param)
  ram_form_var = RAMForm(instance=ram)
  if request.method == "POST":
    ram_form_var = RAMForm(request.POST, instance=ram)
    if ram_form_var.is_valid():
      ram_form_var.save()
      return HttpResponseRedirect(reverse('ram'))
  return render(request, 'updateRam.html', {'new_ram': ram_form_var})
