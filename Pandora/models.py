from django.db import models

# Create your models here.
class ToolGroupInfo(models.Model):
    group_name = models.CharField(max_length=32)

    def __unicode__(self):
        return self.group_name

class ToolInfo(models.Model):
    tool_name = models.CharField(max_length=64)
    tool_summary = models.CharField(max_length=128)
    tool_url = models.CharField(max_length=256)
    tool_imgaddr = models.CharField(max_length=128)
    tool_group = models.ForeignKey(ToolGroupInfo)

    def __unicode__(self):
        return self.tool_name

