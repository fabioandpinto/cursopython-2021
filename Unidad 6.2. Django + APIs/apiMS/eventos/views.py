from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from dateutil import tz, parser
from django.urls import reverse

from .auth_helper import get_sign_in_flow, get_token_from_code, store_user
from .help_box import  *

# Create your views here.
def home(request):
  return render(request, 'home.html')

def sign_in(request):
  flow = get_sign_in_flow()
  try:
    request.session['auth_flow'] = flow
  except Exception as e:
    print(e)

  return HttpResponseRedirect(flow['auth_uri'])

def callback(request):
# Make the token request
  result = get_token_from_code(request)

  #Get the user's profile
  user = get_user(result['access_token'])
  # Store user
  store_user(request, user)
  return HttpResponseRedirect(reverse('home'))

