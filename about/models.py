from django.db import models

# Create your models here.
class About(models.Model):
    # Title fieldld
    title = models.CharField(
        max_length=200,
        help_text="Enter the title of the About Page"
    )

    # Content field 
    content = models.TextField(
        help_text="Enter the main content for the About page"
    )

    # Updated On field
    updated_on = models.DateTimeField(
        auto_now=True,
        help_text="The date and time when the page was last updated"
    )

    # String representation
    def __str__(self):
        return self.title