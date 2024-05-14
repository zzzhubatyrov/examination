from typing import Dict
from typing import Optional
from django.http import HttpRequest
from django.utils import timezone
from django.utils.text import gettext_lazy as _
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.utils import datetime_from_epoch
from .models import AuthTransaction
from .models import Custom_User



def get_client_ip(request: HttpRequest) -> Optional[str]:
    """
    Fetches the IP address of a client from Request and
    return in proper format.
    Source: https://stackoverflow.com/a/4581997

    Parameters
    ----------
    request: django.http.HttpRequest

    Returns
    -------
    ip: str or None
    """
    x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
    if x_forwarded_for:
        return x_forwarded_for.split(",")[0]
    else:
        return request.META.get("REMOTE_ADDR")


def check_unique(prop: str, value: str) -> bool:
    """
    This function checks if the value provided is present in Database
    or can be created in DBMS as unique data.
    Parameters
    ----------
    prop: str
        The model property to check for. Can be::
            email
            mobile
            username
    value: str
        The value of the property specified

    Returns
    -------
    bool
        True if the data sent is doesn't exist, False otherwise.
    Examples
    --------
    To check if test@testing.com email address is already present in
    Database
    >>> print(check_unique('email', 'test@testing.com'))
    True
    """
    user = Custom_User.objects.extra(where=[prop + " = '" + value + "'"])
    return user.count() == 0


def login_user(user: Custom_User, request: HttpRequest) -> Dict[str, str]:
    """
    This function is used to login a user. It saves the authentication in
    AuthTransaction model.

    Parameters
    ----------
    user: django.contrib.auth.get_user_model
    request: HttpRequest

    Returns
    -------
    dict:
        Generated JWT tokens for user.
    """
    token: RefreshToken = RefreshToken.for_user(user)

    user.last_login = timezone.now()
    user.save()

    AuthTransaction(
        created_by=user,
        ip_address=get_client_ip(request),
        token=str(token.access_token),
        refresh_token=str(token),
        session=user.get_session_auth_hash(),
        expires_at=datetime_from_epoch(token["exp"]),
    ).save()

    return {
        "refresh_token": str(token),
        "token": str(token.access_token),
        "session": user.get_session_auth_hash(),
    }
