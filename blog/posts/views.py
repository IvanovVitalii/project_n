from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import generic

from .forms import LoginForm, PostForm, ProductForm
from .models import Post, Product

PAGINATOR = 5


class PostList(generic.ListView):
    queryset = Post.objects.all().order_by('-created')
    template_name = 'post/post.html'
    paginate_by = PAGINATOR


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post/post_detail.html'


class PostCreate(generic.CreateView):
    form_class = PostForm
    template_name = 'post/post_create.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.author = self.request.user
        post.save()
        return redirect('post')


class PostUpdate(generic.UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'post/post_create.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.author = self.request.user
        post.save()
        return redirect('post_detail', pk=post.pk)


class ProductList(generic.ListView):
    queryset = Product.objects.all().order_by('-created')
    template_name = 'product/product.html'
    paginate_by = PAGINATOR


class ProductDetail(generic.DetailView):
    model = Product
    template_name = 'product/product_detail.html'


class ProductCreate(generic.CreateView):
    form_class = ProductForm
    template_name = 'product/product_create.html'

    def form_valid(self, form):
        product = form.save(commit=False)
        product.author = self.request.user
        product.save()
        return redirect('product')


class ProductUpdate(generic.UpdateView):
    form_class = ProductForm
    model = Product
    template_name = 'product/product_create.html'

    def form_valid(self, form):
        product = form.save(commit=False)
        product.author = self.request.user
        product.save()
        return redirect('product_detail', pk=product.pk)


class SearchResultsView(generic.ListView):
    '''
    Generating post_list and product_list to display on the search_results page
    '''
    template_name = 'search_results.html'
    context_object_name = 'post_list'
    model = Post
    paginate_by = PAGINATOR

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Post.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query)
        )

    def get_context_data(self, **kwargs):
        query = self.request.GET.get('q')
        context = super(SearchResultsView, self).get_context_data(**kwargs)
        context['product_list'] = Product.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query)
        )
        return context


def about(request):
    return render(request, 'about.html')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('post')
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
                    return redirect('post')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('post')
