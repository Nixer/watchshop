from django.http import JsonResponse
from .models import WatchShop
from watchshopapp.serializers import WatchShopSerializer


def client_get_watchshops(request):
    watchshops = WatchShopSerializer(
        WatchShop.objects.all().order_by('-id'),
        many=True,
        context={'request': request}
    ).data

    return  JsonResponse({'watchshops': watchshops})
