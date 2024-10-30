import helpers

from typing import Any
from django.core.management.base import BaseCommand

VENDOR_STATICFILES = {
    "flowbite.min.css" : "https://cdnjs.cloudflare.com/ajax/libs/flowbite/2.3.0/flowbite.min.css",
    "flowbite.min.js" : "https://cdnjs.cloudflare.com/ajax/libs/flowbite/2.3.0/flowbite.min.js",

}

class Command(BaseCommand):
    def handle(self, *args: Any, **options: Any):
        self.stdout.write("Downloading Vendor Stattic Files")

        for name,url in VENDOR_STATICFILES.items():
            print(name,url)
        