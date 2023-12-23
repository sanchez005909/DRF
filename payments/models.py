import uuid
from django.db import models
from curses.models import Curs, NULLABLE


class StripeCheckoutSession(models.Model):
    stripe_id = models.CharField(max_length=255, unique=True, editable=False)
    curs = models.ForeignKey(Curs, on_delete=models.CASCADE)
    status = models.CharField(max_length=10)
    customer_email = models.EmailField(null=True, blank=True)
    url = models.URLField(max_length=400, **NULLABLE)