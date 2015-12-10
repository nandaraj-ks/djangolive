from django.test import TestCase
from web.models import Animal, Task

class AnimalTestCase(TestCase):

    def test_animals_can_speak(self):
        """Animals that can speak are correctly identified"""
        Animal.objects.create(name="lion", sound="roar")
        Animal.objects.create(name="cat", sound="meow")
        lion = Animal.objects.get(name="lion")
        cat = Animal.objects.get(name="cat")
        self.assertEqual(lion.speak(), 'The lion says "roar"')
        self.assertEqual(cat.speak(), 'The cat says "meow"')

class TaskTestCase(TestCase):

    def test_initial_status(self):
        print "testttttt"
        new_task = Task.objects.create(name="Django Test")
        self.assertEqual(new_task.is_completed, False)