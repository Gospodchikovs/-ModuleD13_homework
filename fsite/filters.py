from django_filters import FilterSet,  DateFilter  # импортируем filterset, чем-то напоминающий знакомые дженерики
from .models import Advertisment


class AdvertismentFilter(FilterSet):

    class Meta:
        model = Advertisment
        fields = {'heading': ['icontains'], 'body':['icontains'], 'user': ['in'], 'category': ['in']}
