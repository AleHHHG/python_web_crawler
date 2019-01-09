from django.contrib import admin

from .models import Product, Solution, Service, Log, CrawlerInstruction

class CrawlerInstructionAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, {'fields': ['kind','url','instrunction']})
	]
	list_display = ('kind', 'url')
# Register your models here.
admin.site.register(Product)
admin.site.register(Solution)
admin.site.register(Service)
admin.site.register(Log)
admin.site.register(CrawlerInstruction, CrawlerInstructionAdmin)