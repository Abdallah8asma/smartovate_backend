from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from django.forms.models import inlineformset_factory
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import MyUserProfile  

def upgrade_user_admin(UserProfile=None, unique_email=False, list_display=None):
    if UserProfile:
        class UserProfileFormSet(inlineformset_factory(User, UserProfile, fields='__all__')):
            def __init__(self, *args, **kwargs):
                super(UserProfileFormSet, self).__init__(*args, **kwargs)
                self.can_delete = False

        # Allow user profiles to be edited inline with User
        class UserProfileInline(admin.StackedInline):
            model = UserProfile
            fk_name = 'user'
            max_num = 1
            extra = 0
            formset = UserProfileFormSet

    # use these form classes to enforce unique emails, if required
    class UniqueEmailForm:
        def clean_email(self):
            qs = User.objects.filter(email=self.cleaned_data['email'])
            if self.instance:
                qs = qs.exclude(pk=self.instance.pk)
            if qs.count():
                raise forms.ValidationError(
                    'That email address is already in use')
            else:
                return self.cleaned_data['email']

    class MyUserChangeForm(UniqueEmailForm, UserChangeForm):
        email = forms.EmailField(required=True)

    class MyUserCreationForm(UniqueEmailForm, UserCreationForm):
        email = forms.EmailField(required=True)

    class MyUserAdmin(UserAdmin):
        # add the email field in to the initial add_user form
        add_fieldsets = (
            (None, {
                'classes': ('wide',),
                'fields': ('username', 'email', 'password1', 'password2')
            }),
        )

        inlines = [UserProfileInline, ] if UserProfile else []
        actions = ['make_active', 'make_inactive']
        list_filter = ['is_active', 'is_staff', 'is_superuser', 'date_joined',
                       'last_login']

        form = MyUserChangeForm if unique_email else UserChangeForm
        add_form = MyUserCreationForm if unique_email else UserCreationForm

        def make_active(self, request, queryset):
            rows_updated = queryset.update(is_active=True)
            if rows_updated == 1:
                message_bit = "1 person was"
            else:
                message_bit = "%s people were" % rows_updated
            self.message_user(
                request, "%s successfully made active." % message_bit)

        def make_inactive(self, request, queryset):
            rows_updated = queryset.update(is_active=False)
            if rows_updated == 1:
                message_bit = "1 person was"
            else:
                message_bit = "%s people were" % rows_updated
            self.message_user(
                request, "%s successfully made inactive." % message_bit)

    if list_display:
        MyUserAdmin.list_display = list_display

    # Re-register UserAdmin with custom options
    admin.site.unregister(User)
    admin.site.register(User, MyUserAdmin)

# Call the upgrade_user_admin function with the necessary parameters
upgrade_user_admin( unique_email=True)