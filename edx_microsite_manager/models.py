from django.conf import settings
from django.db import models
import json
import os


class Microsite(models.Model):
    domain_prefix = models.CharField(max_length=100)
    site_title = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='microsites/logos')

    def __unicode__(self):
        return self.site_title

    def save(self):
        super(Microsite, self).save()
        update_microsite_configuration()


def update_microsite_configuration():
    microsites = {
        "default": {
            "course_about_show_social_links": False,
        }
    }
    for m in Microsite.objects.all():
        # prepare MICROSITE_CONFIGURATION
        microsites[m.domain_prefix] = {
            'domain_prefix': m.domain_prefix,
            'university': m.site_title,
            'SITE_NAME': '{}.intersystems.com'.format(m.domain_prefix),
            'logo_image_url': '{}/images/{}'.format(m.domain_prefix, os.path.basename(m.logo.name)),
            'course_org_filter': m.domain_prefix,
            'course_about_show_social_links': False,
        }

        # put logo in place
        microsite_dir = os.path.join(settings.MICROSITE_ROOT_DIR, m.domain_prefix)
        images_dir = os.path.join(microsite_dir, 'images')
        if not os.path.exists(images_dir):
            os.makedirs(images_dir)
        image_path = os.path.join(images_dir, os.path.basename(m.logo.name))
        f = open(image_path, 'wb')
        f.write(m.logo.read())
        f.close()

    f = open('/edx/var/edxapp/microsites.json', 'w')
    f.write(json.dumps(microsites, indent=4))
    f.close()
