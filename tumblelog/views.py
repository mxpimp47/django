from tumblelog.models import TumbleItem
from django.shortcuts import render_to_response


def tumbler(request):
	context = {
		'tumble_item_list': TumbleItem.objects.all().order_by('-pub_date')
	}

	return render_to_response('tumblelog/list.html', context)
