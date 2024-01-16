from django.contrib import admin
from .models import Employee, Testimonial

class EmpAdmin(admin.ModelAdmin):
    list_display = ('emp_id','name','working','department')
    list_editable=('working','department')
    search_fields = ('name','department','working')
    list_filter = ('working','department')

class TestmoAdmin(admin.ModelAdmin):
    list_display = ('name','testimonial','rating')
    search_fields = ('name','rating')
    list_filter = ('rating',)

# Register your models here.
admin.site.register(Employee,EmpAdmin)
admin.site.register(Testimonial,TestmoAdmin)
