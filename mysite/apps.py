from django.contrib.admin.apps import AdminConfig


class PollAdminConfig(AdminConfig):
    default_site = "mysite.admin.PollAdminSite"
