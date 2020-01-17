from django.db import models


class TimeStampModel(models.Model):

    """ Time stamped model"""

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        # abstract = True : 코드에서만 사용되고 DB에는 해당 model이 등록되지 않음
        abstract = True
