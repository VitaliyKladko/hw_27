import json

from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from django.views.generic import DetailView

from ads.models import Categories, AdsModel


def index(request):
    return JsonResponse({"status": "ok"}, status=200)


@method_decorator(csrf_exempt, name='dispatch')
class CategoriesView(View):
    def get(self, request):
        categories = Categories.objects.all()

        response = []
        for category in categories:
            response.append(
                {
                    'id': category.id,
                    'name': category.name,
                }
            )

        return JsonResponse(response, safe=False)

    def post(self, request):
        category_data = json.loads(request.body)

        category = Categories()
        category.name = category_data['name']
        category.save()

        return JsonResponse({
            'id': category.id,
            'name': category.name,
        })


class CategoriesDetailView(DetailView):
    model = Categories

    def get(self, request, *args, **kwargs):
        try:
            category = self.get_object()
        except Categories.DoesNotExist:
            return JsonResponse({'error': 'Not found'}, status=404)

        return JsonResponse({
            'id': category.id,
            'name': category.name,
        })


@method_decorator(csrf_exempt, name='dispatch')
class AdsView(View):
    def get(self, request):
        ads = AdsModel.objects.all()

        response = []
        for i in ads:
            response.append(
                {
                    'id': i.id,
                    'name': i.name,
                    'author': i.author,
                    'price': i.price,
                    'description': i.description,
                    'address': i.address,
                    'is_published': i.is_published,
                }
            )

        return JsonResponse(response, safe=False)

    def post(self, request):
        ads_data = json.loads(request.body)

        ads = AdsModel(**ads_data)
        ads.save()

        return JsonResponse(
            {
                'id': ads.id,
                'name': ads.name,
                'author': ads.author,
                'price': ads.price,
                'description': ads.description,
                'address': ads.address,
                'is_published': ads.is_published,
            }
        )


class AdsDetailView(DetailView):
    model = AdsModel

    def get(self, request, *args, **kwargs):
        try:
            ads = self.get_object()
        except AdsModel.DoesNotExist:
            return JsonResponse({'error': 'Not found'}, status=404)

        return JsonResponse(
            {
                'id': ads.id,
                'name': ads.name,
                'author': ads.author,
                'price': ads.price,
                'description': ads.description,
                'address': ads.address,
                'is_published': ads.is_published,
            }
        )
