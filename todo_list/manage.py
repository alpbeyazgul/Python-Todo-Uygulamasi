import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "todo_list.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        # Hata mesajını güncelleyebilirsiniz
        raise ImportError(
            "Django yüklü olmadığından emin olun. "
            "Yükleme talimatları için https://docs.djangoproject.com/en/ bağlantısına bakabilirsiniz."
        )
    execute_from_command_line(sys.argv)
