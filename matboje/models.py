from django.db import models
from django.forms import ModelForm
from competitors.models import Competitor
from django.forms.widgets import CheckboxSelectMultiple


class Matboj(models.Model):
    name = models.CharField(max_length=100, unique=True, null=False)
    date = models.DateTimeField('date played')
    competitors = models.ManyToManyField(Competitor, through='MatbojCompetitors')
    default_rank = models.IntegerField(default = 1000)
    
    def __str__(self):
        return "{}".format(self.name)

# I wouldn't call this in plural, one instance of this class refers to one Competitor
class MatbojCompetitors(models.Model):
    competitor = models.ForeignKey(Competitor, on_delete=models.CASCADE)
    matboj = models.ForeignKey(Matboj, on_delete=models.CASCADE)
    ranking = models.IntegerField(default=1000)
    
    def __str__(self):
        return "{}".format(str(self.competitor))

    class Meta:
        # Order decreasingly by the ranking
        ordering = ['competitor']    
        auto_created = True
        
class MatbojAdminForm(ModelForm):  
      
    class Meta:  
        model = Matboj  
        fields = ("competitors",)  
               
    def __init__(self, *args, **kwargs):  
          
        super(CompanyForm, self).__init__(*args, **kwargs)  
          
        self.fields["competitors"].widget = CheckboxSelectMultiple()  
        self.fields["competitors"].queryset = Competitor.objects.all()  
