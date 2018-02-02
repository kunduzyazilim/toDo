from django.db import models

class toDoList_Tab:
    toDoIcerik=models.CharField()
    toDoYazan=models.CharField()
    yapildi=models.CharField()
    def __unicode__(self):
        return self.toDoIcerik
