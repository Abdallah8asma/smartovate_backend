from django.contrib import admin
from .models import Pageindex, FeedbackClient

@admin.register(Pageindex)
class PageindexAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'subtitle',
        'description',
        'about_title',
        'about_description',
        'service_title',
        'service_subtitle',
        'service_description',
        'feedback_title',
        'feedback_subtitle',
        'call_to_action_title',
        'call_to_action_subtitle',
        'meta_title',
        'meta_description',
    )
    list_filter = (
        'title',
    )

@admin.register(FeedbackClient)
class FeedbackClientAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'avatar',
        'description',
        'created_at',
        'updated_at',
    )
    list_filter = (
        'created_at',
        'updated_at',
    )
    search_fields = ('name',)
    date_hierarchy = 'created_at'
