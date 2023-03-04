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


def payment_callback(request):
    payment_authority = request.GET.get('Authority')
    payment_status = request.GET.get('Status')

    order = get_object_or_404(Order, zarin_authority=payment_authority)
    toman_total_price = order.get_total_price()
    rial_total_price = toman_total_price * 10

    if payment_status == 'OK':
        request_header = {
            "accept": "application/json",
            "content-type": "application/json",
        }

        request_data = {
            'merchant_id': settings.ZARINPAL_MERCHANT_ID,
            'amount': rial_total_price,
            'authority': payment_authority,
        }

        res = requests.post(url='https://api.zarinpal.com/pg/v4/payment/verify.json', data=json.dumps(request_data),
                            headers=request_header)

        if 'data' in res.json() and ('errors' not in res.json()['data'] or len(res.json()['errors'] == 0)):
            data = res.json()['data']
            payment_code = data['code']

            if payment_code == 100:
                order.is_paid = True
                order.zarin_ref_id = data['ref_id']
                order.zarin_data = data
                order.save()
                return redirect('home:home')

            elif payment_code == 101:
                return redirect('home:home')

            else:
                payment_error = res.json()['errors']['code']
                payment_message = res.json()['errors']['message']
                return redirect('home:home')

        else:
            return redirect('home:home')

    else:
        return redirect('home:home')
