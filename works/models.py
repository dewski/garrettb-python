from django.db import models

class Work(models.Model):
    title = models.CharField(blank=False, max_length=100)
    url = models.URLField(blank=False, verify_exists=True)
    
    
    def __unicode__(self):
        return self.title

class WorkItem(models.Model):
    work = models.ForeignKey(Work)
    asset = models.FileField()