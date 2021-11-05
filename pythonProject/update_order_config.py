import requests as req

protocol = "http://"
host = 'localhost'
port = 10011
service_endpoint = '/api/order/propertyConfig/propertyId/'
header = {
    'Accept': '',
    'Content-Type': 'application/json'
}

properties = [
    {
        "PropertyId": "PROP_7",
		"Name": "enableGTPBatchAssignment",
        "Description": "Enable GTP station batch assignment using DI",
        "PropertyValues": [{
            "Value": "false",
            "PropertyValueId": "ENABLEGTPBATCHASSIGNMENT"
        }]
    }, {
        "PropertyId": "PROP_8",
		"Name": "gtpAssignmentBatchSize",
        "Description": "Number of orders for GTP station batch assignment",
        "PropertyValues": [{
            "Value": "3",
            "PropertyValueId": "GTPASSIGNMENTBATCHSIZE"
        }]
    }, {
        "PropertyId": "PROP_9",
		"Name": "nextGTPBatchCreationThresholdPercentage",
        "Description": "Pct. of orders in process to form the next batch",
        "PropertyValues": [{
            "Value": "50",
            "PropertyValueId": "NEXTGTPBATCHCREATIONTHRESHOLDPERCENTAGE"
        }]
    }
]

propertyId = "PROP_7"
URL = protocol + host + ':' + str(port) + service_endpoint + propertyId

response=req.put(URL,json=properties[0],headers=header,timeout=10)
print(response)
print(response.content)