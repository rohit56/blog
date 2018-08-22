from django.shortcuts import render, redirect
from blog.forms import RegistrationForm
from django.contrib.auth.decorators import login_required


@login_required(login_url='/login/')
def home(request):
    query = request.GET.get('name')
    msg = 'My Name is {} and I learn Django'.format(query)
    template = "home.html"
    context = {
         'message' : msg,
    }
    return render(request, template, context)

def user_register(request):
    template = 'user/add.html'
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/final')
    else:
        form = RegistrationForm()

        args = {'form': form}
        return render(request, template, args)

def final(request):
    template = "auth/register.html"
    context = {}
    return render(request, template, context)
