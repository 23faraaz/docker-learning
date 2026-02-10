# 🧪 CoderCo Containers Challenge  
### Multi-Container Flask + Redis System (Docker, Compose, NGINX)

> A multi-container Docker system built to surface **real DevOps failure modes**:  
> container ephemerality, service networking, state persistence, configuration drift, and horizontal scaling.
>
> This project documents not just *what works*, but **what broke, why it broke, and how the system was evolved** toward production-ready patterns.

---

## ⚡ If you read one thing

This project demonstrates my ability to:

- Debug multi-container networking failures  
- Reason clearly about **state vs stateless services**  
- Introduce persistence correctly using Docker volumes  
- Decouple configuration using environment variables  
- Scale services safely using a reverse proxy (NGINX)  

These are the **same failure modes encountered in real production systems**, not toy examples.

---

## 🎯 Challenge Overview

**Objective:**  
Build and progressively harden a multi-container application using Docker and Docker Compose.

**Core services:**
- **Flask** web application  
- **Redis** key-value store  

**Functional requirements:**
- `/` → welcome route  
- `/count` → increments and displays a visit counter stored in Redis  

**Extended goals (bonus):**
- Persistent storage for Redis  
- Environment-based configuration  
- Horizontal scaling  
- Load balancing via NGINX  

---

## 🧱 System Architecture

**Flask (stateless)**  
- Handles HTTP requests  
- Reads/writes visit count from Redis  
- Designed to scale horizontally  

**Redis (stateful)**  
- Stores visit counter  
- Uses a Docker volume for persistence  

**Docker Compose**  
- Defines system topology  
- Manages service networking and dependencies  

**NGINX (bonus)**  
- Reverse proxy  
- Load balances traffic across multiple Flask replicas  

---

## 🛠 Implementation Journey

### 1️⃣ Base Multi-Container Application

**What I built**
- Flask app with two routes  
- Redis counter using `INCR`  
- Dockerfile for Flask  
- Docker Compose file defining both services  

**Key insight**
> Docker Compose automatically creates a shared virtual network, allowing services to communicate by name.

---

### 2️⃣ Early Failures & Mental Model Fixes

**What broke**
- Flask could not connect to Redis despite Redis running  

**Incorrect assumption**
> “If Redis is up, Flask will connect automatically.”

**Correct understanding**
- Containers do **not** share localhost  
- Service names act as DNS hostnames  
- Ports do not imply connectivity  

Fixing the mental model resolved multiple downstream issues.

---

### 3️⃣ Persistent Storage (Bonus)

**Observed failure**
- Visit counter reset after container restart  

**Why it happened**
- Containers are ephemeral by default  

**Fix implemented**
- Added a named Docker volume  
- Mounted Redis `/data` directory  

**DevOps principle reinforced**
> State must live *outside* containers.

---

### 4️⃣ Environment Variables (Bonus)

**Initial implementation**
- Redis host and port hard-coded in Flask  

**Why this was bad**
- Tightly couples code to environment  
- Breaks portability  
- Not CI/CD friendly  

**Improvement**
- Injected `REDIS_HOST` and `REDIS_PORT` via Compose  
- Read configuration using environment variables  

**Outcome**
- Same image runs across environments without modification  

---

### 5️⃣ Scaling & Load Balancing with NGINX (Bonus)

**Attempted action**
```bash
docker compose up --scale web=3
```
### ⚠️ Scaling Failure & Architectural Correction (NGINX)

**Failure encountered**
- Host port conflicts when scaling the Flask service

**Incorrect assumption**
> “Scaling a service automatically exposes all replicas.”

**What actually happens**
- Multiple containers cannot bind to the same host port
- Scaling without changing exposure strategy leads to runtime failure

**Correct approach**
- Replace `ports` with `expose` for the Flask service
- Introduce an **NGINX reverse proxy**
- Bind a **single external port** at the proxy layer

**Result**
- Horizontally scalable Flask service
- Traffic evenly distributed across replicas
- No port conflicts

This mirrors **real production architectures**, where services scale internally and ingress is handled separately.

---

## ❓ Misconceptions I Corrected

- ❌ Containers preserve data by default  
- ❌ Exposed ports enable container-to-container communication  
- ❌ Scaling services automatically makes them accessible  
- ❌ Docker Compose is just a shortcut for `docker run`  

**Correct mental model**
- Containers are disposable  
- Networking is explicit  
- Docker Compose models **systems**, not commands  
- Reverse proxies are required for scalable services  

---

## 🧾 Commands Used (In Context)

These commands were executed **in response to real failures**, not as a checklist.

```bash
# Build & run
docker build -t flask-app .
docker compose up
docker compose up --build

# Debugging
docker ps
docker logs <container>
docker exec -it <container> /bin/sh

# Volumes
docker volume ls
docker volume inspect redis-data

# Scaling
docker compose up --scale web=3

# Teardown
docker compose down
