from django.db import models

# Create your models here.
class Login(models.Model):
    roll = models.IntegerField(db_column='Roll', blank=True, null=True)  # Field name made lowercase.
    pass_field = models.CharField(db_column='pass', max_length=20, blank=True, null=True)  # Field renamed because it was a Python reserved word.
    name = models.CharField(max_length=50, blank=True, null=True)
    branch = models.CharField(max_length=50, blank=True, null=True)
    hostel = models.CharField(max_length=20, blank=True, null=True)
    alloted = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'Login'




class Room(models.Model):
    number = models.CharField(max_length=10, blank=True, null=True)
    occupancy = models.IntegerField(blank=True, null=True)
    aval = models.IntegerField(blank=True, null=True)
    floor = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.number

    class Meta:
        managed = False
        db_table = 'Room'

