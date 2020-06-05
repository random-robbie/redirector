# redirector

Redirects any request with which ever http status code you want to a location of your choice

it will ignore all requests and force a redirection to the url you have set.

By default it will redirect to AWS metadata endpoint but can be changed by using `-u http://someothersite.com`


```
usage: redirector.py [-h] [-u URL] [-c CODE] [-p PORT]

optional arguments:
  -h, --help            show this help message and exit
  -u URL, --url URL     url to redirect to
  -c CODE, --code CODE  HTTP Status Code
  -p PORT, --port PORT  Port to listen to
 ```
