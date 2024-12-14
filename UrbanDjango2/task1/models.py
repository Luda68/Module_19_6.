from django.db import models

# Create your models here.

class User(models.Model):
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email
class Buyer(models.Model):
    name = models.CharField(max_length=30)
    balance = models.DecimalField(max_digits=10, decimal_places=3)
    age = models.IntegerField()

    def __str__(self):
        return self.name


class Game(models.Model):
    title = models.CharField(max_length=30)
    cost = models.DecimalField(max_digits=10, decimal_places=3)
    size = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    age_limited = models.BooleanField(default=False)
    buyer = models.ManyToManyField(Buyer, related_name='buyers')

    def __str__(self):
        return self.title


"""python manage.py shell
from task1.models import Buyer, Game
Buyer.objects.create(name='Anna', balance=10000, age=21)
Buyer.objects.create(name='Roman', balance=30000, age=30)
Buyer.objects.create(name='Olga', balance=150, age=16)
Buyer.objects.all()
Buyer.objects.count()
Game.objects.create(title='Mario', cost=5, size=0.5, description='2D', age_limited=False)
Game.objects.create(title='Silent Hill 2', cost=300, size=120, description='horror', age_limited=True)
Game.objects.create(title='Cyberpunk', cost=500, size=102, description='RPG', age_limited=True)
Game.objects.all()
Game.objects.count()
buyer1=Buyer.objects.get(id=1)
buyer2=Buyer.objects.get(id=2)
buyer3=Buyer.objects.get(id=3)
Game.objects.get(id=1).buyer.set([buyer1, buyer2])
Game.objects.get(id=2).buyer.set([buyer1])
Game.objects.get(id=3).buyer.set([buyer1, buyer3])"""