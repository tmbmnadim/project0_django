from django.db import models

class SiteDetails(models.Model):
    """Model definition for SiteDetails."""

    name = models.CharField(max_length=100)
    about = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    partner = models.CharField(max_length=100)
    

    def save(self, *args, **kwargs):
        if SiteDetails.objects.exists() and not self.pk:
            raise ValueError('There can only be one SiteDetails instance.')
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'SiteDetails'
        verbose_name_plural = 'SiteDetails'

class Services(models.Model):
    """Model definition for Services."""
    site_details = models.ForeignKey(SiteDetails, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    details = models.CharField(max_length=100)

    def __str__(self):
        return self.name