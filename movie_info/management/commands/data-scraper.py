from django.core.management.base import BaseCommand
from data_processor.processor import data_processor

class Command(BaseCommand):
    help = 'Scrap Data From Wiki'

    def handle(self, *args, **kwargs):
        data_processor()