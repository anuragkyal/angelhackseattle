from django.db import models

class Plan(models.Model):
    plan_id = models.IntegerField()
    user_id = models.CharField(max_length=200)
    hotel_name = models.CharField(max_length=200)
    hotel_price = models.FloatField()
    rental_name = models.CharField(max_length=200)
    rental_price = models.FloatField()

    def __str__(self):              # __unicode__ on Python 2
        return self.question_text


class Interest(models.Model):
    plan_id = models.ForeignKey(Plan)
    friend_user_id = models.CharField(max_length=200)
    accepted = models.BooleanField(default=False)

    def __str__(self):              # __unicode__ on Python 2
        return self.question_text
