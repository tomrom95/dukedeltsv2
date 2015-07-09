from .models import BoardMember

order = ['President', 'Internal Vice President',
         'External Vice President', 'Sergeant at Arms',
         'Treasurer', 'Director of Risk Management',
         'Secretary']

def ordered_list():
	memset = BoardMember.objects
	olist = []
	for role in order:
		try:
			olist.append(memset.get(position=role))
		except:
			continue
	return olist	
