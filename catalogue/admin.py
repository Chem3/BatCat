from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Person
from .models import Shelf
from .models import Project
from .models import Sample
from .models import Parameter
from .models import Method
from .models import Analysis
from .models import Treatment
from .models import Container
from .models import Material
from .models import StorageUpdate
from .forms import StorageUpdateForm

class StorageUpdateAdmin(admin.ModelAdmin):
    form = StorageUpdateForm

admin.site.register(Shelf)
admin.site.register(Person)
admin.site.register(Project)
admin.site.register(Sample)
admin.site.register(Parameter)
admin.site.register(Method)
admin.site.register(Analysis)
admin.site.register(Treatment)
admin.site.register(Container)
admin.site.register(Material)
admin.site.register(StorageUpdate, StorageUpdateAdmin)
