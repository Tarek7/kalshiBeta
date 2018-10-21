from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_date = models.DateField(null=True, blank=True)
    wallet_number = models.CharField(max_length=200)
    balance = models.FloatField(default=0)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    def __str__(self):
        return self.user.username


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    rules = models.TextField()
    settle_time = models.DateTimeField()

    category_choices = (
        ('Sports', 'Sports'),
        ('eSports', 'eSports'),
        ('Entertainmnet', 'Entertainmnet'),
        ('Financials', 'Financials'),
        ('Politics', 'Politics'),
        ('Random', 'Random'),
    )
    category = models.CharField(max_length=20, choices=category_choices)
    pending = models.BooleanField(default=True)
    settled = models.BooleanField(default=False)

    def __str__(self):
        return self.question_text


class Bet(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    yes_user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='yes_bet')
    no_user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='no_bet')
    pay_amount = models.FloatField()
    receive_amount = models.FloatField()
    resolved = models.BooleanField(default=False)

    def __str__(self):
        return "{}/{}".format(self.yes_user.username, self.no_user.username)
