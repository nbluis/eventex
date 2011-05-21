# -*- coding: utf-8 -*-

from django.core.mail import send_mail
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404

from subscription.models import Subscription
from subscription.forms import SubscriptionForm

def new(request):
    form = SubscriptionForm()
    context = RequestContext(request, {'form': form})
    return render_to_response('subscription/new.html', context)

def create(request):
    form = SubscriptionForm(request.POST)

    if not form.is_valid():
        context = RequestContext(request, {'form': form})
        return render_to_response('subscription/new.html', context)

    subscription = form.save()
    send_subscription_email(subscription)
    return HttpResponseRedirect(reverse('subscription:success', args = [subscription.pk]))

def success(request, id):
    subscription = get_object_or_404(Subscription, pk=id)
    context = RequestContext(request, {'subscription': subscription})
    return render_to_response('subscription/success.html', context)

def send_subscription_email(subscription):
	send_mail(
		subject = u'Inscrição no EventeX', 
		message = u'Obrigado por se inscrever no EventeX!', 
		from_email = 'contato@eventex.com', 
		recipient_list = [ subscription.email ],
	)
