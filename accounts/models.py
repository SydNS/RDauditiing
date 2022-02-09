from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,User




# Create your models here.
# Create a user

class MyAccountManager(BaseUserManager):
    def create_user(self,email,username,password=None):
        if not email:
            raise ValueError("Users must have an email")
        if not username:
            raise ValueError("Users must have an email")
        user=self.model(
            email=self.normalize_email(email),
            username=username,
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self,email,username,password=None):

        user=self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password
        )
        user.is_admin=True
        user.is_staff=True
        user.is_superuser=True

        user.set_password(password)
        user.save(using=self.db)
        return user



class Account(AbstractBaseUser):
    email   =models.EmailField(verbose_name="email",max_length=60,unique=True)
    username   =models.CharField(max_length=30,unique=True)
    date_joined   =models.DateTimeField(verbose_name="date_joined",auto_now_add=True)
    last_login   =models.DateTimeField(verbose_name="last_login",auto_now=True)
    is_admin   =models.BooleanField(default=False)
    is_active    =models.BooleanField(default=True)
    is_staff   =models.BooleanField(default=False)
    is_superuser   =models.BooleanField(default=False)
    hide_email=models.BooleanField(default=True)
    # profileimage=models.ImageField(max_length=255,upload_to=,null=True,default=)

    objects=MyAccountManager()

    USERNAME_FIELD="email"
    REQUIRED_FIELDS=["email"]

    def __str__(self):
        return self.username

    def has_perm(self,perm,obj=None):
        return self.username

    def has_module_perms(self,app_label):
        return True


class Department(models.Model):
    CRITICALITY_LEVELS = (
        ('low', 'low'),
        ('medium', 'medium'),
        ('high', 'high'),
    )
    departmenttname = models.CharField(max_length=100)
    departmentrole = models.CharField(max_length=100)
    numberofmembers = models.IntegerField()
    criticality = models.CharField(db_column='Criticality', max_length=20, blank=False, null=True,
                                   choices=CRITICALITY_LEVELS, default='draft')  # Field name made lowercase.
    def __str__(self):
        return self.deptname


    # class Meta:
    #     unique_together = ("deptname", "deptrole",)


class Person(models.Model):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female')
    ]
    name_user = models.ForeignKey(User, on_delete=models.CASCADE)
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='profileimages/')
    gender = models.CharField(choices=GENDER_CHOICES, default='male', max_length=6)
    address = models.CharField(max_length=100)
    personsdept = models.ForeignKey(Dept, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "People"

    def __str__(self):
        return self.last_name


class RatingUser(models.Model):
    RATINGS = (
        ('1', '1/10'),
        ('2', '2/10'),
        ('3', '3/10'),
        ('4', '4/10'),
        ('5', '5/10'),
        ('6', '6/10'),
        ('7', '7/10'),
        ('8', '8/10'),
        ('9', '9/10'),
        ('10', '10/10'),
    )
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    rate_levels = models.PositiveSmallIntegerField()
    deptnem = models.ForeignKey(Dept, on_delete=models.CASCADE)

    def __str__(self):
        return self.grade
