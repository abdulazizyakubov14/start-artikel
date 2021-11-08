from django.db import models

# Create your models here.
# from parler.models import TranslatableModel, TranslatedFields
from django.urls import reverse
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.


class Categorys(models.Model):
    name = models.CharField('Категория имя',max_length=150)
    slug = models.SlugField('*',max_length=150, unique=True)
    img = models.ImageField("Категория Фото", upload_to='cat_imgs',)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse('main:category_detail', kwargs={'category_slug':self.slug})

class Articles(models.Model):
    title = models.TextField("Название статьи")
    subtitle = RichTextField()
    slug = models.SlugField("*")
    category = models.ForeignKey(Categorys, related_name='categoryies' ,on_delete=models.CASCADE)
    author = models.CharField("Статья Афтори", max_length=50)
    date = models.DateField("Дата Отправки", auto_now=True,)
    # post_views = models.IntegerField(default=0, null=True, blank=True)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'


    def __str__(self):
        return self.title
