from django.contrib import admin

from .models import Task


class TaskAdmin(admin.ModelAdmin):
    readonly_fields = ("created",)
    list_display = ["title", "important", "get_username"]

    def get_username(self, obj):
        return obj.user.username

    get_username.admin_order_field = 'user'  # Permite ordenar por este campo
    get_username.short_description = 'Username'  # Define el nombre de la columna en el administrador


admin.site.register(Task, TaskAdmin)
