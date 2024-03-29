from typing import Any
from django.views import generic
from django.urls import reverse_lazy
from django.http import Http404
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import SelectRelatedMixin

from . import forms, models

from django.contrib.auth import get_user_model
User = get_user_model()

class CreatePost(LoginRequiredMixin,SelectRelatedMixin,generic.CreateView):
    fields = ('image','caption')
    model = models.Post
   
    def form_valid(self,form):
        self.object = form.save(commit = False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)
    
class PostList(SelectRelatedMixin,generic.ListView):
    model = models.Post
    select_related = ['user']

class UserPostList(SelectRelatedMixin,generic.ListView):
    model = models.Post
    template_name = "posts/user_post_list.html"

    def get_queryset(self):
        try:
            self.post_user = User.objects.prefetch_related("posts").get(username__iexact =self.kwargs.get("username"))
        except User.DoesNotExist:
            raise Http404
        else:
            return self.post_user.posts.all()
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['post_user'] = self.post_user
        return context
