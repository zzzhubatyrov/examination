from typing import Optional
from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):

    use_in_migrations = True

    def _create_user(
        self,
        first_name: str,
        middle_name: str,
        last_name: str,
        username: str,
        password: str,
        email: Optional[str] = None,
        office_phone: Optional[int] = None,
        mobile_phone: Optional[str] = None,
        telegram: Optional[str] = None,
        department: Optional[int] = None,
        **kwargs
    ):
        """
        Creates and saves a User with given details
        """
        email = self.normalize_email(email)
        user = self.model(first_name=first_name, middle_name=middle_name, last_name=last_name, 
            username=username, email=email, office_phone=office_phone, mobile_phone=mobile_phone,
            telegram=telegram, department=department, **kwargs
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(
        self,
        first_name: str,
        middle_name: str,
        last_name: str,
        username: str,
        password: str,
        email: Optional[str] = None,
        office_phone: Optional[int] = None,
        mobile_phone: Optional[str] = None,
        telegram: Optional[str] = None,
        department: Optional[int] = None,
        **kwargs
    ):
        """
        Creates a normal user considering the specified user settings
        from Django Project's settings.py

        Parameters
        ----------
        username: str
        email: str
        password: str
        name: str
        mobile: str, optional
        kwargs

        Returns
        -------
        User Instance
        """
        kwargs.setdefault("is_superuser", False)
        kwargs.setdefault("is_staff", False)
        kwargs.setdefault("is_active", True)

        return self._create_user(first_name, middle_name, last_name,
                                 username, password, email, office_phone, mobile_phone,
                                 telegram, department, **kwargs)

    def create_superuser(
        self,
        first_name: str,
        middle_name: str,
        last_name: str,
        username: str,
        password: str,
        email: Optional[str] = None,
        office_phone: Optional[int] = None,
        mobile_phone: Optional[str] = None,
        telegram: Optional[str] = None,
        department: Optional[int] = None,
        **kwargs
    ):
        """
        Creates a super user considering the specified user settings
        from Django Project's settings.py
        Parameters
        ----------
        username: str
        email: str
        password: str
        name: str
        mobile: str, optional
        kwargs

        Returns
        -------
        User Instance
        """

        kwargs.setdefault("is_superuser", True)
        kwargs.setdefault("is_staff", True)
        kwargs.setdefault("is_active", True)

        if kwargs.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        if kwargs.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")

        return self._create_user(first_name, middle_name, last_name,
                                 username, password, email, office_phone, mobile_phone,
                                 telegram, department, **kwargs)
