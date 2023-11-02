from django.contrib import admin
from .models import New_Query, Keyword


class KeywordAdmin(admin.ModelAdmin):
    list_display = ["keyword_text", "volume"]
    search_fields = ["keyword_text"]


class New_QueryAdmin(admin.ModelAdmin):
    list_display = ["query_text"]
    search_fields = ["query_text"]


admin.site.register(Keyword, KeywordAdmin)
admin.site.register(New_Query, New_QueryAdmin)
