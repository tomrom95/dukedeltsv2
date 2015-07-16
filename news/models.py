from django.db import models
import markdown
from markupfield.fields import MarkupField

class Story(models.Model):
    title = models.CharField(max_length=200)
    body_markdown = models.TextField('Entry body', help_text='Use Markdown syntax.')
    body = models.TextField('Entry body as HTML', blank=True, null=True)
    image = models.ImageField()
    pub_date = models.DateTimeField('date published')

    class Admin:
        fields = (
            (None, {'fields': ('title', 'pub_date', 'body_markdown', 'image')}),
            )

    def save(self):
        import markdown
        self.body = markdown.markdown(self.body_markdown)
        super(Story, self).save()

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name_plural = "stories"
        ordering = ('-pub_date',)