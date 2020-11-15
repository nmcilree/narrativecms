from django.db import models

# Create your models here.


class Page(models.Model):
    title = models.CharField(max_length=255, blank=True)
    body = models.TextField(max_length=255, blank=True)
    left = models.IntegerField(blank=True, null=True)
    top = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.title


class PageConnector(models.Model):
    # The page that this connector applies to
    page = models.ForeignKey('Page', on_delete=models.CASCADE, related_name='connectors', null=True)
    # The destination of this connector
    destination = models.ForeignKey('Page', on_delete=models.CASCADE, related_name='exits', null=True, blank=True)
    # The origin of this connector
    origin = models.ForeignKey('Page', on_delete=models.CASCADE, related_name='entrypoints', null=True, blank=True)

    @property
    def get_origin(self):
        return self.origin.all()[:1]

    @property
    def get_destination(self):
        return self.destination.all()[:1]



    def __str__(self):
        return "Connector for {}".format(self.page.title)