from django.db import models

class Transaction(models.Model):
    timestamp = models.DateTimeField(auto_now=True)  # Automatically updates the timestamp on creation or modification
    transaction_amount = models.DecimalField(max_digits=10, decimal_places=2)  # To handle monetary values
    transaction_name = models.CharField(max_length=255)  # Name or description of the transaction
    bill_url = models.URLField(max_length=500, blank=True, null=True)  # Optional field for bill URL
    transaction_screenshot_url = models.URLField(max_length=500, blank=True, null=True)  # Optional field for screenshot URL
    account_balance = models.DecimalField(max_digits=10, decimal_places=2)  # Account balance after this transaction
    comments = models.TextField(blank=True, null=True)  # Optional field for additional comments

    class Meta:
        ordering = ['-timestamp']  # Transactions ordered by timestamp descending
        verbose_name = 'Transaction'
        verbose_name_plural = 'Transactions'

    def __str__(self):
        return f"{self.transaction_name} - {self.transaction_amount} ({self.timestamp})"
