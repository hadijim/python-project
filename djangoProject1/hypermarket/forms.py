from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm
from .models import CustomUser, Good, Factor, Buyer


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("codepersonely", "is_warekeeper", "is_accountant")


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ("codepersonely",)


class GoodCreationForm(ModelForm):
    class Meta:
        model = Good
        fields = ("name", "ma_data", "exp_data", "num", "company_price", "consumer_price",)


class FactorCreationForm(ModelForm):
    class Meta:
        model = Factor
        fields = ("good", "buyer",)

class BuyerCreationForm(ModelForm):
    class Meta:
        model = Buyer
        fields = ("user", "discount",)