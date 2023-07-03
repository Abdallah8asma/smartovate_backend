from django.contrib import admin
from team.models import Team, TeamMember

@admin.register(Team)
class CategoryAdmin(admin.ModelAdmin):

    search_fields = ('title',)
    list_display = ('id', 'title', 'description')

@admin.register(TeamMember)
class CategoryAdmin(admin.ModelAdmin):

    search_fields = ('name',)
    list_display = ('id', 'name', 'image')
    

