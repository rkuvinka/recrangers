from django.conf.urls import url, include
from homepage.views import autocomplete_view, organization_detail, HomePageView, SearchResultsView
from . import views

urlpatterns = [
# url(r'^admin/', admin.site.urls),
url(r'^autocomplete/', autocomplete_view, name='autocomplete-view'),
url(r'^organization', organization_detail, name='organization-detail'),
url(r'^search', SearchResultsView.as_view(), name='search'),
url(r'^$', HomePageView.as_view(), name="index-view")


]