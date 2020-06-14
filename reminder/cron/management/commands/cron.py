from django.conf import settings
from django.core.management.base import BaseCommand
from linebot import LineBotApi
from linebot.exceptions import LineBotApiError
from linebot.models import TextSendMessage

from lecture.models import Professor


class Command(BaseCommand):
    def handle(self, *args, **options):
        message = Professor.objects.get(pk=3)
        self.reminde(message.name)

    def reminde(self, message):
        line_bot_api = LineBotApi(settings.LINE_ACCESS_TOKEN)
        try:
            line_bot_api.push_message(
              settings.GROUP_ID,
              TextSendMessage(text=message)
            )
        except LineBotApiError as e:
            raise e
