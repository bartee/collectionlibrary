from django.views.generic import TemplateView

from catalog.services import get_collections_for_user, get_entities_for_user


class DashboardView(TemplateView):
    template_name = "dashboard.html"

    def get_context_data(self, **kwargs):
        """
        Return all users' collections and all the current users' entities for rendering

        :param kwargs:
        :return:
        """
        context = super(DashboardView, self).get_context_data(**kwargs)

        context["collections"] = get_collections_for_user(self.request.user)
        context["entities"] = get_entities_for_user(self.request.user)

        return context
