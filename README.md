
Django Timestamps
=======================

Adds created_at, updated_at, and/or deleted_at (soft-delete) to django models

Usage
=====

    from django.db import models
    from django_timestamps.softDeletion import SoftDeletionModel
    from django_timestamps.timestamps import TimestampsModel

    class Device(SoftDeletionModel, TimestampsModel):
        name = models.CharField(max_length=20)
        os = models.CharField(max_length=20)

TimestampsModel adds created_at and updated_at fields to the model. This fields are updated automatically

SoftDeletionModel adds deleted_at (soft-delete)

To soft-delete a model you must call delete() function:

    device = Device.objects.filter(id=1).first()
    device.delete()

To hard-delete a model you must call hard_delete() function:

    device = Device.objects.filter(id=1).first()
    device.hard_delete()

To restore a model you must call restore() function and use all_objects instead of objects:

    device = Device.all_objects.filter(id=1).first()
    device.restore()

To get all objects trashed

    devices_trashed = Device.all_objects.all().dead()


ModelViewSet for rest_framework:
===================

Adds urls for soft-deleted elements, returns deleted_at:

    #Example for devices:
    #    (get)   /devices/trashed/       -> trashed elements, paginated
    #    (get)   /devices/4/get-trashed/ -> get trashed element
    #    (patch) /devices/4/restore/     -> restore trashed element

    from django_timestamps.SoftDeleteViewSet import SoftDeleteViewSet

    class DeviceViewSet(viewsets.ModelViewSet, SoftDeleteViewSet):
        queryset = Device.objects.all().order_by('id')
        serializer_class = DeviceSerializer
        querysetTrashed = Device.all_objects.all().dead().order_by('id')

        #add extra filters for queryset and querysetTrashed
        def full_queryset(self, queryset):

            user_id = self.request.query_params.get('user_id', None)
            if user_id:
                queryset = queryset.filter(user_id=user_id)

            return queryset




