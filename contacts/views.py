from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import ListView,DetailView,CreateView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.db.models import Q

from .models import Contact

class ContactListView(LoginRequiredMixin,ListView):
    model = Contact
    template_name = 'contacts/index.html'
    context_object_name = "contacts"

    def get_queryset(self,*args, **kwargs):
        queryset = super().get_queryset()
        return queryset.filter(manager=self.request.user)


class ContactDetailView(LoginRequiredMixin,DetailView):
    template_name = 'contacts/detail.html'
    context_object_name = 'contact'

    def get_object(self, queryset=None):
        queryset=Contact.objects.filter(manager=self.request.user)
        return super().get_object(queryset=queryset)

class SearchView(LoginRequiredMixin, ListView):
    template_name = 'contacts/search.html'
    context_object_name = "contacts"

    def get_queryset(self):
        term = self.request.GET.get('q')
        queryset = Contact.objects.filter(
            Q(manager=self.request.user)&
            Q(name__icontains=term)|
            Q(email__icontains=term)|
            Q(info__icontains=term)|
            Q(phone__icontains=term)
        )
        return queryset
   
class ContactCreateView(LoginRequiredMixin, CreateView):
    model = Contact
    template_name = 'contacts/create.html'
    fields = ['name','email','phone','info','gender','image']
    
    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.manager = self.request.user
        instance.save()
        messages.success(self.request,'Contact created successfully')
        return redirect('home')


class ContactUpdateView(LoginRequiredMixin, UpdateView):
    model = Contact
    template_name = 'contacts/update.html'
    fields = ['name','email','phone','info','gender','image']

    def get_object(self, queryset=None):
        queryset=Contact.objects.filter(manager=self.request.user)
        return super().get_object(queryset=queryset)
    
    def form_valid(self, form):
        instance = form.save()
        messages.success(self.request,'Contact Updated successfully')
        return redirect('detail', instance.id)

class ContactDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'contacts/delete.html'
    success_url = reverse_lazy('home')

    def get_object(self, queryset=None):
        queryset=Contact.objects.filter(manager=self.request.user)
        return super().get_object(queryset=queryset)

    def delete(self,*args, **kwargs):
        messages.success(self.request,'Your contact has been deleted successfully !')
        return super().delete(self,*args, **kwargs)

class SignupView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('home')