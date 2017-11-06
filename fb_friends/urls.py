"""fb_friends URL Configuration

"""

from django.conf.urls import url, include
from django.contrib import admin
from django.shortcuts import render
from friends.models import UserFriends

def enter(request):
    return render(request, 'enter.html', {})

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^$', enter)
]

from allauth.socialaccount.signals import pre_social_login
from django.dispatch import receiver

@receiver(pre_social_login)
def after_user_signed_up(sender, request, **kwargs):

    user_id = kwargs['sociallogin'].account.user_id
    user_friends = kwargs['sociallogin'].account.extra_data['friends']['data']
    obj_for_user = UserFriends.objects.filter(user_id=user_id)

    for user_friend in user_friends:
        if not obj_for_user.filter(friend_id=int(user_friend['id'])):
            obj = UserFriends(user_id=user_id,
                              friend_id=int(user_friend['id']), friend_name=user_friend['name'])
            obj.save()

