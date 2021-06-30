import redis
from redis import StrictRedis
import requests
import random
redis_host = "localhost"
redis_port = 6379
global response
import time

country = input("Enter country: ")
n = int(input("Enter number of universities: "))
print()

def redis_string():
	try:
		r = redis.StrictRedis(host=redis_host,port=redis_port,decode_responses=True)
		with r.pipeline() as pipe:
			for univ_id,univ in universities.items():
				pipe.hset(univ_id,None,None,univ)
			pipe.execute()
		print("Shortlisted University stored in Redis successfully")

		l = len(universities)

		p = 1
		while(p!=4):
			print()
			p = int(input("Enter 1 for list of shortlisted universities, 2 to delete a university from list, 3 to add a university or 4 to quit: "))
			if p==1:
				print("Getting from database")
				time.sleep(3)
				for x in range(1,l+1):
					print(r.hgetall(f"University {x}"))

			elif p==2:
				print("Getting from database")
				for x in range(1,l+1):
					print(str(x)+".",end=" ")
					print(r.hgetall(f"University {x}"))
				u = int(input("Enter no of university to delete: "))
				r.hdel(f"University {u}","name")
				print("Deleted successfully")

			elif p==3:
				u = input("Enter name of university to add: ")
				univ = {"name":u}
				r.hset(f"University {len(universities)+1}",None,None,univ)
				l += 1
				print("Added successfully")

 

	except Exception as e:
		print(e)



def get_data(country,n):
	url = f"http://universities.hipolabs.com/search?country={country}"
	res = requests.get(url)
	response = res.json()
	for x in range(0,n):
		results = response[x]["name"]
		print(results)

def shortlist():
	global e
	e=[]
	entry=""
	while entry != 'quit':
		entry = input('Enter university ("quit" to finish) : ')
		e.append(entry)
	e.pop()
	university = {}
	global universities
	universities = {}
	i = 1
	for x in e:
		university = {"name":x}
		universities[f"University {i}"] = university
		i += 1




get_data(country,n)
shortlist()
redis_string()





















