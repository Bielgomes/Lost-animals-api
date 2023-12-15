from rest_framework import permissions
from rest_framework.viewsets import ViewSet


class AnimalRetrieveViewSet(ViewSet):

    def retrieve(self, request):
        pass


class AnimalViewSet(ViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def retrieve(self, request):
        pass

    def create(self, request):
        pass

    def patch(self, request):
        pass

    def delete(self, request):
        pass
