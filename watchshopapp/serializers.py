from rest_framework import serializers
from watchshopapp.models import WatchShop


class WatchShopSerializer(serializers.ModelSerializer):
    # id = serializers.IntegerField(read_only=True)
    # name = serializers.CharField(required=False, max_length=100, allow_blank=True)
    # phone = serializers.CharField(max_length=100)
    # address = serializers.CharField(max_length=100)
    logo = serializers.SerializerMethodField()

    def get_logo(self, watchshop):
        request = self.context.get('request')
        logo_url = watchshop.logo.url
        return request.build_absolute_uri(logo_url)

    class Meta:
        model = WatchShop
        fields = ('id', 'name', 'phone', 'address', 'logo')
