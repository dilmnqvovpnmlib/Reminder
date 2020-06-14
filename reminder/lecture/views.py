from braces.views import CsrfExemptMixin
from django.conf import settings
from django.http import HttpResponse, HttpResponseForbidden
from django.views.generic import TemplateView
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
from rest_framework.viewsets import ModelViewSet

from lecture.serializers import (LectureSerializer, ProfessorSerializer,
                                 TaskSerializer)

from .models import Lecture, Professor, Task


class ProfessorViewSet(ModelViewSet):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer


class LectureViewSet(ModelViewSet):
    queryset = Lecture.objects.all()
    serializer_class = LectureSerializer


class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


line_bot_api = LineBotApi(settings.LINE_ACCESS_TOKEN)
handler = WebhookHandler(settings.LINE_CHANNEL_SECRET)


class Test(CsrfExemptMixin, TemplateView):
    def get(self, request, *args, **kwargs):
        return HttpResponse("hello")

    def post(self, request, *args, **kwargs):
        signature = request.META['HTTP_X_LINE_SIGNATURE']
        body = request.body.decode('utf-8')
        try:
            handler.handle(body, signature)
        except InvalidSignatureError:
            HttpResponseForbidden()
        return HttpResponse('OK', status=200)

    @handler.add(MessageEvent, message=TextMessage)
    def handle_text_message(event):
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="Hello ~")
            # オウム返し
            # TextSendMessage(text=event.message.text)
        )
