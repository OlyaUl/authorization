from django.shortcuts import render, render_to_response
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

from django.views.generic import CreateView
from .forms import UserForm


def index(request):
    return render(request, 'standart_auth/index.html', {})


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/standart_auth/')
            else:
                return HttpResponse("Your account is disabled.")
        else:
            print("Invalid login details: {0}, {1}".format(username, password))
            return HttpResponse("Invalid login details supplied.")

    else:
        return render(request, 'standart_auth/login.html', {})


# регистрация
def register_view(request):
    form = UserForm()

    if request.method == 'POST':
        data = request.POST.copy()
        errors = form.get_validation_errors(data)
        if not errors:
            new_user = form.save(data)
            return HttpResponseRedirect("/standart_auth/")
    else:
        data, errors = {}, {}

    return render(request, 'standart_auth/registration.html', {
       # 'form': forms.FormWrapper(form, data, errors)
    })


    '''registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        # profile_form = UserProfileForm(data=request.POST)
        if user_form.is_valid() :#and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            #profile = profile_form.save(commit=False)
            #profile.user = user
            #if 'photo' in request.FILES:
             #   profile.picture = request.FILES['photo']
            #profile.save()
            registered = True
        else:
            print(user_form.errors)#, profile_form.errors)
    else:
        user_form = UserForm()
        #profile_form = UserProfileForm()

    return render(request, 'standart_auth/registration.html',
                  {'user_form': user_form,
                 #  'profile_form': profile_form,
                   'registered': registered})'''


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/standart_auth/')


'''class UserFormView(CreateView):
    form_class = UserForm
    template_name = 'standart_auth/registration.html'
    success_url = '/standart_auth/'

    def form_valid(self, form):
        response = super(UserFormView, self).form_valid(form)
        self.object.set_password(form.cleaned_data['password'])
        response

    def get_context_data(self, **kwargs):
        return super(UserFormView, self).get_context_data(**kwargs)'''
