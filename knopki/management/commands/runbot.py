from django.core.management.base import BaseCommand
from knopki import knopkibot

class Command(BaseCommand):
    help = 'Runs the bot'

    def handle(self, *args, **options):
        knopkibot.polling(none_stop=True, interval=0)
       