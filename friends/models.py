from django.db import models

class UserFriends(models.Model):
    user_id = models.BigIntegerField()
    friend_id = models.BigIntegerField()
    friend_name = models.CharField(max_length=150)

    class Meta:
        unique_together = (('user_id', 'friend_id'),)
