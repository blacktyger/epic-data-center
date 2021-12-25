from django.db import models


class Block(models.Model):
    """Epic-Cash block instance with explorer data"""

    class Algorithm(models.TextChoices):
        """Available EPIC algorithms"""
        CUCKOO = 'cuckoo'
        PROGPOW = 'progpow'
        RANDOMX = 'randomx'

    hash = models.CharField(max_length=128)
    algo = models.CharField(max_length=10, choices=Algorithm.choices)
    height = models.IntegerField(primary_key=True, unique=True)
    reward = models.DecimalField(max_digits=32, decimal_places=8)
    supply = models.IntegerField()
    avg_time = models.IntegerField()
    timestamp = models.IntegerField()

    total_diffs = models.JSONField(default=dict)
    target_diffs = models.JSONField(default=dict)
    network_hashrate = models.JSONField(default=dict)

    class Meta:
        ordering = ('-height', )

    def __str__(self):
        return f"Block({self.height})"

    def __repr__(self):
        return self.height
