from django.shortcuts import render
from django.views.generic import ListView
from . models import Factor
from tutelary.mixins import PermissionRequiredMixin
# Create your views here.

class FactorView(PermissionRequiredMixin, ListView):
	permission_required = 'user.accountant'
	class Meta:
		model = Factor

# class FactorView(PermissionRequiredMixin, ListView):
# 	permission_required = 'user.accountant'
# 	class Meta:
# 		model = Factor