from rest_framework import serializers
from .models import GithubCred, GithubToken, HoustonUser

class GithubTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = GithubToken
        fields = ['owner', 'token']

class GithubCredSerializer(serializers.ModelSerializer):
    pk = serializers.SerializerMethodField()

    class Meta:
        model = GithubCred
        fields = ['pk', 'name', 'desc', 'token', 'owner', 'repo']

    # Define a method to compute the value for the static field
    def get_pk(self, obj):
        return str(obj.id)

class HoustonUserSerializer(serializers.ModelSerializer):
    # github_creds = GithubCredSerializer(source='githubcred_set', many=True, read_only=True)  # Nested serializer for GithubCred

    class Meta:
        model = HoustonUser
        fields = ['id', 'first_name', 'last_name', 'email']  # Include GitHub tokens in the response
