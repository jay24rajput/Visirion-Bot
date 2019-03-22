import hmac
import json
import re
from hashlib import sha1

from django.conf import settings
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseServerError
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.encoding import force_bytes

import requests
from ipaddress import ip_address, ip_network
flag=0
ACCESS_TOKEN=''

@csrf_exempt
def hello(request):
    global flag
    # Verify if request came from GitHub
    forwarded_for = u'{}'.format(request.META.get('HTTP_X_FORWARDED_FOR'))
    client_ip_address = ip_address(forwarded_for)
    whitelist = requests.get('https://api.github.com/meta').json()['hooks']

    for valid_ip in whitelist:
        if client_ip_address in ip_network(valid_ip):
            break
    else:
        return HttpResponseForbidden('Permission denied.')

    # Verify the request signature
    header_signature = request.META.get('HTTP_X_HUB_SIGNATURE')
    if header_signature is None:
        return HttpResponseForbidden('Permission denied.')

    #verifing signatures

    sha_name, signature = header_signature.split('=')
    if sha_name != 'sha1':
        return HttpResponseServerError('Operation not supported.', status=501)

    mac = hmac.new(force_bytes(settings.GITHUB_WEBHOOK_KEY), msg=force_bytes(request.body), digestmod=sha1)
    if not hmac.compare_digest(force_bytes(mac.hexdigest()), force_bytes(signature)):
        return HttpResponseForbidden('Permission denied.')


    #Fetching comments body
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    # print(body)

    #Fetching comments url

    pull_request_url= body['issue']['pull_request']['url']
    request_branch_data = requests.get(url = pull_request_url,params=None)
    request_branch_data=request_branch_data.json()
    
    #---------Head Branch---------------#
    head_branch=request_branch_data['head']['ref']
    
    head_url = request_branch_data['head']['repo']['html_url']
    base_url = request_branch_data['base']['repo']['html_url']

    #fetching the forked repo name from the head url
    head_repository_name=head_url.split('/')[-1]
    print(head_repository_name)
   
    comments_url = body['issue']['comments_url']

    # print(comments_url)

    
    request_data = requests.get(url = comments_url,params=None)

    #Fetching comments json
    comment_json= request_data.json()

    #Fetching comment contents
    comments_list=[]
    for key in comment_json:
        comments_list.append(key['body'])


    pattern='@visirion ([a-z]*)$'
    lastComment=comments_list[-1]
    ans=re.match(pattern,lastComment)
    print(lastComment)
    if ans!= None:
        temp=makeComment(comments_url)
    
    # temp=makeComment()


    #print success if no error occurs
    return HttpResponse("success")


def makeComment(github_url):
    headers = {'Authorization': 'token ' + ACCESS_TOKEN}
    data = json.dumps({'body':'Rebase is in progress. Kindly do not push changes while rebase is being performed :warning:'})
    r = requests.post(github_url, data=data,headers=headers)
    return ""
