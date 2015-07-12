from django.contrib.auth.models import User
from .models import Profile
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

def fill_users(text_file):
    entries = []
    with open(text_file) as f:
        entries = f.readlines()
    for e in entries:
        info = e.split('/')
        try:
            user = User.objects.get(username=info[5].split('@')[0])
            user.first_name = info[0]
            user.last_name = info[1]
            user.email = info[5]
            prof = Profile.objects.get_or_create(user=user)[0]
            prof.year = info[2]
            if prof.year == "2015":
                prof.delete()
                user.delete()
                continue
            prof.position = info[3]
            prof.duke_email = info[4]
            prof.phone_number = info[6]
            prof.home_street = info[7]
            prof.home_town = info[8]
            prof.save()
            user.save()
        except Exception as ex:
            print "Error updating user with entry %s: %s" %(e, ex)
