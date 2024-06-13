from django.db import models
from .utils import vote_id_number

# Create your models here.
class Candidates(models.Model):
    sl_number = models.AutoField(primary_key=True)
    candidate_name = models.CharField(max_length=100)
    votes = models.IntegerField(default=0)
    candidate_party = models.CharField(max_length=100)
   
    class Meta:
        verbose_name_plural = 'Candidates'

    def __str__(self) -> str:
        return self.candidate_name


class Voters(models.Model):
    name = models.CharField(max_length=200)
    age = models.SmallIntegerField()
    mobile_number = models.CharField(max_length=10, unique=True)
    card_number = models.CharField(max_length=10, unique=vote_id_number())
    already_vote = models.BooleanField(default=False)
    voted_for = models.ForeignKey(Candidates, on_delete=models.CASCADE, null=True, blank=True)


    def save(self):
        if not self.card_number:
            self.card_number = vote_id_number()
        super().save()

    class Meta:
        verbose_name_plural = 'Voters'

