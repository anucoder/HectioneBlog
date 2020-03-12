from django.shortcuts import render,redirect
from django.views.generic import TemplateView,ListView,DetailView
from blog.models import Post
from django.utils import timezone
from . import forms
# Create your views here.


class IndexView(TemplateView):
    template_name = 'index.html'


class AboutView(TemplateView):
    template_name = 'about.html'

class ContactView(TemplateView):
    template_name = 'contact.html'


class ThanksView(TemplateView):
    template_name = 'thanks.html'


class PostListView(ListView):
    model = Post
    # context_object_name = 'post_list'

    def get_queryset(self):
        # return Post.objects.filter(created_on__lte=timezone.now()).order_by('-created_on')
        return Post.objects.filter()


# class PostDetailView(DetailView):
#     model = Post

def contactFormView(request):
    form = forms.ContactForm


    if(request.method == 'POST'):
        form = forms.ContactForm(request.POST)

        if form.is_valid():
            print("name "+form.cleaned_data['name'])
            print("email "+form.cleaned_data['email'])
            print("message "+form.cleaned_data['message'])

            return redirect('/thanks/')
    else:
        form = forms.ContactForm

    return render(request,'contact.html',{'form':form})
