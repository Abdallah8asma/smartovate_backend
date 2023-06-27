JAZZMIN_SETTINGS = {
    "site_title": "Caustaza",
    "site_header": "Caustaza",
    "site_brand": "Caustaza",
    "site_logo": "images/Logo.png",
    "login_logo": "images/logo_login.jpeg",
    "login_logo_dark": "logo_login.jpeg",
    "site_logo_classes": "images/Logo.png",
    "site_icon": "images/Logo.png",
    "welcome_sign": "Welcome to the Caustaza admin",
    "copyright": "caustaza",
    "search_model": "auth.User",
    "user_avatar": "images/Logo.png",
    "topmenu_links": [
        {"name": "Home", "url": "admin:index", "permissions": ["auth.view_user"]},
        {"model": "auth.User"},
        {"app": "books"},
    ],
    "usermenu_links": [
        {"name": "Support", "url": "https://github.com/farridav/django-jazzmin/issues", "new_window": True},
        {"model": "auth.user"}
    ],
    "show_sidebar": True,
    "navigation_expanded": True,
    "hide_apps": [],
    "hide_models": [],
    "order_with_respect_to": ["auth", "books", "books.author", "books.book"],
    "custom_links": {
        "books": [
            {"name": "Make Messages", "url": "make_messages", "icon": "fas fa-comments", "permissions": ["books.view_book"]}
        ]
    },
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
    },
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-circle",
    "related_modal_active": False,
    "custom_css": None,
    "custom_js": None,
    "show_ui_builder": True,
    "changeform_format": "horizontal_tabs",
    "changeform_format_overrides": {"auth.user": "collapsible", "auth.group": "vertical_tabs"},
}

JAZZMIN_UI_TWEAKS = {
    
   
    "accent": "accent-maroon",
   
    "sidebar": "sidebar-dark-maroon",
    
    "button_classes": {
        "primary": "btn-primary",
        "secondary": "btn-outline-secondary",
        "info": "btn-outline-info",
        "warning": "btn-outline-warning",
        "danger": "btn-outline-danger",
        "success": "btn-outline-success"
    },
}
