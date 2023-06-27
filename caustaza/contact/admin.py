from django.contrib import admin
from .models import Contact

# Define the ContactAdmin class
class ContactAdmin(admin.ModelAdmin):
    # Define the fields to display in the admin list view
    list_display = (
        'id',
        'full_name',
        'email',
        'phone',
        'adress',
        'message',
        'created_at',
        'updated_at',
    )
    
    # Define the fields to use for filtering in the admin list view
    list_filter = (
        'full_name',
        'email',
        'phone',
    )
    
    # Define the date hierarchy for the admin list view
    date_hierarchy = 'created_at'

# Register the Contact model with the ContactAdmin class
admin.site.register(Contact, ContactAdmin)
