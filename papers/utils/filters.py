# myapp/filters.py
import django_filters
from ..models import Paper

class PaperFilter(django_filters.FilterSet):
    class Meta:
        model = Paper
        fields = ['year', 'level__name', 'subject__name', 'title']
