#coding=utf-8
from django.contrib.auth import authenticate
from django.http import HttpResponse

from django.shortcuts import render,render_to_response,RequestContext,HttpResponseRedirect
from django import  forms
from models import Members
from yzm import create_validate_code

from django.contrib.auth.hashers import make_password,check_password


#注册表单
class UserForm(forms.Form):
    Email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Email','autocomplete':'off','id':'inputEmail','required':'','autofocus':''}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'password','autocomplete':'off'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Confirm Password','autocomplete':'off'}))

#上传图片
class UserPic(forms.Form):
    pic =forms.FileField()
#登陆表单
class UserLogin(forms.Form):
    Email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Email','autocomplete':'off','id':'inputEmail','required':'','autofocus':''}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'password','autocomplete':'off'}))


#注册
def reg(req):
    if req.method == 'POST':
        m = UserForm(req.POST)
        if m.is_valid():
            print m.cleaned_data
            mail = m.cleaned_data['Email']
            password = m.cleaned_data['password']
            confirm_password = m.cleaned_data['confirm_password']
            sha256 = make_password(password,'Dzer0','pbkdf2_sha256')
            md5password = make_password(sha256,None,'unsalted_md5')
            print sha256
            print md5password
            if password == confirm_password:
                Members.objects.create(Email =mail,password = md5password)
                return HttpResponse('REG SUCCESS!!!')
            else:
                return HttpResponseRedirect('/reg/')
            #return HttpResponse('REG SUCCESS!!!')
            #return render_to_response('regedit.html',locals())
    else:
        m = UserForm()
        return render_to_response('reg.html',locals(),context_instance=RequestContext(req))


#取列
def lie(req):
    a=['123123123','sfdadfasf']
    return render_to_response('lie.html',locals())


#登陆
def login(req):
    if req.method=='POST':
        mlc = UserLogin(req.POST)
        if mlc.is_valid():
            email = mlc.cleaned_data['Email']
            password = mlc.cleaned_data['password']
            sha256 = make_password(password,'Dzer0','pbkdf2_sha256')
            md5password = make_password(sha256,None,'unsalted_md5')
            user = Members.objects.filter(Email = email,password = md5password)
            print email
            print md5password
            print user
            if user:

                sessname = req.session['Email']=email
                return render_to_response('login.html',locals(),context_instance =RequestContext(req))
                #return HttpResponse('LOGIN SUCCESS!')
                #return render_to_response('form.html',locals(),context_instance = RequestContext(req))
            else:
                mlc=UserLogin()
                return HttpResponseRedirect('/login/')
    else:
        mlc =UserLogin()
        return render_to_response('login.html',locals(),context_instance = RequestContext(req))

#退出登陆

def logout(req):
    sessname = req.session['Email']=''
    mlc = UserLogin()
    return HttpResponseRedirect('/login/')
    #return render_to_response('login.html',locals(),context_instance = RequestContext(req))


#上传图片
def up(req):
    if req.method == 'POST':
        picpost =UserPic(req.POST,req.FILES)
        print picpost
        if picpost.is_valid():
            sessname = req.session['Email']
            print picpost.cleaned_data
            pic = picpost.cleaned_data['pic']

            up_headimg= Members.objects.get(Email=sessname)
            up_headimg.headimg = pic
            #up_headimg.save()
            return  HttpResponse('ok')
            #return render_to_response('login.html',locals(),context_instance=RequestContext(req))

    else:
        if req.session['Email'] =='':
            mlc =UserLogin()
            return HttpResponseRedirect('/login/')
        else:
            sessname = req.session['Email']
            pic_forms=UserPic()
            print pic_forms
    #mlc = UserLogin()
            return render_to_response('pic.html',locals(),context_instance = RequestContext(req))




#验证码
def validate(req):
    mstream = StringIO.StringIO()

    validate_code = create_validate_code()
    img = validate_code[0]
    img.save(mstream, "GIF")

    req.session['validate'] = validate_code[1]

    return HttpResponse(mstream.getvalue(), "image/gif")


