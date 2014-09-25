Microsite Manager for EdX
=========================

This provides a UI in the Django Admin for configuring EdX microsites.

It updates a JSON file on disk. Loading the JSON into the MICROSITE_CONFIGURATION setting
is left as an exercise.

Installation
------------

1. Install the package using pip:
    - `pip install -e git+https://github.com/jazkarta/edx-microsite-manager`
2. Add edx_microsite_manager to INSTALLED_APPS in Django ettings.
3. Access the Django admin; you should see the Microsite object.
