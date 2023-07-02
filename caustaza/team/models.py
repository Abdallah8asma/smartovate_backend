from django.db import models


class TeamMember(models.Model):
    id = models.BigAutoField(primary_key=True)
    image = models.ImageField(upload_to='images/team',blank=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    designation = models.CharField(max_length=250, blank=True, null=True)
    location = models.CharField(max_length=30, blank=True, null=True)
    description = models.CharField(
        max_length=250, blank=True, null=True
    )  # Material Icon name



    class Meta:
        managed = True
        db_table = 'team_member'

    def __str__(self):
        return self.name


class Team(models.Model):
    id = models.BigAutoField(primary_key=True)
    teammember = models.ManyToManyField(
        TeamMember,
    )
    subtitle = models.CharField(max_length=250, blank=True, null=True)
    title = models.CharField(max_length=30, blank=True, null=True)
    description = models.CharField(max_length=250, blank=True, null=True)
    

    class Meta:
        managed = True
        db_table = 'team'

    def __str__(self):
        return self.title
