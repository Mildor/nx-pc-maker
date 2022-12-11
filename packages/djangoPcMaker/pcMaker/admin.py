from django.contrib import admin
from pcMaker.models import *

class MotherBoardAdmin(admin.ModelAdmin):
    list_display=('marque', 'chipset')

class GPUAdmin(admin.ModelAdmin):
    list_display=('marque', 'modele')

class StockageAdmin(admin.ModelAdmin):
    list_display=('type', 'taille')

class ProcesseurAdmin(admin.ModelAdmin):
    list_display=('marque', 'categorie', 'modele')

class RAMAdmin(admin.ModelAdmin):
    list_display=('marque', 'frequence', 'taille')

class OrdinateurAdmin(admin.ModelAdmin):
    list_display=('gpu', 'get_stockage', 'processeur', 'ram')



admin.site.register(MotherBoard, MotherBoardAdmin)
admin.site.register(GPU, GPUAdmin)
admin.site.register(Stockage, StockageAdmin)
admin.site.register(Processeur, ProcesseurAdmin)
admin.site.register(RAM, RAMAdmin)
admin.site.register(Ordinateur, OrdinateurAdmin)