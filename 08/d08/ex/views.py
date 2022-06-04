from django.shortcuts import render
from django.views.generic import FormView, ListView
from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Image
from .forms import ImageForm

# Create your views here.
class Index(ListView, FormView):
	success_url = reverse_lazy('index')
	template_name = 'ex/index.html'
	form_class = ImageForm
	model = Image
	queryset = model.objects.all().order_by('-id')

	def form_valid(self, form: ImageForm):
		form.save()
		return super().form_valid(form)

	def form_invalid(self, form: ImageForm):
		print(form.errors)
		return super().form_invalid(form)