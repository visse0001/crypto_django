from django.db import models

from pgcrypto import fields


class Producer(models.Model):
    name = models.CharField(max_length=128)


class ProducerSymmetric(models.Model):
    name = fields.CharPGPSymmetricKeyField()
    description = fields.CharPGPSymmetricKeyField()
    credentials = fields.CharPGPSymmetricKeyField()
