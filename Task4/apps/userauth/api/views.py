from django.http import Http404
from rest_framework import generics, status
from django.shortcuts import get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from django.contrib.auth.models import User
from apps.userauth.api.serializers import RegTrySerializer, SetPassSerialazer
from apps.OTC.api.serializers import OTCSerializer
from apps.userauth.models import RegistrationTry as RegistrationTryModel
from apps.OTC.models import OTCRegistration



class RegistrationTry(generics.CreateAPIView):
    queryset = RegistrationTryModel.objects.all()
    serializer_class = RegTrySerializer

    def post(self, *args, **kwargs):
        res = super().post(*args, **kwargs)
        if res.status_code == status.HTTP_201_CREATED:
            pass
        return res


class RegistrationCheck(generics.RetrieveUpdateAPIView):
    queryset = OTCRegistration.objects.all()
    serializer_class = OTCSerializer

    def get_object(self):
        try:
            code = get_object_or_404(OTCRegistration, otc=self.kwargs.get('otc_check'))
            if not code.is_used:
                return code
            else:
                raise Http404
        except Exception as e:
            raise e



class SuccessRegistration(generics.ListCreateAPIView):
    queryset = RegistrationTryModel.objects.all()
    serializer_class = RegTrySerializer


class SetPass(generics.RetrieveAPIView, generics.CreateAPIView):
    queryset = RegistrationTryModel.objects.all()
    serializer_class = SetPassSerialazer

    def get_object(self):
        # cheking OTC, cheking RegistrationTry
        try:
            code = get_object_or_404(OTCRegistration, otc=self.kwargs.get('otc_check'))
            registration = RegistrationTryModel.objects.get(otc=code.id)  # geting RegistrationTry by OTC
            if not code.is_used:
                return registration
            elif registration.is_finished:
                return registration
            else:
                print('404 in code.is_used')
                raise Http404
        except Exception as e:
            print('404 in get_object ---->', e)
            raise Http404



def HomeView(request):
    return render(request, 'home.html')


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




