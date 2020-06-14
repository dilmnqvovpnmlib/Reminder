from django.db import models

from reminder.models import ModelBase


class Professor(ModelBase):
    class Meta:
        ordering = ['created']

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Lecture(ModelBase):
    PERIOD_CHOICES = (
        (0, "前期"),
        (1, "後期"),
    )

    class Meta:
        ordering = ['created']

    name = models.CharField(max_length=100)
    professor = models.ForeignKey(
        Professor,
        verbose_name="担当教員",
        on_delete=models.CASCADE,
    )
    year = models.IntegerField(verbose_name="年度")
    period = models.IntegerField(verbose_name="学期", choices=PERIOD_CHOICES)

    def __str__(self):
        return self.name


class Task(ModelBase):
    class Meta:
        ordering = ['created']

    name = models.CharField(max_length=100)
    deadline = models.DateTimeField("締め切り")
    lecture = models.ForeignKey(
        Lecture,
        verbose_name="講義科目",
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name
