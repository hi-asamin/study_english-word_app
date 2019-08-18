from django.db import models
from django.core import validators

class Word(models.Model):
    word = models.CharField(
        max_length=50,
        validators=[validators.RegexValidator(
            regex=u'^[a-zA-Z]+$',
            message='半角英字のみ単語登録可能です',
        )]
    )
    mean1 = models.CharField(
        max_length=100
    )
    mean2 = models.CharField(
        max_length=100,
        default='',
        null=True
    )
    mean3 = models.CharField(
        max_length=100,
        default='',
        null=True
    )
    part_of_speech = models.PositiveSmallIntegerField()
    create_datetime = models.DateTimeField(
        auto_now_add = True,
    )
    update_datetime = models.DateTimeField(
        auto_now = True
    )
    logical_delete_flag = models.BooleanField(
        default=False
    )
