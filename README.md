# 🐳 Docker Learning Journey — From Fundamentals to Production‑Ready Systems

> A hands‑on, end‑to‑end Docker learning repository focused on **real DevOps workflows**, not just syntax.
> This repo documents *what I built*, *what broke*, *why it broke*, and *how I fixed it* — the same skills used in real engineering teams.

---

## 🚀 Why this repository exists

Many Docker repos show **hello‑world examples**. This one demonstrates **operational understanding**:

* How containers actually behave at runtime
* How multi‑container systems communicate
* Why things fail (networking, state, ports, registries)
* How Docker fits into modern DevOps and cloud workflows

This repo is designed to be useful for:

* **Recruiters** scanning for practical Docker experience
* **Engineers** reviewing how I reason about systems
* **Myself** as a living reference for production patterns

---

## 🧱 What Docker is (quick context)

Docker is a **lightweight application packaging and runtime platform** that allows applications and their dependencies to be shipped as containers.

At a high level:

* Containers share the host OS kernel
* Each container packages its own application + libraries
* Docker Engine manages build, run, and isolation
* Registries (Docker Hub / AWS ECR) store and distribute images

This repo follows that lifecycle **end‑to‑end**.

---

## 📚 Learning Path (Structured)

The repository mirrors a real progression used in industry.

### 1️⃣ Containers vs Virtual Machines

**Key concepts learned:**

* Containers start in seconds; VMs take minutes
* Containers are process‑level isolated, not full OS
* Containers are more resource‑efficient and portable

**Why this matters:**
Understanding this distinction explains *why* Docker is used for CI/CD, microservices, and cloud workloads.

---

### 2️⃣ Docker Setup & Core Commands

**Covered:**

* Installing Docker
* `docker version`, `docker info`
* Understanding images vs containers

**Outcome:**
Confidence navigating Docker locally without copy‑pasting commands blindly.

---

### 3️⃣ Dockerfiles — Building Images Properly

**What I implemented:**

* Writing Dockerfiles from scratch
* Using official base images
* Correct instruction ordering for caching

**Key instructions used:**

* `FROM`
* `WORKDIR`
* `COPY`
* `RUN`
* `CMD`

**Important learning:**
Dockerfiles are **layered build graphs**, not scripts. Instruction order directly affects build speed and reproducibility.

---

### 4️⃣ Running Single‑Container Applications

**Projects included:**

* Flask API containers
* FastAPI services

**Concepts learned:**

* Port mapping (`host:container`)
* Why an app can be running but unreachable
* Container lifecycle: run → stop → remove

This stage built intuition before introducing complexity.

---

### 5️⃣ Docker Networking (Where Most People Get Stuck)

**Critical concepts learned:**

* Containers do **not** share `localhost`
* Docker creates isolated virtual networks
* Containers communicate via **service/container names**

**Commands used:**

* `docker network ls`
* `docker network inspect`
* Manual vs automatic networking

**Key realisation:**

> Most Docker bugs are networking misunderstandings, not code bugs.

---

### 6️⃣ Docker Compose — Multi‑Container Systems

**What I built:**

* Flask + Redis application
* Multi‑service `docker-compose.yml`

**Concepts covered:**

* Service definitions
* `depends_on`
* Automatic networking
* Environment variables

**Why this matters:**
Docker Compose models **system topology**, not just containers. This mirrors real production stacks.

---

### 7️⃣ State & Persistence (Redis + Volumes)

**Problem observed:**

* Data loss when containers restart

**Solution implemented:**

* Named Docker volumes
* Mounted Redis data directories

**Learning outcome:**
Containers are ephemeral — **state must be externalised**.

This is foundational for databases, caches, and production reliability.

---

### 8️⃣ Docker Registries (Docker Hub & AWS ECR)

**Hands‑on work:**

* Tagging images correctly
* Authenticating via CLI
* Pushing images to Docker Hub
* Pushing and pulling images from AWS ECR

**Advanced Compose usage:**

* Swapping `build:` → `image:`
* Running remote images without rebuilding

**Why this matters:**
This is the exact workflow used in CI/CD pipelines.

---

## 🧠 Questions, Misconceptions & Debugging Moments (From My Learning Process)

This section intentionally documents **real questions I asked, MCQ mistakes I made, and misconceptions I corrected** while working through the Docker module. These are based on lecture transcripts, exercises, challenges, and debugging sessions — not hindsight.

---

### ❓ Containers, Images & Theory Misconceptions

**Misconception:**

> "A container *is* the application"

**Correction:**

* A container is a **running instance of an image**
* Images are immutable blueprints
* Containers are ephemeral runtime processes

This distinction became critical later when debugging restarts, data loss, and registry pulls.

---

**Misconception (MCQ):**

> "Containers are lighter because they remove the OS entirely"

**Correction:**

* Containers **share the host OS kernel**
* They still require user-space binaries and libraries
* This explains why Linux containers behave differently across hosts

---

### ❓ VMs vs Containers (FAMOUS Interview Question)

**Initial confusion:**

> "Containers are just smaller VMs"

**Clarified understanding:**

| Virtual Machines | Containers              |
| ---------------- | ----------------------- |
| Full guest OS    | Share host kernel       |
| Heavyweight      | Lightweight             |
| Slower startup   | Start in seconds        |
| Strong isolation | Process-level isolation |

This question appears repeatedly in interviews and MCQs, and understanding *why* each exists matters more than memorising the table.

---

### ❓ Dockerfile & Build Process Misconceptions

**Misconception:**

> "Dockerfile instructions run top to bottom like a script"

**Correction:**

* Each instruction creates a **cached image layer**
* Order directly impacts rebuild speed
* COPY-ing dependency files first enables cache reuse

This explained why small code changes sometimes triggered long rebuilds.

---

### ❓ Web App Containerisation Confusions

**Misconception:**

> "If my app runs locally, it will run in Docker"

**Reality discovered:**

* Missing dependencies
* Incorrect working directories
* Port exposure vs port mapping confusion

Fixing this built strong intuition around container isolation.

---

### ❓ Docker Networking (Major Learning Moment)

**Misconception (very common):**

> "localhost inside one container refers to another container"

**Correction:**

* Each container has its **own network namespace**
* `localhost` always refers to *itself*
* Containers communicate via **service/container names**

This misunderstanding directly caused:

* MySQL connection errors
* Redis connection failures

Once resolved, most networking issues disappeared.

---

### ❓ Docker Compose Misunderstandings

**Misconception:**

> "Docker Compose is just a shortcut for docker run"

**Correct understanding:**

* Compose defines **system architecture**
* It creates a shared virtual network
* It models dependencies and runtime configuration

This reframed Compose as an **orchestration-lite tool**, not convenience syntax.

---

### ❓ Registry & ECR Confusion

**Misconception:**

> "If an image exists locally, Docker Compose will use it"

**Correction:**

* `build:` builds locally
* `image:` pulls from a registry
* Auth, tags, and regions all matter

This surfaced while debugging ECR networking and authentication issues.

---

### ❓ Persistence & State

**Misconception:**

> "Stopping a container should keep application data"

**Correction:**

* Containers are disposable
* State must live in volumes or external services

This became clear during the Redis persistence bonus challenge.

---

### ❓ Environment Variables & Configuration

**Early confusion:**

> "Why not hardcode connection details?"

**Learning outcome:**

* Environment variables decouple config from images
* Enables reuse across environments
* Critical for CI/CD and cloud deployments

---

### ❓ Load Balancing & nginx (Bonus Insight)

**Key learning:**

* Containers scale horizontally
* A reverse proxy (nginx) distributes traffic
* This pattern mirrors real production systems

---

### 🧠 Meta-Learning Outcome

The biggest lesson from this module was:

> Most Docker problems are **mental model problems**, not command problems.

This repo documents the transition from memorising commands to **reasoning about systems**.

---

## 🛠 Skills Demonstrated

* Containerisation of real applications
* Dockerfile design & optimisation
* Container networking
* Multi‑container orchestration
* State management with volumes
* Image distribution via registries
* Debugging broken container systems

---

## 🧾 Docker Commands Used Throughout This Module

This section lists **all key Docker commands I used hands-on**, grouped by learning stage. These are not copied reference lists — each command below was executed during builds, debugging, deployment, or challenges in this repo.

---

### 🔹 Docker Setup & Core Inspection

```bash
docker --version
docker version
docker info
```

Used to verify installation, daemon health, and runtime configuration.

---

### 🔹 Images & Containers (Fundamentals)

```bash
docker images
docker ps
docker ps -a
docker pull <image>
docker run <image>
docker stop <container>
docker rm <container>
docker rmi <image>
```

Built intuition around the **image → container lifecycle** and container ephemerality.

---

### 🔹 Building Images with Dockerfiles

```bash
docker build -t <image-name> .
docker build -t <image-name>:<tag> .
```

Used repeatedly while iterating on Dockerfiles and optimising build layers.

---

### 🔹 Running Containers (Ports & Environment)

```bash
docker run -p 5000:5000 <image>
docker run -d -p 5000:5000 <image>
docker run --name <container-name> <image>
docker run -e KEY=value <image>
```

Helped clarify the difference between **EXPOSE** and actual port mapping.

---

### 🔹 Debugging & Inspection

```bash
docker logs <container>
docker exec -it <container> /bin/sh
docker inspect <container>
```

Essential for diagnosing crashes, networking failures, and misconfiguration.

---

### 🔹 Docker Networking

```bash
docker network ls
docker network inspect <network>
docker network create <network>
docker network connect <network> <container>
```

Used while debugging MySQL/Redis connectivity and understanding container DNS.

---

### 🔹 Docker Compose (Multi-Container Systems)

```bash
docker compose up
docker compose up -d
docker compose down
docker compose ps
docker compose logs
```

Used to model multi-service systems, shared networking, and dependency order.

---

### 🔹 Volumes & Persistence

```bash
docker volume ls
docker volume inspect <volume>
```

Validated persistent Redis state across container restarts.

---

### 🔹 Docker Registries (Docker Hub & AWS ECR)

```bash
docker login
docker tag <local-image> <repo>:<tag>
docker push <repo>:<tag>
docker pull <repo>:<tag>
```

Used to publish, retrieve, and reuse images across environments.

---

### 🔹 AWS ECR (CLI-integrated Workflow)

```bash
aws ecr get-login-password | docker login --username AWS --password-stdin <account>.dkr.ecr.<region>.amazonaws.com
```

Enabled authenticated pushes and pulls from private registries.

---

### 🔹 Multi-Stage Builds (Image Optimisation)

```dockerfile
FROM <builder-image> AS builder
FROM <runtime-image>
COPY --from=builder /app /app
```

Reduced image size and attack surface by separating build and runtime stages.

---

## 📌 How this maps to real DevOps work

This repo directly supports:

* CI/CD pipelines
* Cloud deployments
* Microservice architectures
* Platform & infrastructure roles

It intentionally avoids toy examples and focuses on **operational realism**.

---

## 🔜 Next Steps

Planned extensions:

* Failure & recovery experiments
* Restart policies
* Health checks
* Observability hooks
* Kubernetes transition

---

## 📎 Final note

This repository represents **learning by building, breaking, and fixing** — the same loop used in real engineering teams.


