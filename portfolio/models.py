from django.db import models


class Paintings(models.Model):
    image = models.ImageField(upload_to='images/paintings_img/')
    title = models.CharField(max_length=50, blank=True)
    create_date = models.DateField('date published')
    description = models.CharField(max_length=200, blank=True)
    details = models.CharField(max_length=50, blank=True)


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published', null=True)

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


class Comment(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.name, self.created)
