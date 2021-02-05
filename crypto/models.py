from django.db import models

from pgcrypto import fields


class MyModel(models.Model):
    hostname = fields.TextDigestField()


class Producer(models.Model):
    name = fields.TextPGPPublicKeyField()
    email = fields.EmailPGPSymmetricKeyField()


class Default(models.Model):
    name = models.TextField()
