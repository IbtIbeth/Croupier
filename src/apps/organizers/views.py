from django.shortcuts import render

from django.http import HttpResponseRedirect
from django.shortcuts import render

from organizers.forms import SignupForm

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SignupForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            form.save()
            return HttpResponseRedirect('/organizers/welcome')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = SignupForm()

    return render(request, 'organizers/signup.html', {'form': form})


def welcome(request):
    return render(request, 'organizers/welcome.html')