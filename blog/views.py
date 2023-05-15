from django.shortcuts import get_object_or_404, render,redirect
from .models import * 
from taggit.models import Tag 
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
# Create your views here.
#newsletter for collecting emails
def newsletter(request):
    if request.method=="POST":
        email=request.POST.get('email')
        #this get_or_create autmacically detects from data base if exsist then get and if not then it creates it.
        newsletter, created = Newsletter.objects.get_or_create(email=email)
        if created:
            newsletter.save()
            messages.success(request, "You have successfully joined our newsletter!")
            return redirect('/')
            
        else:
            messages.success(request, "Your are already our member.")
            return redirect('/')
    
def index(request, tag_slug=None):
    post=Post.objects.filter(status='published').order_by('-publish')
    alltags=Tag.objects.all()
    print(alltags)

     # post tag
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        post = post.filter(tags__in=[tag])
    
    post=Post.objects.filter(status='published').order_by('-publish')
    
    latestpost=Post.objects.filter(status='published').order_by('-publish')[:3]
    category=Categorie.objects.all()
    
    page = request.GET.get('page', 1)

    paginator = Paginator(post, 10)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    
    return render(request,'index.html',{'posts':posts,'category':category,'latestpost':latestpost,'post':post, 'tag':tag,'alltags':alltags})

def category(request,url):
    post=Post.objects.filter(status='published',category__name__contains=url).order_by('-publish')
    page = request.GET.get('page', 1)
    

    paginator = Paginator(post, 10)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request,'search.html',{'posts':posts,'query':url})
    
def postdetails(request,url):
    postdetails=get_object_or_404(Post,url=url)
    return render(request,'pd.html',{'postdetails':postdetails})
def search(request):
    if request.method=="GET":
        query=request.GET.get('s') 
        post=Post.objects.filter(status='published',title__icontains=query,body__icontains=query).order_by('-publish')
    
    page = request.GET.get('page', 1)

    paginator = Paginator(post, 10)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request,'search.html',{'posts':posts,'query':query})
def contact(request):
    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        message=request.POST.get("message")
        contact=Contact(name=name,email=email,message=message)
        contact.save()
        messages.success(request, "Your cont form is successfully sent.")
        
    return render(request,'contact.html')
def author(request,author):

    post=Post.objects.filter(status='published',author__username__contains=author).order_by('-publish')
    return render(request,'author.html',{'posts':post,'author':author})