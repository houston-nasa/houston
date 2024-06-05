from rest_framework import serializers
from .models import GithubToken, HoustonUser

class GithubTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = GithubToken
        fields = ['owner', 'token']

class HoustonUserSerializer(serializers.ModelSerializer):
    github_tokens = GithubTokenSerializer(source='githubtoken_set', many=True, read_only=True)  # Nested serializer for GitHub tokens

    class Meta:
        model = HoustonUser
        fields = ['id', 'first_name', 'last_name', 'email', 'github_tokens']  # Include GitHub tokens in the response
