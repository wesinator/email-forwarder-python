# email-forwarder
High-level email forwarding in Python

## Usage
```python
from email_forwarder import EmailForwarder

e = EmailForwarder("user@example.com", "password", "smtp.example.com", 587)

eml = open("message.eml", 'r').read()
e.forward(eml, "to@example.com")
```

**Note:** current implementation forwards in place without adding original `From` info.
