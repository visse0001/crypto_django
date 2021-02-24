from django.db import models

from pgcrypto import fields


class Producer(models.Model):
    name = models.CharField(max_length=128)


class ProducerSymmetric(models.Model):
    name = fields.CharPGPSymmetricKeyField(max_length=512)
    description = fields.CharPGPSymmetricKeyField(max_length=512)
    credentials = fields.CharPGPSymmetricKeyField(max_length=512)
