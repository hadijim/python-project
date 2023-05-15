from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm, GoodCreationForm, BuyerCreationForm
from .models import CustomUser, Factor, Good, Buyer


# Register your models here.


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ("codepersonely", "is_staff", "is_active",)
    list_filter = ("codepersonely", "is_staff", "is_active",)
    fieldsets = (
        (None, {"fields": ("codepersonely", "password")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "groups", "user_permissions")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "codepersonely", "password1", "password2", "is_warekeeper", "is_accountant", "is_staff",
                "is_active", "is_superuser", "groups", "user_permissions"
            )}
         ),
    )
    search_fields = ("codepersonely",)
    ordering = ("codepersonely",)


class GoodsAdmin(admin.ModelAdmin):
    add_form = GoodCreationForm
    form = GoodCreationForm
    list_display = ("name", "ma_data", "exp_data", "num", "company_price", "consumer_price",)
    list_filter = ("exp_data", "name", "ma_data")
    search_fields = ("name", "ma_data", "exp_data",)
    ordering = ("exp_data",)


class FactoryAdmin(admin.ModelAdmin):
    list_display = ("buyer", "good")
    list_filter = ("good",)
    search_fields = ("buyer", "good",)


class BuyerAdmin(admin.ModelAdmin):
    add_form = BuyerCreationForm
    form = BuyerCreationForm
    list_display = ("user", "discount","discount_end_date", "discount_start_date",)
    search_fields = ("user",)


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Good, GoodsAdmin)
admin.site.register(Factor, FactoryAdmin)
admin.site.register(Buyer, BuyerAdmin)
