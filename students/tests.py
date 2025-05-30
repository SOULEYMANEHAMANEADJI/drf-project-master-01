from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from students.models import Student


# Create your tests here.


class StudentModelTest(TestCase):

    def setUp(self):
        # Création d'un étudiant pour les tests
        self.student = Student.objects.create(
            name = 'Monitor',
            branch = 'Science',
        )

    def test_student_creation(self):
        # Vérifie si l'étudiant est bien créé
        student = self.student
        self.assertEqual(student.name, 'Monitor')
        self.assertEqual(student.branch, 'Science')
        self.assertIsInstance(student, Student)

    def test_string_representation(self):
        # Vérifie si la méthode __str__ de l'objet renvoie le bon nom
        self.assertEqual(str(self.student), 'Monitor')


class StudentViewsTest(APITestCase):

    def setUp(self):
        # Création d'un étudiant pour les tests
        self.student = Student.objects.create(name='John Doe', branch='Science')
        self.url = reverse('students-list')  # URL pour les requêtes GET et POST

    def test_get_students(self):
        # Test de la requête GET (récupérer tous les étudiants)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], 'John Doe')

    def test_create_student(self):
        # Test de la requête POST (créer un étudiant)
        data = {'name': 'Jane Doe', 'branch': 'Mathematics'}
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], 'Jane Doe')
        self.assertEqual(response.data['branch'], 'Mathematics')

    def test_update_student(self):
        # Test de la requête PUT (mettre à jour un étudiant)
        url = reverse('student-detail', args=[self.student.pk])
        data = {'name': 'John Doe Updated', 'branch': 'Engineering'}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'John Doe Updated')
        self.assertEqual(response.data['branch'], 'Engineering')

    def test_delete_student(self):
        # Test de la requête DELETE (supprimer un étudiant)
        url = reverse('student-detail', args=[self.student.pk])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        # Vérifier que l'étudiant a bien été supprimé
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)