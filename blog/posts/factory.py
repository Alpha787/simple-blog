import factory
from django.contrib.auth.models import User
from factory.faker import faker

from .models import Post

FAKE = faker.Faker()

class PostFactory(factory.django.DjangoModelFactory):
  class Meta:
    model = Post 
    
  title = factory.Faker("sentence", nb_words=12)
  # text = factory.Faker("sentence", nb_works=25) 
  author = User.objects.get_or_create(username="admin")[0]
  # created_date = factory.Faker()
  
  @factory.lazy_attribute
  def text(self):
    x = ""
    for _ in range(0, 5):
      x += "\n" + FAKE.paragraph(nb_sentences=30) + "\n"
    return x 

  # status = "published"
