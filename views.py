import json

from django.http import HttpResponse
from django.shortcuts import render_to_response
import requests
import json
import string


# Create your views here.
def index(request):
    return render_to_response('index.html')


def getTopo(request):
    r = requests.get('http://10.0.2.15:8181/restconf/operational/network-topology:network-topology',
                     auth=('admin', 'admin'))
    return HttpResponse(json.dumps(r.json()))
def getflow(request):
    flow = requests.get('http://10.0.2.15:8181/restconf/operational/opendaylight-inventory:nodes',auth=('admin','admin'))
    return HttpResponse(json.dumps(flow.json()))

#def findflow(request):
    #if request.method == "POST":
          #  node_id = request.POST.get('node_id')
           # flow_id = request.POST.get('flow_id')
          #  url = 'http://10.0.2.15:8181/restconf/operational/opendaylight-inventory:nodes/node/' + node_id + '/table/0/flow/' + flow_id
          #  print url
	   # partflow = requests.get(url,auth=('admin','admin'))
	    #partflow = requests.put(url,auth=('admin','admin'),headers={'Content-Type':'application/json'})
           # print partflow
     #headers = {'Content-Type':'application/xml','Accept':'application/xml'}
#     partflow = requests.get('http://10.0.2.15:8181/restconf/operational/opendaylight-inventory:nodes/node/openflow:1/table/0',auth=('admin','admin'),headers = {'Content-Type':'application/json','Accept':'application/json','Authorization':'admin'})
#     return HttpResponse(json.dumps(partflow.json()))
#def flow_update(request):
   # if request.method == "POST":
        #    node_id = request.POST.get('node_id')
          #  flow_id = request.POST.get('flow_id')
#infolo = {"flow":[{"id":0,"instructions": {"instruction":[{"apply-actions":{"action": [{"drop-action": {},"order":0}]},"order":0}]},"priority":11,"table_id":0}]}
def deleteflow(request):
    if request.method == "POST":
        node_id1 = request.POST.get('node_id1')
	table_id1 = request.POST.get('table_id1')
	flow_id1 = request.POST.get('flow_id1')
	url = 'http://10.0.2.15:8181/restconf/config/opendaylight-inventory:nodes/node/'+node_id1+'/flow-node-inventory:table/'+table_id1+'/flow/'+flow_id1
    flow_delete = requests.delete(url,auth=('admin','admin'))
    return HttpResponse(json.dumps(flow_delete.json()))


def putflow(request):
    if request.method == "POST":
        node_id = request.POST.get('node_id')
	table_id = request.POST.get('table_id')
	flow_id = request.POST.get('flow_id')
        x1 = request.POST.get('cookie')
	x2 = request.POST.get('priority')
	x3 = string.atoi(x1)
	x4 = string.atoi(x2)
	#x3 = request.POST.get('second')
	#x4 = request.POST.get('nasosecond')
	#x5 = request.POST.get('packet-count')
	#x6 = request.POST.get('byte-count')
	#x7 = request,POST.get('order')
	#x8 = request.POST,get('or

    infolo = {"flow":[{"id":flow_id,"instructions": {"instruction":[{"apply-actions":{"action": [{"drop-action": {},"order":0}]},"order":0}]},"cookie":x3,"priority":x4,"table_id":table_id}]}
    url = 'http://10.0.2.15:8181/restconf/config/opendaylight-inventory:nodes/node/'+node_id+'/flow-node-inventory:table/'+table_id+'/flow/'+flow_id
    response = requests.put(url ,data=json.dumps(infolo),auth=('admin','admin'),headers={'Content-Type':'application/json'})
    #print response
    #print response.text
    if response == 200:
	result = 1
	return HttpResponse(json.dumps({"result":result}))
    else:
	result = 0
	return HttpResponse(json.dumps({"result":result}))
    #return 1
