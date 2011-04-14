from django.contrib import admin

from testproject.blog.models import Entry

from testproject.blog.admin import EntryAdmin



from testproject.links.models import Link

from testproject.links.admin import LinkAdmin



class AdminSite(admin.AdminSite):

	pass
	
	
	
	
	
	
	
site = AdminSite()

site.register(Entry, EntryAdmin)

site.register(Link, LinkAdmin)