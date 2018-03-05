from django.http import JsonResponse
from .models import WatchShop, Watch
from watchshopapp.serializers import WatchShopSerializer, WatchsSerializer


def client_get_watchshops(request):
    watchshops = WatchShopSerializer(
        WatchShop.objects.all().order_by('-id'),
        many=True,
        context={'request': request}
    ).data

    return JsonResponse({'watchshops': watchshops})


def client_get_watchs(request, watchshop_id):
    watchs = WatchsSerializer(
        Watch.objects.all().filter(watchshop_id=watchshop_id).order_by('-id'),
        many=True,
        context={'request': request}
    ).data

    return JsonResponse({'watchs': watchs})
