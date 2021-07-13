from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import generic

from .forms import LoginForm, PostForm
from .models import Post, Product

PAGINATOR = 5


# class PostList(generic.ListView):
#     queryset = Post.objects.all().order_by('-created')
#     template_name = 'home.html'
#     paginate_by = PAGINATOR


class PostList(generic.ListView):
    '''
    Generating post_list and product_list to display on the home page
    '''
    template_name = 'home.html'
    context_object_name = 'post_list'
    model = Post
    paginate_by = PAGINATOR

    def get_queryset(self):
        return Post.objects.all().order_by('-created')

    def get_context_data(self, **kwargs):
        context = super(PostList, self).get_context_data(**kwargs)
        context['product_list'] = Product.objects.all().order_by('-created')
        return context


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'


class SearchResultsView(generic.ListView):
    model = Post
    template_name = 'search_results.html'
    paginate_by = PAGINATOR

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Post.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query)
        )
        return object_list


class PostCreate(generic.CreateView):
    form_class = PostForm
    template_name = 'post_create.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.author = self.request.user
        post.save()
        return redirect('home')


class PostUpdate(generic.UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'post_create.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.author = self.request.user
        post.save()
        return redirect('post_detail', pk=post.pk)


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('home')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})


def logout(request):
    logout(request)
    return redirect('home')
