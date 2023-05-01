# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'category'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Food(models.Model):
    name = models.CharField(max_length=255)
    name_scientific = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'food'


class Ingredient(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    category = models.ForeignKey(Category, models.DO_NOTHING, blank=True, null=True)
    selected = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ingredient'


class MyFood(models.Model):
    user_input = models.CharField(max_length=255)
    fk_ingredient = models.ForeignKey(Ingredient, models.DO_NOTHING, blank=True, null=True)
    selected = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'my_food'


class Nutrition(models.Model):
    recipe = models.ForeignKey('Recipe', models.DO_NOTHING, blank=True, null=True)
    calories_amount = models.FloatField(blank=True, null=True)
    calories_unit = models.ForeignKey('Unit', models.DO_NOTHING, blank=True, null=True)
    carbohydrates_amount = models.FloatField(blank=True, null=True)
    carbohydrates_unit = models.ForeignKey('Unit', models.DO_NOTHING, related_name='nutrition_carbohydrates_unit_set', blank=True, null=True)
    protein_amount = models.FloatField(blank=True, null=True)
    protein_unit = models.ForeignKey('Unit', models.DO_NOTHING, related_name='nutrition_protein_unit_set', blank=True, null=True)
    fat_amount = models.FloatField(blank=True, null=True)
    fat_unit = models.ForeignKey('Unit', models.DO_NOTHING, related_name='nutrition_fat_unit_set', blank=True, null=True)
    saturated_fat_amount = models.FloatField(blank=True, null=True)
    saturated_fat_unit = models.ForeignKey('Unit', models.DO_NOTHING, related_name='nutrition_saturated_fat_unit_set', blank=True, null=True)
    polyunsaturated_fat_amount = models.FloatField(blank=True, null=True)
    polyunsaturated_fat_unit = models.ForeignKey('Unit', models.DO_NOTHING, related_name='nutrition_polyunsaturated_fat_unit_set', blank=True, null=True)
    monounsaturated_fat_amount = models.FloatField(blank=True, null=True)
    monounsaturated_fat_unit = models.ForeignKey('Unit', models.DO_NOTHING, related_name='nutrition_monounsaturated_fat_unit_set', blank=True, null=True)
    trans_fat_amount = models.FloatField(blank=True, null=True)
    trans_fat_unit = models.ForeignKey('Unit', models.DO_NOTHING, related_name='nutrition_trans_fat_unit_set', blank=True, null=True)
    cholesterol_amount = models.FloatField(blank=True, null=True)
    cholesterol_unit = models.ForeignKey('Unit', models.DO_NOTHING, related_name='nutrition_cholesterol_unit_set', blank=True, null=True)
    sodium_amount = models.FloatField(blank=True, null=True)
    sodium_unit = models.ForeignKey('Unit', models.DO_NOTHING, related_name='nutrition_sodium_unit_set', blank=True, null=True)
    potassium_amount = models.FloatField(blank=True, null=True)
    potassium_unit = models.ForeignKey('Unit', models.DO_NOTHING, related_name='nutrition_potassium_unit_set', blank=True, null=True)
    fiber_amount = models.FloatField(blank=True, null=True)
    fiber_unit = models.ForeignKey('Unit', models.DO_NOTHING, related_name='nutrition_fiber_unit_set', blank=True, null=True)
    sugar_amount = models.FloatField(blank=True, null=True)
    sugar_unit = models.ForeignKey('Unit', models.DO_NOTHING, related_name='nutrition_sugar_unit_set', blank=True, null=True)
    vitamin_a_amount = models.FloatField(blank=True, null=True)
    vitamin_a_unit = models.ForeignKey('Unit', models.DO_NOTHING, related_name='nutrition_vitamin_a_unit_set', blank=True, null=True)
    vitamin_c_amount = models.FloatField(blank=True, null=True)
    vitamin_c_unit = models.ForeignKey('Unit', models.DO_NOTHING, related_name='nutrition_vitamin_c_unit_set', blank=True, null=True)
    calcium_amount = models.FloatField(blank=True, null=True)
    calcium_unit = models.ForeignKey('Unit', models.DO_NOTHING, related_name='nutrition_calcium_unit_set', blank=True, null=True)
    iron_amount = models.FloatField(blank=True, null=True)
    iron_unit = models.ForeignKey('Unit', models.DO_NOTHING, related_name='nutrition_iron_unit_set', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nutrition'


class Recipe(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    url = models.CharField(unique=True, max_length=500, blank=True, null=True)
    data = models.TextField(blank=True, null=True)
    cuisine = models.CharField(max_length=255, blank=True, null=True)
    servings = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'recipe'


class Recipes(models.Model):
    recipe = models.ForeignKey(Recipe, models.DO_NOTHING)
    amount = models.FloatField(blank=True, null=True)
    unit = models.ForeignKey('Unit', models.DO_NOTHING, blank=True, null=True)
    ingredient = models.ForeignKey(Ingredient, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'recipes'


class Unit(models.Model):
    type = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'unit'
