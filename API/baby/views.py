from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets

from guardian.shortcuts import assign_perm
from permissions.services import APIPermissionClassFactory
from baby.models import Baby
from baby.serializers import BabySerializer


class BabyViewSet(viewsets.ModelViewSet):
    queryset = Baby.objects.all()
    serializer_class = BabySerializer
    permission_classes = (
            APIPermissionClassFactory(
                name='BabyPermissions',
                permission_configuration={
                    'base': {
                        'create': True,
                        'list': False,
                        'getAllBabies': True
                    },
                    'instance': {
                        'retrieve': 'baby.view_baby',
                        'destroy': False,
                        'update': True,
                        'partial_update': 'baby.change_baby',
                        # 'update_permissions': 'users.add_permissions'
                        # 'archive_all_students': phase_user_belongs_to_school,
                        # 'add_clients': True,
                    }
                }
            ),
        )


    @action(detail=False, url_path='all', methods=['get'])
    def getAllBabies(self, request):
            allBabies = []
            print("SI entro bor!!!!")
            for b in Baby.objects.all():
                if b.parent == self.request.user:
                    allBabies.append(BabySerializer(b).data)
            return Response(allBabies)

    def perform_create(self, serializer):
        baby = serializer.save()
        user = self.request.user
        assign_perm('baby.change_baby', user, baby)
        assign_perm('baby.view_baby', user, baby)
        return Response(serializer.data)


        
