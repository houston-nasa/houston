from rest_framework import serializers
from .models import GithubCred, GithubToken, HoustonUser

class GithubTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = GithubToken
        fields = ['owner', 'token']

class GithubCredSerializer(serializers.ModelSerializer):
    class Meta:
        model = GithubCred
        fields = ['id', 'name', 'desc', 'token', 'owner', 'repo']

class HoustonUserSerializer(serializers.ModelSerializer):
    github_creds = GithubCredSerializer(source='githubcred_set', many=True, read_only=True)  # Nested serializer for GithubCred

    class Meta:
        model = HoustonUser
        fields = ['id', 'first_name', 'last_name', 'email', 'github_creds']  # Include GitHub tokens in the response
