In the Google API Console - https://code.google.com/apis/console/:

#. Create a Project
#. In Services, enable Google+ API
#. In API Access for your project, create a Client ID. Set the Authorized Redirect URIs to "http://mydomain.com/google/callback/" and Authorized Javascript Origins to your domain.




You need to set the following in your settings.py

* DOMAIN
* GOOGLE_API_KEY, GOOGLE_CLIENT_ID and GOOGLE_CLIENT_SECRET - get the values at the Google API Console: https://code.google.com/apis/console/




