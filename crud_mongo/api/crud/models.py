from django.db import models
from django.utils.text import slugify
import uuid


class Recipes(models.Model):
    recipe_name = models.CharField(max_length=100)
    recipe_category = models.CharField(max_length=100)
    recipe_type = models.CharField(max_length=100)
    recipe_desc = models.CharField(max_length=200)
    recipe_id = models.UUIDField(default=uuid.uuid4, null=True)
    recipe_slug = models.SlugField(null=True)
    created_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_date"]

    def save(self, *args, **kwargs) -> None:
        self.recipe_slug = slugify(self.recipe_name)
        return super(Recipes, self).save(*args, **kwargs)

    def __str__(self):
        return self.recipe_name


class Chef(models.Model):
    chef_name = models.CharField(max_length=100)
    chef_desc = models.CharField(max_length=200)
    chef_rest = models.CharField(max_length=100)
    chef_practice = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-chef_practice"]

    def __str__(self):
        return self.chef_name
