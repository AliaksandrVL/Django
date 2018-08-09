import json

from django.shortcuts import get_list_or_404

from django.http import HttpResponse

from . import models

def api_product_list(request):
    
    query = get_list_or_404(models.Article)

    data = map(lambda itm: {
        'id': itm.id,
        'name': itm.name,
        'image': itm.image.name
        }, query)

    context = json.dumps({'results': list(data)})

    return HttpResponse(context)