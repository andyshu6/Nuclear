from django.db import models

# Create your models here.
class ToolGroupInfo(models.Model):
    group_code = models.CharField(max_length=32)
    group_parent = models.IntegerField(null=True,blank=True)
    group_name = models.CharField(max_length=32)

    def __unicode__(self):
        return self.group_name

class ToolInfo(models.Model):
    tool_name = models.CharField(max_length=64)
    tool_desc = models.CharField(max_length=128,null=True,blank=True)
    tool_url = models.CharField(max_length=256)
    tool_imgaddr = models.CharField(max_length=128,null=True,blank=True)
    tool_heat = models.IntegerField(default=0)
    tool_group = models.ManyToManyField(ToolGroupInfo, related_name="type")

    def __unicode__(self):
        return self.tool_name

