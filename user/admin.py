from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from user.models import User

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (
            None, {
                "fields": (
                    "username",
                    "password",
                )
            }
        ),
        (
            "Información personal", {
                "fields": (
                    "first_name",
                    "last_name",
                    "email",                    
                    "dni",
                )
            }
        ),
        (
            "Redes sociales", {
                "fields": (
                    "web_site",
                )
            }
        ),
        (
            "Permisos", {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            }
        ),
        (
            "Fechas importantes", {
                "fields": (
                    "last_login",
                    "date_joined",
                )
            }
        ),      
    )
