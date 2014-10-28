# -*- coding: utf-8 -*-
from django.template import Context
from django.template.loader import get_template
from django.db import models
from django.db.models.signals import post_save

import mandrill
 
API_KEY = 'Db9t7n5kJHIrJLw5wXyuJg'

class Correo(models.Model):
    asunto = models.CharField(max_length=225)
    para = models.CharField(max_length=225)
    contenido = models.TextField()
    def __unicode__(self):
        return self.asunto

def enviar_Correo(sender, instance, **kwargs):
    mandrill_client = mandrill.Mandrill(API_KEY)
    htmly     = get_template('sidebar-hero.html')

    d = Context({ 'nombre': instance.para, 'contenido':instance.contenido })

    html_content = htmly.render(d)

    message = {
        "html": html_content,
        "text": "que raro, no cargo el html :(",
        "subject": instance.asunto,
        "from_email": "phyrox.vash512@gmail.com",
        "from_name": "vash Lab",
        "to": [
            {
                "email": instance.para
            }
        ]
    }
    result = mandrill_client.messages.send(message=message, async=False)


post_save.connect(enviar_Correo, sender=Correo, dispatch_uid="enviar_correo")