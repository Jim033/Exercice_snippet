from wagtail.models import Page
from django.db import models
from wagtail.admin.panels import FieldPanel
from wagtail.snippets.models import register_snippet


class CoachPage(Page):
    photo = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+"
    )
    content_panels = Page.content_panels + [
        FieldPanel("photo")
    ]

@register_snippet #Je déclare mon DECORATEUR snippet
class Cours(models.Model):
    nom = models.CharField(max_length=100, blank=True)
    horaire = models.CharField(max_length=100, blank=True)
    niveau = models.CharField(max_length=100, blank=True)
    description = models.TextField(max_length=255, blank=True)

    panels = [
        FieldPanel("nom"),
        FieldPanel("horaire"),
        FieldPanel("niveau"),
        FieldPanel("description")
    ]

    def __str__(self):
        return self.nom

class CoursPage(Page):
    def get_context(self, request):
        context = super().get_context(request)
        context["cours_list"] = Cours.objects.all()
        return context
        


class ContactPage(Page):
    pass
