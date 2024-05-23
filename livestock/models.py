"""Models for the livestock app."""
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse


# manager for livestock
class LivestockManager(models.Manager):
    """Manager for livestock entries."""
    def get_queryset(self) -> models.QuerySet:
        """Return queryset for livestock entries."""
        return super(LivestockManager, self).get_queryset().order_by('-created_at')

# livestock model
class Livestock(models.Model):
    """Model for livestock entries."""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    breed = models.CharField(max_length=100)
    age = models.IntegerField()
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    health_status = models.CharField(max_length=200, blank=True)
    breed_image = models.ImageField(upload_to='breed_img/', blank=True)  

    def __str__(self):
        return f"{self.breed} - {self.gender}"
    

# manager for health records
class HealthRecordManager(models.Manager):
    """Manager for health records."""
    def get_queryset(self) -> models.QuerySet:
        """Return queryset for health records."""
        return super(HealthRecordManager, self).get_queryset().order_by('-created_at')

class HealthRecord(models.Model):
    """Model for health records."""
    livestock = models.ForeignKey(Livestock, on_delete=models.CASCADE)
    symptoms = models.TextField()
    diagnosis = models.TextField()
    treatment = models.TextField()
    vaccination_records = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Health Record for {self.livestock}"



# adding manager
class PublishedManager(models.Manager):
    """Manager for published posts."""
    def get_queryset(self):
        """Return queryset for published posts."""
        return super(PublishedManager, self).get_queryset().filter(status='published')



# post model for blog
class Post(models.Model):
    """
        title: Field for post title.
        slug: Used for URLS.
        author: This field defines many-to-one- relationship.
        body: The bosy of post.
        publish: 
    """


    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_post')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    objects = models.Manager() # The default manager.
    published = PublishedManager() # Our custom manager.
    
    def __str__(self):
        """An object"""
        return f"{self.title} by {self.author}"
    
    def get_absolute_url(self):
        """Return the absolute URL for a post."""
        return reverse('Post:post_detail', args=[self.publish.year, self.publish.month, self.publish.day, self.slug])
