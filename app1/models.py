from django.db import models
from django.db.models import Manager

class DocumentQuerySet(models.QuerySet):
    def pdfs(self):
        return self.filter(file_type='pdf')

    def smaller_than(self, size):
        return self.filter(size__lt=size)

class DocumentManager(models.Manager):
    def get_queryset(self):
        return DocumentQuerySet(self.model, using=self._db)  # Important!

    def pdfs(self):
        return self.get_queryset().pdfs()

    def smaller_than(self, size):
        return self.get_queryset().smaller_than(size)

class Document(models.Model):
    name = models.CharField(max_length=30)
    size = models.PositiveIntegerField(default=0)
    file_type = models.CharField(max_length=10, blank=True)

    objects = DocumentManager()

    def __str__(self):
    	return '%s %d %s' %(self.name,self.size,self.file_type)

    def _get_full_name(self):
        return '%s %s' % (self.name, self.file_type)  # Returns the person's full name.
    full_name = property(_get_full_name)
    
    def __unicode__(self):
        return self.full_name



