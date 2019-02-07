from rest_framework.generics import ListAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView
from restaurants.models import Restaurant
from .serializers import RestaurantListSerializer,RestaurantDetailSerializer,RestaurantUpdateSerializer

class RestaurantListView(ListAPIView):
	queryset = Restaurant.objects.all()
	serializer_class = RestaurantListSerializer

# Complete me
class RestaurantDetailView(RetrieveAPIView):
	queryset = Restaurant.objects.all()
	serializer_class = RestaurantDetailSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'restaurant_id'



# Complete me
class RestaurantUpdateView(UpdateAPIView):
	queryset = Restaurant.objects.all()
	serializer_class = RestaurantUpdateSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'restaurant_id'



# Complete me
class RestaurantDeleteView(DestroyAPIView):
	queryset = Restaurant.objects.all()
	serializer_class = RestaurantListSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'restaurant_id'
