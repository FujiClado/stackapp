import requests
from flask import Flask, render_template, request
import os
import requests
import re
import redis

app = Flask(__name__)


@app.route("/", defaults={"ip": None},strict_slashes=False)
@app.route("/<ip>",strict_slashes=False)
def search(ip):
  
  

  if ip != None:

    # Checking ipaddress is valid.
    pattern = re.compile("^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$")
    valid_ip = pattern.match(ip.strip())
    
    if valid_ip:
      
      try:

        redis_con = redis.StrictRedis(host=caching_server, 
                              port=caching_port,
                              charset="utf-8",
                              decode_responses=True)

      except:
        
        return render_template('error.tmpl',msg="Redis connection failed.")
      

      redis_result = redis_con.get(ip)

      if redis_result:

        return render_template('result.tmpl',hostname=hostname,country=redis_result,redis_status=True) 

      
      if ipstack_key:
          
          try:

            url = 'http://api.ipstack.com/{}?access_key={}'.format(ip,ipstack_key)
            country = requests.get(url).json()['country_name']
            redis_con.set(ip,country)

            return render_template('result.tmpl',hostname=hostname,country=country,redis_status=False)

          except:
            
            return render_template('error.tmpl',msg="https://ipstack.com api request failed.")
      else:

        return render_template('error.tmpl',msg="https://ipstack.com api key is not provided.")

    else:
    
      return render_template('error.tmpl',msg="Invalid ipaddress.")

  else:

    return render_template('index.tmpl')





if __name__ == '__main__':

  hostname = os.getenv('HOSTNAME',None)

  ipstack_key = os.getenv('IPSTACK_KEY',None)
  caching_server = os.getenv('CACHING_SERVER',None)
  caching_port = os.getenv('CACHING_PORT',6379)

  app.run(host='0.0.0.0',port=8080,debug=True)