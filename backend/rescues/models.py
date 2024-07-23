from django.db import models

# Create your models here.

# all in the scope of making a perfinder website
# will have to populate more breeds
# for frontend..dont see your breed. click other..ya'know

class Rescue(models.Model):
    name = models.CharField(max_length=45)
    description = models.TextField()

class breed(models.Model):
    pass

# class breed, age, 


# looking at petfinder the categories are
# dog, cat, rabbits, small & furry, scales, fins, & other, birds , horses, barnyard
# probably will have to go deeper with a filter for each of these
# categories

# small and furry: guinea pig, rat, gerbil, dwarf Hamster
# so filter it to size of animal
class Category(models.Model):
    pass


