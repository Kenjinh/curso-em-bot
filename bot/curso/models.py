from django.db import models


# Create your models here.

class Areas(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'tb_conversation_areas_ctg'


class Languages(models.Model):
    name = models.CharField(max_length=100)
    id_area = models.ForeignKey(Areas, on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'tb_conversation_languages_ctg'


class Level(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'tb_conversation_level_ctg'


class Courses(models.Model):
    name = models.CharField(max_length=100)
    id_level = models.ForeignKey(Level, on_delete=models.CASCADE)
    id_language = models.ForeignKey(Languages, on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'tb_conversation_courses_ctg'


class LinksCourse(models.Model):
    id_course = models.ForeignKey('Courses', on_delete=models.CASCADE)
    id_language = models.ForeignKey(Languages, on_delete=models.CASCADE)
    link = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.link

    class Meta:
        db_table = 'tb_conversation_links_course'
