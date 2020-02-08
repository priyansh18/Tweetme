from django.shortcuts import render
from django.views.generic import DetailView,ListView,CreateView,UpdateView,DeleteView
from django.db.models import Q
from .models import Tweet
from .forms import TweetModelForm
from .mixins import FormUserMixins,UserOwnerMixin
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class TweetCreateView(LoginRequiredMixin,FormUserMixins,CreateView):
    form_class = TweetModelForm
    template_name = 'tweet/create_view.html'
    success_url = '/tweet/'
    login_url   = '/admin/'

class TweetUpdateView(LoginRequiredMixin,UserOwnerMixin,UpdateView):
    queryset = Tweet.objects.all()
    form_class = TweetModelForm
    template_name = 'tweet/update_view.html'
    success_url = '/tweet/'

class TweetDeleteView(LoginRequiredMixin,UserOwnerMixin,DeleteView):
    queryset = Tweet.objects.all()
    form_class = TweetModelForm
    template_name = 'tweet/delete_view.html'
    success_url = '/tweet/'    
      
class TweetDetailView(DetailView):
    template_name = 'tweet/detail_view.html'
    queryset = Tweet.objects.all()

    def get_object(self):
        pk = self.kwargs.get('pk')
        return Tweet.objects.get(id=pk)        

class TweetListView(ListView):
    template_name = 'tweet/list_view.html'
         
    def get_queryset(self,*args,**kwargs):
        qs = Tweet.objects.all()
        print(qs)
        print(self.request.GET)
        query = self.request.GET.get('q', None)
        if query is not None:
            qs = qs.filter(
                Q(content__icontains=query) |
                Q(user__username__icontains=query)
                           )
        return qs

    def get_context_data(self,*args,**kwargs):
        context = super(TweetListView,self).get_context_data(*args,**kwargs)
        context['create_form'] = TweetModelForm()
        context['create_url'] = 'tweet/create/'
        return context


# def tweet_detail_view(request,id=1):
#     obj = Tweet.objects.get(id=id)
#     print(obj)
#     context = {
#         'object' : obj
#     }
#     return render(request,'tweet/detail_view.html',context)

# def tweet_list_view(request):
#     queryset = Tweet.objects.all()
#     print(queryset)
#     for val in queryset:
#         print(val)
#     context = {
#         'object_list' : queryset
#     }
#     return render(request,'tweet/list_view.html',context)    