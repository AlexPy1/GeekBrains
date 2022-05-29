import re
email = 'sa_sha_gb@gmail.com'
d = 'domain'
u = 'username'
def email_parse(email_address):
    try:
        my_set = {}
        RE_MAIL = re.compile(r'(^\w+[._-]*\w+)\@(\w+\.\w+)')
        my_tup = RE_MAIL.findall(email)
        my_set.setdefault(u,my_tup[0][0])
        my_set.setdefault(d, my_tup[0][1])

        print(my_set)

    except:
        msg = 'wrong email:' + str(email)
        raise ValueError(msg)

email_parse(email)