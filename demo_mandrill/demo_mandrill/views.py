# -*- coding: utf-8 -*-
from django.core.mail import EmailMessage
from django.template import Context
from django.template.loader import get_template

from django.http import HttpResponseRedirect,HttpResponse

import mandrill
 
API_KEY = 'Db9t7n5kJHIrJLw5wXyuJg'
 

 

def mail(request):
    mandrill_client = mandrill.Mandrill(API_KEY)
    htmly     = get_template('sidebar-hero.html')

    d = Context({ 'nombre': "vash loco" })

    html_content = htmly.render(d)

    message = {
        "html": html_content,
        "subject": "Mas minimalista",
        "from_email": "phyrox.vash512@gmail.com",
        "from_name": "vash's Lab",
        "to": [
            {
                "email": "phyrox.vash512@gmail.com"
            }
        ]
    }


    result = mandrill_client.messages.send(message=message, async=False)

    return HttpResponseRedirect('/?enviado=True')
