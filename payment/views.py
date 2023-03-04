import requests
import json

from django.shortcuts import get_object_or_404, redirect, reverse
from django.http import HttpResponse
from django.conf import settings

from orders.models import Order


def payment_process(request):
    order_id = request.session.get('order_id')
    order = get_object_or_404(Order, id=order_id)

    toman_total_price = order.get_total_price()
    rial_total_price = toman_total_price * 10

    zarinpal_request_url = 'https://api.zarinpal.com/pg/v4/payment/request.json'

    request_header = {
        "accept": "application/json",
        "content-type": "application/json",
    }

    request_data = {
        'merchant_id': settings.ZARINPAL_MERCHANT_ID,
        'amount': rial_total_price,
        'description': f"#{order.id} : {order.firstname} {order.lastname}",
        'callback_url': request.build_absolute_uri(reverse('payment:payment_callback')),
    }

    res = requests.post(url=zarinpal_request_url, data=json.dumps(request_data), headers=request_header)
    data = res.json()['data']
    authority = data['authority']
    order.zarin_authority = authority
    order.save()

    if 'errors' not in data or len(data['errors'] == 0):
        return redirect(f'https://www.zarinpal.com/pg/StartPay/{authority}')
    else:
        return HttpResponse('Zarinpal Error')
