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




# Two different types of notifications are sent,

1. Sending a message to a specific user for a specific operation

2. Sending a broadcast type notification (to all users or to a specific segment)

# FOR ONE USER

[Django API or Client]
   │
   │  (1) POST /notify/  {"template_name": "...", "data": {...}, "recipient": {...}} 
# User information is always included with the request so that the messaging service doesn't have to ask and waste time.
   ▼
[ FastAPI Notification API ]
   │
   │  (2) Create Notification
   │      Create DeliveryLog (for 1 user)
   │      Send Celery Task: (notification_id, recipient)
   ▼
[ Celery Worker ]
   │
   │  (3) Load Template
   │      Render Template with data
   │      Dispatch to recipient.channel
   ▼
[ Channel Dispatcher ]
   │
   ├──► [ WebSocket (if online) ]
   ├──► [ Email / SMS / Firebase ]
   └──► [ Update DeliveryLog: status=sent/failed ]


# BroadCast message

[Django API or Admin Trigger]
   │
   │  (1) POST /notify/broadcast/
   │      {"template_name": "...", "data": {...}, "audience": "subscribed"}
   ▼
[ FastAPI Notification API ]
   │
   │  (2) Create Notification (is_broadcast=True)
   │
   │  (3) Fetch users list (from E-commerce API or DB/cache)
   │
   │  (4) For each user:
   │        - Create DeliveryLog
   │        - Send Celery Task: (notification_id, recipient)
   ▼
[ Celery Worker ]
   │
   │  (5) Load Template
   │      Render Template with data
   │      Dispatch to recipient.channel
   ▼
[ Channel Dispatcher ]
   │
   ├──► [ WebSocket (if online) ]
   ├──► [ Email / SMS / Firebase ]
   └──► [ Update DeliveryLog: status=sent/failed ]