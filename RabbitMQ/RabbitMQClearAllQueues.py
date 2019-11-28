'''
RabbitMQ Reference Pages:
 - https://www.rabbitmq.com/uri-spec.html
 - http://localhost:15672/api/

'''

import requests

queuesRequest = requests.get("http://localhost:15672/api/queues", auth=("guest", "guest"))

def escape_bad_characters(text):
	return text.replace("/", "%2F").replace(" ", "%20").replace("#", "%23")

queues = [(escape_bad_characters(queue["vhost"]), escape_bad_characters(queue["name"]), queue["messages"]) 
			for queue in queuesRequest.json() if queue["messages"] > 0] 

# print(queues)

print(str(len(queues)) + " queues to clear")
deleteRequests = []
for queue in queues:
	if queue[2] > 0:
		request = requests.delete(
			"http://localhost:15672/api/queues/" + queue[0] + "/" + queue[1] + "/contents",
			auth=("guest", "guest")
		)
		deleteRequests.append(request)
		
		is_success = "Cleared " + str(queue[2]) if request.status_code == 204 else "Unknown Response " + str(request.status_code)
		print("\t" + queue[1] + ": " + is_success)

print("Done")
