from django.db import models

class Project(models.Model):
    CATEGORY_CHOICES = [
        ('RES', 'Residential Rooftop'),
        ('COM', 'Commercial Setup'),
        ('MW', 'Megawatt Scale / Industrial'),
    ]
    
    title = models.CharField(max_length=200)
    location = models.CharField(max_length=100, help_text="e.g., Coimbatore, Tamil Nadu")
    category = models.CharField(max_length=3, choices=CATEGORY_CHOICES, default='RES')
    capacity_kw = models.DecimalField(max_digits=10, decimal_places=2, help_text="Capacity in kW or MW")
    description = models.TextField()
    image = models.ImageField(upload_to='projects/images/', blank=True, null=True)
    video_url = models.URLField(blank=True, null=True, help_text="YouTube/Vimeo embed link for drone footage")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.location}"

class Lead(models.Model):
    SCALE_CHOICES = [
        ('RES', 'Residential Rooftop (<10 kW)'),
        ('COM', 'Commercial Roof (10 kW - 100 kW)'),
        ('MW', 'Megawatt / Industrial Utility Scale (>100 kW)'),
    ]
    FINANCE_CHOICES = [
        ('LOAN', 'Loans Only'),
        ('SUBSIDY', 'Subsidy Assistance Only'),
        ('BOTH', 'Both Loans & Subsidies'),
        ('NONE', 'Self-Funded'),
    ]

    name = models.CharField(max_length=150)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    location = models.CharField(max_length=100)
    monthly_bill = models.DecimalField(max_digits=10, decimal_places=2)
    project_scale = models.CharField(max_length=3, choices=SCALE_CHOICES)
    financial_assistance = models.CharField(max_length=8, choices=FINANCE_CHOICES)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Inquiry from {self.name}"