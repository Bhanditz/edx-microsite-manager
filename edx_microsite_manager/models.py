from django.db import models
from urlparse import urlparse
import json



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
        #remove query string from logo url
        p_url = urlparse(m.logo.url)
        logo_url = ''.join([p_url.scheme,'://',p_url.netloc,p_url.path])

        # prepare MICROSITE_CONFIGURATION
        microsites[m.domain_prefix] = {
            'domain_prefix': m.domain_prefix,
            'university': m.site_title,
            'SITE_NAME': '{}.intersystems.com'.format(m.domain_prefix),
            'logo_image_url': logo_url,
            'course_org_filter': m.domain_prefix,
            'course_about_show_social_links': False,
        }

    f = open('/edx/var/edxapp/microsites.json', 'w')
    f.write(json.dumps(microsites, indent=4))
    f.close()
