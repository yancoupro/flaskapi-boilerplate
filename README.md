# flaskapi-boilerplate

## getting started

### on mac

run these lines in terminal

```
cd /flaskapi-boilerplate
python3.7 -m venv flaskvenv
source flaskvenv/bin/activate
flaskvenv/bin/pip install -r requirements.txt
```

# good to know

- env_demo.py contains allowed users
- main_app.py is the file to run

public url by default are :

- http://127.0.0.1:8090/api/alarm/111?uid=user1001&key=langDevo
  > 111 is any code the esp32 wants to send to differentiate reasons for the call
  >
  > user1001 is a user from env_demo and langDevo the value for this user

- http://127.0.0.1:8090/api/watchdog?uid=user1001&key=langDevo


