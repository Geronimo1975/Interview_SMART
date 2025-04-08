# documents/models.py
from django.db import models
from django.conf import settings
from core.models import TimeStampedModel, Tag, Category

class Document(TimeStampedModel):
    DOCUMENT_TYPE_CHOICES = (
        ('resume', 'Resume/CV'),
        ('cover_letter', 'Cover Letter'),
        ('certificate', 'Certificate'),
        ('reference', 'Reference Letter'),
        ('template', 'Interview Template'),
        ('report', 'Interview Report'),
        ('other', 'Other'),
    )
    
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    file = models.FileField(upload_to='documents/')
    document_type = models.CharField(max_length=20, choices=DOCUMENT_TYPE_CHOICES)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='documents')
    tags = models.ManyToManyField(Tag, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    is_template = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title

class Template(TimeStampedModel):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    content = models.TextField()
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)
    
    def __str__(self):
        return self.name