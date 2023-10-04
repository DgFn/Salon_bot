from django.core.management.base import BaseCommand
from knopiproject.knopkibot import knopkibot 

class Command(BaseCommand):
    help = 'Runs the bot'

    def handle(self, *args, **options):
        bot = knopki()  # Создайте экземпляр вашего бота
        bot.run()  # Запустите бота
