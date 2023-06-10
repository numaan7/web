from django.shortcuts import get_object_or_404, render,redirect
from .models import * 
from shop.models import Address
from django.conf import settings
from django.core.mail import send_mail
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from taggit.models import Tag
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth  import authenticate,  login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin

class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'password_reset.html'
    email_template_name = 'password_reset_email.html'
    subject_template_name = 'users/password_reset_subject.txt'
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      " If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and check your spam folder."
    success_url = reverse_lazy('home')
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
    
def index(request,tag_slug=None):
   
   
    all_tags = Tag.objects.all()

    
    post=Post.objects.filter(status='published').order_by('-publish')
    
    latestpost=Post.objects.filter(status='published').order_by('-publish')[:3]
    category=Categorie.objects.all()
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        post=Post.objects.filter(status='published',tags=tag).order_by('-publish')
    
    page = request.GET.get('page', 1)

    paginator = Paginator(post, 10)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    
    return render(request,'index.html',{'posts':posts,'category':category,'latestpost':latestpost,'post':post,'all_tags':all_tags,'tag':tag})

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
    comments=Comment.objects.filter(post=postdetails,is_parent=True).order_by('-date')
    if request.method=="POST":
        try:
           comment=request.POST.get("comment")
           user=request.user
           com=Comment(comment=comment,user=user,post=postdetails,is_parent=True)
           com.save()
           
        except:
            reply=request.POST.get("reply")
            commentid=request.POST.get("commentid")
            ruser=request.user
            parent=get_object_or_404(Comment,id=int(commentid))
            rep=Comment(comment=reply,user=ruser,post=postdetails,parent=parent,is_parent=False)
            rep.save()
   
    return render(request,'pd.html',{'postdetails':postdetails,'comments':comments})
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
    user=get_object_or_404(User,username=author)
    
    profile=get_object_or_404(Profile,user=user,staff=True)
    post=Post.objects.filter(status='published',author__username__contains=author).order_by('-publish')
    return render(request,'author.html',{'posts':post,'author':author,'profile':profile})

def signup(request):
    if request.method=="POST":
        email=request.POST.get('email')
        username=request.POST.get('username')
        password=request.POST.get('password')
        if len(username)<=6:
            messages.error(request, " Your user name must be under 6 characters")
            return redirect('/signup')

        if not username.isalnum():
            messages.error(request, " User name should only contain letters and numbers")
            return redirect('/signup')
        if User.objects.filter(email=email).exists():
            messages.error(request, " Email already Exists.")
            return redirect('/signup')
        if User.objects.filter(username=username).exists():
            messages.error(request, " Username already Exists.")
            return redirect('/signup')

        
        myuser = User.objects.create_user(username, email, password)
        myuser.save()
        address=Address(user=myuser)
        address.save()
        profile=Profile(user=myuser)
        profile.save()
        subject="Account creation successfull!"
        message=f"Hi {username},\n Thank you! for creating your Account in {settings.MY_WEBSITE_NAME}."
        email_from=settings.EMAIL_HOST_USER
        recipient_list=[email,]
        send_mail( subject, message, email_from, recipient_list )
        messages.success(request, " Your Smartify has been successfully created")
        return redirect('/login')
    return render(request,'signup.html')

def loginhandle(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username= username, password= password)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect("/")
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect("/login")
    return render(request,'login.html')

@login_required(login_url='/login')
def handelLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('/')

@login_required(login_url='/login')
def account(request):
    profile=get_object_or_404(Profile,user=request.user)
    
    
    if (request.method=="POST" ):
        s=request.user

        fname=request.POST.get("firstname")
        s.first_name=fname
    
        
        lname=request.POST.get("lastname")

        s.last_name=lname

        s.save()
        desc=request.POST.get("desc")
        profile.desc=desc
     
        fb=request.POST.get("fb")
        profile.facebook=fb
      
        ig=request.POST.get("ig")
        profile.instagram=ig

        tw=request.POST.get("tw")
        profile.twitter=tw
        profile.save()
     


    return render(request,'account.html',{'profile':profile})

@login_required(login_url='/login')
def updateprofile(request):
    profile=get_object_or_404(Profile,user=request.user)
    if request.method=="POST":
        upload=request.FILES.get('upload')
        profile.image=upload
        profile.save()
        return redirect('/blog/account/')

def terms(request):
    return render(request,'terms-conditions.html')
def privacy(request):
    return render(request,'privacy-policy.html')
def about(request):
    return render(request,'about.html')


  