import json
string = '["{\"RequestDetails\": {\"Connection\": {\"SSL\": \"Yes\", \"LAN IPAddress\": \"192.168.188.55\"}, \"Time\": {\"RequestSent\": \"2016-11-14 10:59:47.416800\"}}, \"Server\": {\"Action\": {\"Register\": \"True\"}, \"ServerDetails\": {\"NetworkLoad\": {\"Received\": \"2000\", \"Sent\": \"1001\"}, \"ServerName\": \"BermDox\", \"CPU_Usage\": \"0,30\", \"ServerKey\": \"Lqdie4ARBhbJtawrmTBCkenmhb9rvqgRzWN\"}}}"]'

jsond = json.dumps(string)
print json.loads(jsond)
