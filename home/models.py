from django.db import models

class SiteDetails(models.Model):
    """Model definition for SiteDetails."""

    name = models.CharField(max_length=100)
    value = models.CharField(max_length=100)

    def __str__(self):
        """Unicode representation of SiteDetails."""
        return self.name

    class Meta:
        """Meta definition for SiteDetails."""

        verbose_name = 'SiteDetails'
        verbose_name_plural = 'SiteDetails'

        def __str__(self):
            """Unicode representation of SiteDetails."""
            return self.name