from django.db import models
from core import models as core_models


class Review(core_models.TimeStampModel):

    """ Review Model Definition """

    review = models.TextField()
    accuracy = models.IntegerField()
    communication = models.IntegerField()
    cleanliness = models.IntegerField()
    location = models.IntegerField()
    check_in = models.IntegerField()
    value = models.IntegerField()
    # user가 삭제되면 리뷰도 같이 삭제돼야함. 따라서 CASCADE
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    room = models.ForeignKey("rooms.Room", on_delete=models.CASCADE)

    def __str__(self):
        # fk로 설정한 값을 뿌려줄 수 있음.
        return f"{self.review} - {self.room}"
