# THIS IS NOTIFICATION SERVICE 

# Architecture 
[Django API] OR CLIENT (any request sender`)
    │
    │  (1) HTTP POST /notify/
    ▼
[ FastAPI Notification Server ]
    │
    │  (2) Send task to Celery (async)
    ▼
[ Celery Worker ]
    │
    │  (3) Process message
    ▼
[ Redis Pub/Sub or Direct WebSocket Send ]
    │
    ├──► [ WebSocket Users (online) ]
    └──► [ Save in DB / Send to Firebase / Log ]




