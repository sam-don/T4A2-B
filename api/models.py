from django.core import validators
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

class Record(models.Model):
    title = models.CharField(max_length=64)
    artist = models.CharField(max_length=64)

    def num_ratings(self):
        ratings = Rating.objects.filter(record=self)
        return len(ratings)

    def avg_rating(self):
        sum = 0
        ratings = Rating.objects.filter(record=self)
        for rating in ratings:
            sum += rating.stars
        if len(ratings) > 0:
            return sum / len(ratings)
        else:
            return 0

class Rating(models.Model):
    record = models.ForeignKey(Record, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stars = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    class Meta:
        unique_together = (('user', 'record'),)
        index_together = (('user', 'record'),)
