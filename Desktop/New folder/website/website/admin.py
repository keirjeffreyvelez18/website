from django.contrib import admin
from . models import Program, NewsPost, FacultyMember, ResearchTitle, OutreachPost, UpcomingEvent, Alumni
admin.site.register(Program)
admin.site.register(NewsPost)
admin.site.register(FacultyMember)
admin.site.register(ResearchTitle)
admin.site.register(OutreachPost)
admin.site.register(UpcomingEvent)
admin.site.register(Alumni)

# @admin.register(NewsPost)
# class NewsPostAdmin(admin.ModelAdmin):
#     change_list_template = 'admin/newspost_list.html'
#     date_hierarchy = 'news_date'