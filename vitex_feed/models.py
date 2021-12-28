from django.db import models

class VitexHoldersUpdate(models.Model):
    timestamp = models.DateTimeField(auto_now=True)
    holders_count = models.IntegerField()
    holders_stats = models.JSONField(default=dict)

    class Meta:
        ordering = ('-timestamp', )

    def __repr__(self):
        return f"VitexHolders [{self.timestamp}]"

