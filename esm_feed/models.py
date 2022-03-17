from django.db import models

class Update(models.Model):
    """Up to date Epic-Cash related versions, links, etc"""
    timestamp = models.DateTimeField(auto_now=True)
    core_software = models.JSONField(default=dict)
    keybase = models.JSONField(default=dict)
    other = models.JSONField(default=dict)
    tor = models.JSONField(default=dict)

    def __str__(self):
        return f"ESMUpdate [{str(self.timestamp)}]"

    def __repr__(self):
        return f"ESMUpdate [{str(self.timestamp)}]"
