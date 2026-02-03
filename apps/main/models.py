from django.db import models

def cover_image_upload_path(instance, filename):
    return f'volumes/volume_{instance.number}/cover/{filename}'

def article_pdf_upload_path(instance, filename):
    return f'volumes/volume_{instance.volume.number}/articles/{filename}'

class Volume(models.Model):
    number = models.PositiveIntegerField(unique=True)
    cover_image = models.ImageField(upload_to=cover_image_upload_path, blank=True, null=True)
    date = models.DateField()

    class Meta:
        ordering = ['-number']
        verbose_name = 'Journal Volume'
        verbose_name_plural = 'Journal Volumes'

    def __str__(self):
        return f"Volume {self.number} ({self.date.strftime('%B %Y')})"


class Article(models.Model):
    volume = models.ForeignKey(Volume, on_delete=models.CASCADE, related_name='articles')
    title = models.CharField(max_length=500)
    authors = models.TextField(help_text="Comma-separated authors")
    abstract = models.TextField(blank=True, help_text="Summary of the article")
    keywords = models.CharField(max_length=500, blank=True, help_text="Comma-separated keywords for search")
    doi = models.URLField(blank=True, null=True, verbose_name="DOI", help_text="Digital Object Identifier link for the article (if available).")
    pdf = models.FileField(upload_to=article_pdf_upload_path, blank=True, null=True)
    page_start = models.PositiveIntegerField()
    page_end = models.PositiveIntegerField()
    references = models.TextField(blank=True, help_text="References or bibliography")

    class Meta:
        ordering = ['volume', 'page_start']

    def __str__(self):
        return f"{self.title} (Vol {self.volume.number}: pp. {self.page_start}–{self.page_end})"