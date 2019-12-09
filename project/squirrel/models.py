from django.db import models
from django.utils.translation import gettext as _

class Squirrel(models.Model):
    Longitude = models.FloatField(
        blank=True,
        help_text=_('Longitude coordinate for squirrel sighting point'),
    )

    Latitude = models.FloatField(
        blank=True,
        help_text=_('Latitude  coordinate for squirrel sighting point'),
    )

    Unique_Squirrel_ID = models.CharField(
        blank=True,
        max_length=100,
        help_text=_('Identification tag for each squirrel sightings'),
    )

    NONE = ''

    AM = 'AM'
    PM = 'PM'

    SHIFT_CHOICE = (
        (NONE, ''),
        (AM, 'AM'),
        (PM, 'PM'),
    )

    Shift = models.CharField(
        blank=True,
        max_length=16,
        choices=SHIFT_CHOICE,
        help_text=_('Whether the sighting session occured in the morning or late afternoon'),
        default=NONE,
    )
    
    Date = models.CharField(
        blank=True,
        max_length=100,
        help_text=_('Concatenation of the sighting session day and month'),
    )

    Adult = 'Adult'
    Juvenile = 'Juvenile'

    AGE_CHOICE = (
        (NONE, ''),
        (Adult, 'Adult'),
        (Juvenile, 'Juvenile'),
    )

    Age = models.CharField(
        blank=True,
        max_length=100,
        choices=AGE_CHOICE,
        default=NONE,
    )
    
    Gray = 'Gray'
    Cinnamon = 'Cinnamon'
    Black = 'Black'

    FUR_COLOR_CHOICE = (
        (NONE, ''),
        (Gray, 'Gray'),
        (Cinnamon, 'Cinnamon'),
        (Black, 'Black'),
    )

    Primary_Fur_Color = models.CharField(
        blank=True,
        max_length=100,
        choices=FUR_COLOR_CHOICE,
        default=NONE,
    )
    
    Plane = 'Ground Plane'
    Above = 'Above Ground'

    LOCATION_CHOICE = (
        (NONE, ''),
        (Plane, 'Ground plane'),
        (Above, 'Above ground'),
    )
    
    Location = models.CharField(
        blank=True,
        max_length=100,
        choices=LOCATION_CHOICE,
        default=NONE,
        help_text=_('the location of where the squirrel was when first sighted'),
    )
    
    Specific_Location = models.CharField(
        blank=True,
        max_length=100,
        help_text=_("Sighters' commentary on the squirrel location"),
    )
    
    Running = models.BooleanField(
        help_text=_('Whether squirrel was seen running'),
    )
    
    Chasing = models.BooleanField(
        help_text=_('Whether squirrel was seen chasing another squirrel'),
    )

    Climbing = models.BooleanField(
        help_text=_('Whether squirrel was seen climbing a tree or other environmental landmark'),
    )

    Eating = models.BooleanField(
        help_text=_('Whether squirrel was seen eating'),
    )

    Foraging = models.BooleanField(
        help_text=_('Whether squirrel was seen foraging for food'),
    )

    Other_Activities = models.CharField(
        blank=True,
        max_length=100,
    )
    
    Kuks = models.BooleanField(
        help_text=_('Whether squirrel was heard kukking'),
    )
    
    Quaas = models.BooleanField(
        help_text=_('Whether squirrel was heard quaaing'),
    )

    Moans = models.BooleanField(
        help_text=_('Whether squirrel was heard moaning'),
    )

    Tail_flags = models.BooleanField(
        help_text=_('Whether squirrel was seen flagging its tail'),
    )

    Tail_twitches = models.BooleanField(
        help_text=_('Whether squirrel was seen twitching its tail'),
    )

    Approaches = models.BooleanField(
        help_text=_('Whether squirrel was seen approaching human, seeking food'),
    )

    Indifferent = models.BooleanField(
        help_text=_('Whether squirrel was indifferent to human presence'),
    )

    Runs_from = models.BooleanField(
        help_text=_('Whether squirrel was seen running from humans, seeing them as a threat'),
    )

