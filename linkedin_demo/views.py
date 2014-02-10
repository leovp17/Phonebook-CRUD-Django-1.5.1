from django.http import HttpResponse
from linkedin.linkedin import PERMISSIONS, LinkedInApplication, LinkedInAuthentication
from django.shortcuts import render_to_response
import oauth2 as oauth
import json

def test1(request):
    API_KEY = "75b6nt9kewzh8f"
    API_SECRET = "xdhRsXeOAAi9tXB3"
    RETURN_URL = "http://127.0.0.1:8000/linkedin/response1"
    authentication = LinkedInAuthentication(API_KEY,API_SECRET,RETURN_URL,PERMISSIONS.enums.values())
    response = "<h1>Request Access to my own linkedin profile</h1>"
    response += '<a href="'+authentication.authorization_url+'">URL</a>'
    return HttpResponse(response)

def response1(request):
    code = request.GET['code']
    API_KEY = "75b6nt9kewzh8f"
    API_SECRET = "xdhRsXeOAAi9tXB3"
    RETURN_URL = "http://127.0.0.1:8000/linkedin/response1"
    authentication = LinkedInAuthentication(API_KEY,API_SECRET,RETURN_URL,PERMISSIONS.enums.values())
    authentication.authorization_code = code
    authentication.get_access_token()
    application = LinkedInApplication(authentication)

    profile = application.get_profile(selectors=['id', 'first-name', 'last-name','headline', 'location', 'distance', 'num-connections', 'skills', 'educations'])

    connections = application.get_connections()

    return render_to_response('linkedin/profile.html',{'profile':profile, 'connections':connections})


def test2(request, slug):
    API_KEY = "75b6nt9kewzh8f"
    API_SECRET = "xdhRsXeOAAi9tXB3"
    OAUTH_USER_TOKEN = "309c6843-5883-41b9-892e-02b80a831807"
    OAUTH_SECRET_TOKEN = "baf2a63c-7050-4bf7-80c4-01b383ff52c4"

    consumer = oauth.Consumer(API_KEY,API_SECRET)

    access_token = oauth.Token(key=OAUTH_USER_TOKEN,secret=OAUTH_SECRET_TOKEN)

    client = oauth.Client(consumer,access_token)
    candidado_linkedin_prefix = "http%3A%2F%2Fwww.linkedin.com%2Fin%2F"
    linkedin_url = candidado_linkedin_prefix + slug

    resp,content = client.request("http://api.linkedin.com/v1/people/url="+linkedin_url+":(first-name,last-name,headline,picture-url,siteStandardProfileRequest)/?format=json","GET", "")

    return HttpResponse(content, content_type="application/json")


