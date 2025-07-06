from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
import json


class ProfileRegistrationViewTest(APITestCase):
    def setUp(self):
        self.url = reverse('profile-registration')
        self.valid_data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'ComplexPassword123!',
            'password_confirm': 'ComplexPassword123!',
            'first_name': 'Test',
            'last_name': 'User'
        }
    
    def test_improved_behavior_detailed_error_for_existing_email(self):
        """Test that improved implementation returns detailed error for existing email"""
        # Create a user with the same email first
        User.objects.create_user(
            username='existing', 
            email='test@example.com', 
            password='ExistingPassword123!'
        )
        
        response = self.client.post(self.url, self.valid_data, format='json')
        
        # Improved implementation should return field-level validation errors
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('email', response.data)
        self.assertEqual(response.data['email'], ['A user with this email already exists.'])
        # Should NOT return generic error message
        self.assertNotEqual(response.data, {"error": "Invalid request data"})
    
    def test_improved_behavior_detailed_error_for_password_mismatch(self):
        """Test that improved implementation returns detailed error for password mismatch"""
        data = self.valid_data.copy()
        data['password_confirm'] = 'DifferentPassword123!'
        
        response = self.client.post(self.url, data, format='json')
        
        # Improved implementation should return field-level validation errors
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('password_confirm', response.data)
        self.assertEqual(response.data['password_confirm'], ['Passwords do not match.'])
        # Should NOT return generic error message
        self.assertNotEqual(response.data, {"error": "Invalid request data"})
    
    def test_successful_registration(self):
        """Test successful user registration"""
        response = self.client.post(self.url, self.valid_data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('message', response.data)
        self.assertIn('user_id', response.data)
        
        # Verify user was created
        user = User.objects.get(username='testuser')
        self.assertEqual(user.email, 'test@example.com')
    
    def test_multiple_validation_errors(self):
        """Test that field-level validation errors are returned even when some fail"""
        # Create a user with the same email first
        User.objects.create_user(
            username='existing', 
            email='test@example.com', 
            password='ExistingPassword123!'
        )
        
        data = {
            'username': 'testuser',
            'email': 'test@example.com',  # Existing email - this will fail field validation
            'password': 'ComplexPassword123!',
            'password_confirm': 'DifferentPassword123!',  # This won't be checked because email fails first
            'first_name': 'Test',
            'last_name': 'User'
        }
        
        response = self.client.post(self.url, data, format='json')
        
        # Should return the email validation error
        # Note: password_confirm validation doesn't run because email validation fails first
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('email', response.data)
        self.assertEqual(response.data['email'], ['A user with this email already exists.'])
    
    def test_password_mismatch_when_other_fields_valid(self):
        """Test password mismatch validation when other fields are valid"""
        data = {
            'username': 'testuser',
            'email': 'newemail@example.com',  # Valid email
            'password': 'ComplexPassword123!',
            'password_confirm': 'DifferentPassword123!',  # Mismatched password
            'first_name': 'Test',
            'last_name': 'User'
        }
        
        response = self.client.post(self.url, data, format='json')
        
        # Should return password confirmation error
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('password_confirm', response.data)
        self.assertEqual(response.data['password_confirm'], ['Passwords do not match.'])
    
    def test_required_field_errors(self):
        """Test that required field validation errors are detailed"""
        data = {}  # Empty data to trigger required field errors
        
        response = self.client.post(self.url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        # Should return specific required field errors
        self.assertIn('username', response.data)
        self.assertIn('email', response.data)
        self.assertIn('password', response.data)
        self.assertIn('password_confirm', response.data)
