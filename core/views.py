from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from sesame.decorators import authenticate
import sesame.utils
from core.forms import EmailLoginForm

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = EmailLoginForm(request.POST)
        if form.is_valid():
            # here we, want to email the user the magic link
            email = form.cleaned_data['email']
            
            first_user = User.objects.first()
            link = request.build_absolute_uri(reverse('user-profile', kwargs={'pk': first_user.pk}))
            link += sesame.utils.get_query_string(first_user, scope=f"user:{first_user.pk}")
            send_mail(
                "Your Magic Login Link",
                f"""My profile - view with this link: {link}""",
                settings.DEFAULT_FROM_EMAIL,
                [email],
                fail_silently=False,
            )


    context = {'form': EmailLoginForm()}
    return render(request, 'index.html', context)


@authenticate(scope="secret")
def secret_view(request):
    context = {}
    return render(request, 'secret.html', context)


@authenticate(scope="secret")
def secret_report_view(request):
    context = {}
    return render(request, 'secret_report.html', context)


@authenticate(scope="user:{pk}")
def user_profile(request, pk):
    user = get_object_or_404(User, pk=pk)
    context = {'user': user}
    return render(request, 'profile.html', context)