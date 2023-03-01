import json

from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from django.views.generic import DetailView

from ads.models import Categories


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
