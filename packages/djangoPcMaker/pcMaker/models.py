from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class MotherBoard(models.Model):
    marque = models.CharField(max_length=12)
    chipset = models.CharField(max_length=4)
    
    def __str__(self):
        return self.marque+" "+self.chipset

class GPU(models.Model):
    marque = models.CharField(max_length=24)
    modele = models.CharField(max_length=24)

    def __str__(self):
        return self.marque+" "+self.modele

class Stockage(models.Model):
    type = models.CharField(max_length=3)
    taille = models.IntegerField()

    def __str__(self):
        if self.taille >= 1000:
            return self.type+" "+str(self.taille/1000)+" To"
        else:
            return self.type+" "+str(self.taille) +" Go"
    

class Processeur(models.Model):
    marque = models.CharField(max_length=5)
    categorie = models.CharField(max_length=2)
    modele = models.CharField(max_length=10)

    def __str__(self):
        return self.marque+" "+self.modele

class RAM(models.Model):
    marque = models.CharField(max_length=24)
    frequence = models.CharField(max_length=5)
    taille = models.IntegerField()

    def __str__(self):
        return self.marque+" "+self.frequence+"MHz "+str(self.taille)+"Go"

class Ordinateur(models.Model):
    alimentation = models.IntegerField()
    gpu = models.ForeignKey(GPU, on_delete=models.CASCADE)
    stockage = models.ManyToManyField(Stockage)
    processeur = models.ForeignKey(Processeur, on_delete=models.CASCADE)
    ram = models.ForeignKey(RAM, on_delete=models.CASCADE)
    motherBoard = models.ForeignKey(MotherBoard, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_stockage(self):
        return "\n".join([str(p) for p in self.stockage.all()])
    
    def __str__(self):
        return str(self.user)+" / "+str(self.gpu)+" / "+str(self.processeur)+" / "+str(self.motherBoard)+" / "+str(self.ram)+" / "+self.get_stockage()+" / "+str(self.alimentation)