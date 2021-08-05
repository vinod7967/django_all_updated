from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.db.models.signals import post_save, pre_save
from django.contrib.auth.models import User
from django.dispatch import receiver
# from .models import TicketBookModel

@receiver(user_logged_in, sender = User)
def login_success(sender, request, user, **kwargs):
    print('Logged in Signal..')
    print('User:', user)
    print('User Pass:', user.password)
# user_logged_in.connect(login_success, sender=User)

@receiver(user_logged_out, sender = User)
def logout_success(sender, request, user, **kwargs):
    print('Logged out Signal..')
    print('User:', user)
    print('User Pass:', user.password)
# user_logged_out.connect(logout_success, sender=User)

@receiver(user_login_failed, sender = User)
def login_failed(sender, credentials, request, **kwargs):
    print('Logged fail Signal..')
    print('credentials:', credentials)
# user_login_failed.connect(login_failed, sender=User)


@receiver(pre_save, sender = User)
def data_save(sender, instance, **kwargs):
    print('Data Save Signal..')
    print('instance:', instance)
# pre_save.connect(data_save, sender=User)
