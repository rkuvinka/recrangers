from elasticsearch.client import IndicesClient
from django.conf import settings
from django.core.management.base import BaseCommand
from homepage.models import Organization, RecreationalActivity
from elasticsearch.helpers import bulk

index_name = 'django'

class Command(BaseCommand):

	def handle(self, *args, **options):

		self.recreate_index()
		self.push_db_to_index()

	def recreate_index(self):
		indices_client = IndicesClient(client=settings.ES_CLIENT)

		if indices_client.exists(index_name):
			indices_client.delete(index=index_name)
		indices_client.create(index=index_name)

		indices_client.put_mapping(
			doc_type=Organization._meta.es_type_name,
			body=Organization._meta.es_mapping,
			index=index_name
		)
		indices_client.put_mapping(
			doc_type=RecreationalActivity._meta.es_type_name,
			body=RecreationalActivity._meta.es_mapping,
			index=index_name
		)

	def push_db_to_index(self):
		data = [self.convert_for_bulk(s, 'create') for s in Organization.objects.all()]
		bulk(client=settings.ES_CLIENT, actions=data, stats_only=True)

		data = [self.convert_for_bulk(s, 'create') for s in RecreationalActivity.objects.all()]
		bulk(client=settings.ES_CLIENT, actions=data, stats_only=True)

	def convert_for_bulk(self, django_object, action=None):
		data = django_object.es_repr()
		metadata = {
            '_op_type': action,
            "_index": django_object._meta.es_index_name,
            "_type": django_object._meta.es_type_name,
        }
		data.update(**metadata)
		return data