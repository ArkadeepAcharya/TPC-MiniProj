from django.db import models

# Create your models here.
class Credits(models.Model):
    specialization = models.CharField(max_length=100,blank=True, null=True)
    batch = models.CharField(max_length=8,blank=True, null=True)
    credits1 = models.IntegerField(blank=True, null=True)
    credits2 = models.IntegerField(blank=True, null=True)
    credits3 = models.IntegerField(blank=True, null=True)
    credits4 = models.IntegerField(blank=True, null=True)
    credits5 = models.IntegerField(blank=True, null=True)
    credits6 = models.IntegerField(blank=True, null=True)
    credits7 = models.IntegerField(blank=True, null=True)
    credits8 = models.IntegerField(blank=True, null=True)
    class Meta:
        unique_together = ('specialization', 'batch')
    def __str__(self):
        return str(self.batch)+" "+str(self.specialization)
    

#company model
class Company(models.Model):
    cid = models.CharField(max_length=100)
    reqCandDet = models.TextField()
    # minQual = models.FloatField(default=7.5)
    marksCriteria = models.TextField()
    salaryPackage = models.TextField()
    mode_of_interview = models.CharField(max_length=50,choices=(
        ('Online_written','Online Written'),
        ('Offline_written','Offline Written'),
        ('Online_interview','Online Interview'),
        ('Offine_interview','Offline Inteview'),
    ))
    time_of_start_iitp = models.TextField()
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    def __str__(self):
        return self.cid
    
#student model
class Student(models.Model):
    roll_no = models.CharField(max_length=8, primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    # batch = models.CharField(max_length=100, blank=True)
    batch=models.ForeignKey(Credits , on_delete=models.CASCADE, related_name='batch_yr', blank=True, null=True)
    # branch = models.CharField(max_length=100, blank=True)
    # specialization=models.ForeignKey(Credits , on_delete=models.CASCADE, related_name='specialization_branch')
    cgpa = models.FloatField(blank=True, null=True)
    areaofInterest = models.TextField(blank=True, null=True)
    m10 = models.FloatField(blank=True,null=True)
    m11 = models.FloatField(blank=True,null=True)
    m12 = models.FloatField(blank=True,null=True)
    msem1 = models.FloatField(blank=True,null=True)
    msem2 = models.FloatField(blank=True,null=True)
    msem3 = models.FloatField(blank=True,null=True)
    msem4 = models.FloatField(blank=True,null=True)
    msem5 = models.FloatField(blank=True,null=True)
    msem6 = models.FloatField(blank=True,null=True)
    msem7 = models.FloatField(blank=True,null=True)
    msem8 = models.FloatField(blank=True,null=True)

    resume = models.FileField(upload_to='resume/', blank=True, null=True)
    def __str__(self):
        return self.name
    
#alumni model
class Alumni(models.Model):
    name = models.CharField(max_length=100)
    rollnumber = models.CharField(max_length=8, primary_key=True)
    # cid = models.CharField(max_length=100)
    cid=models.ForeignKey(Company , on_delete=models.CASCADE)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    batch = models.CharField(max_length=100)
    branch = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    m10 = models.FloatField(blank=True)
    m11 = models.FloatField(blank=True)
    m12 = models.FloatField(blank=True)
    msem1 = models.FloatField(blank=True)
    msem2 = models.FloatField(blank=True)
    msem3 = models.FloatField(blank=True)
    msem4 = models.FloatField(blank=True)
    msem5 = models.FloatField(blank=True)
    msem6 = models.FloatField(blank=True)
    msem7 = models.FloatField(blank=True)
    msem8 = models.FloatField(blank=True)
    def __str__(self):
        return self.name
    
#credits model
# class Credits(models.Model):
#     specialization = models.CharField(max_length=100)
#     batch = models.CharField(max_length=8)
#     credits = models.IntegerField()
#     class Meta:
#         unique_together = ('specialization', 'batch')
#     def __str__(self):
#         return self.credits