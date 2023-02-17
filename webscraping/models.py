from django.db import models
"""
Environmental evaluation projects model.
"""
class Project(models.Model):
    project_id = models.IntegerField(unique=True, blank=True, null=True)
    name = models.CharField(max_length=255)
    project_type = models.CharField(max_length=64)
    region = models.CharField(max_length=64)
    typology = models.CharField(max_length=64)
    titular = models.CharField(max_length=255)
    investment = models.DecimalField(default=0, max_digits=8, decimal_places=4)
    date = models.DateTimeField()
    status = models.CharField(max_length=122)
    map = models.URLField(max_length=255, default='')
    
    def __str__(self) -> str:
        return self.name

    def serialize(self):
        return {
            'project_id': self.project_id,
            'name': self.name,
            'project_type': self.project_type,
            'region': self.region,
            'typology': self.typology,
            'titular': self.titular,
            'investment': self.investment,
            'date': self.date.strftime('%d/%m/%Y'), 
            'status': self.status,
            'map': self.map
            }
