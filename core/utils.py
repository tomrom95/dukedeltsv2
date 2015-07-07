from django.contrib.auth.models import User
from dukedelts.secret import SOCIAL_AUTH_GOOGLE_OAUTH2_WHITELISTED_EMAILS as emails

def associate_by_email(**kwargs):
    try:
        email = kwargs['details']['email']
        kwargs['user'] = User.objects.get(email=email)
    except:
        pass
    return kwargs

def add_users():
	for email in emails:
		username = email.split('@')[0]
		try:
			User.objects.create_user(username=username, email=email)
		except:
			print "pass"


