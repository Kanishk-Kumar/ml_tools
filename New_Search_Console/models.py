from django.db import models


class New_Query(models.Model):
    query_text = models.CharField(max_length=200)

    def __str__(self):
        return str(self.query_text)


class Keyword(models.Model):
    keyword_text = models.ForeignKey(New_Query, on_delete=models.CASCADE)
    volume = models.IntegerField(default=0)

    def __str__(self):
        return str(self.keyword_text)
