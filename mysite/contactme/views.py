from django.core.mail import EmailMessage
from django.shortcuts import redirect, render
from django.template import Context
from django.template.loader import get_template

from .forms import Contactform

def contact(request):
    form_class = Contactform

    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get('contact_name', '')
            contact_email = request.POST.get('contact_email', '')
            form_content = request.POST.get('content', '')
            # Email the profile with the
            # contact information
            template = get_template('contact_template.txt')
            context = Context({
                'contact_name': contact_name,
                'contact_email': contact_email,
                'form_content': form_content,
            })
            content = template.render(context)

            email = EmailMessage(
                "New contact form submission",
                content,
                "Joy Barnes" +'',
                ['joypersonalwebsite@gmail.com'],
                headers = {'Reply-To': contact_email }
            )
            email.send()
            return redirect('/contacts/thankyou')
    labels = {'contact_name':'your name', 'contact_email':'your email', 'content':'what you want to say?'}
    return render(request, 'contactme/contacts.html', {
        'form': form_class,
    })

def thankyou(request):
    return render(request, 'contactme/thankyou.html')
