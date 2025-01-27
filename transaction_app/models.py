from django.db import models


class Transaction(models.Model):
    timestamp = models.DateTimeField(auto_now=True)
    transaction_amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_name = models.CharField(max_length=255)
    bill_url = models.URLField(max_length=500, blank=True, null=True)
    transaction_screenshot_url = models.URLField(
        max_length=500, blank=True, null=True)
    account_balance = models.DecimalField(max_digits=10, decimal_places=2)
    comments = models.TextField(blank=True, null=True)
    TRANSACTION_TYPES = [
        ("Cr", "Credit"),
        ("Dr", "Debit"),
    ]
    transaction_type = models.CharField(
        max_length=2, choices=TRANSACTION_TYPES)

    class Meta:
        ordering = ['-timestamp']
        verbose_name = 'Transaction'
        verbose_name_plural = 'Transactions'

    def __str__(self):
        return f"{self.transaction_name} - {self.transaction_amount} ({self.timestamp})"
