from django.contrib import admin
from address.models import Address

# Register your models here.
class AddressAdmin(admin.ModelAdmin):
    list_display = ('name', 'tel', 'email', 'address')

#디장고의 관리자모드에서 새롭게 관리될 Address, AddressAdmin을 등록한다.
admin.site.register(Address,AddressAdmin)