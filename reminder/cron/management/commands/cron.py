from django.conf import settings
from django.core.management.base import BaseCommand
from django.utils import timezone
from linebot import LineBotApi
from linebot.exceptions import LineBotApiError
from linebot.models import TextSendMessage

from lecture.models import Task


class Command(BaseCommand):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.now = timezone.datetime.now()
        self.tasks = Task.objects.filter(enable=True)

    def handle(self, *args, **options):
        self.delete_task()
        self.tasks = self.get_valid_task()
        if len(self.tasks) > 0:
            message = self.make_message()
            self.remind(message)
        else:
            self.remind('No Tasks')

    def remind(self, message):
        line_bot_api = LineBotApi(settings.LINE_ACCESS_TOKEN)
        try:
            line_bot_api.push_message(
              settings.GROUP_ID,
              TextSendMessage(text=message),
            )
        except LineBotApiError as e:
            if e.status_code == 400:
                raise 'You have to post valide data'
            else:
                raise e

    def get_valid_task(self):
        tasks = self.tasks.filter(deadline__gte=self.now)
        return tasks

    def make_message(self):
        message = ''
        for task in self.tasks:
            message += '{}　{}'.format(
                task.lecture.name,
                task.deadline.strftime("締め切りは%m月%d日%H時%M分です."),
            )
            message += '\n'
        return message

    def delete_task(self):
        tasks = self.tasks.filter(deadline__lte=self.now)
        tasks.update(enable=False)
