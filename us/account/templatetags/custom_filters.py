from django import template
from django.db.models import Q
from ..models import TourEnrole

register = template.Library()

@register.simple_tag
def enrolled(tour_id, user_id):
    print(tour_id,user_id)
    return TourEnrole.objects.filter(Q(tour_id=tour_id) & Q(user_id=user_id)).exists()
