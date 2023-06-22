from django.db import models


class Brand(models.Model):
    """ Model class for brand """
    name = models.CharField(max_length=255)
    status = models.BooleanField(default=True)

    def __str__(self):
        """ String Represenation of object Brand """
        return self.name