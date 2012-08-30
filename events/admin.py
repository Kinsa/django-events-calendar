from django.contrib import admin

from sorl.thumbnail.admin import AdminImageMixin

from events.models import Event


class EventAdmin(AdminImageMixin, admin.ModelAdmin):

    # use objects instead of the default manager
    def queryset(self, request):
        # use our manager, rather than the default one
        qs = self.model.objects.get_query_set()

        # we need this from the superclass method
        # provide an altenrative so we don't try to get *None
        ordering = self.ordering or ()
        if ordering:
            qs = qs.order_by(*ordering)
        return qs

    list_display = ('__unicode__', 'start_date', 'end_date',)
    list_filter = ('start_date', 'end_date',)
    prepopulated_fields = {'slug': ['name']}
    search_fields = ['name', 'start_date', 'end_date', 'description']

admin.site.register(Event, EventAdmin)
