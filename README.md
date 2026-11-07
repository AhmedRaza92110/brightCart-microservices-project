# BrightCart — E-commerce Microservices + GitOps CI/CD

A portfolio-ready learning project demonstrating a bright, responsive storefront and a 7-service e-commerce backend, Docker Compose local development, GitHub Actions CI, Helm, Kubernetes, and Argo CD GitOps deployment.

## Architecture

- **Frontend:** responsive React-free static storefront (HTML/CSS/JS) served by Nginx.
- **Services:** `auth-service`, `profile-service`, `product-service`, `order-service`, `payment-service`, `message-service`, `history-service`.
- **Local runtime:** Docker Compose.
- **CI:** GitHub Actions runs Python compile/smoke checks, builds service images, pushes images to GHCR.
- **CD/GitOps:** CI updates image tags in `deploy/helm/brightcart/values.yaml`; Argo CD watches the chart path and reconciles Kubernetes.
- **Kubernetes:** Helm chart deploys services and frontend into one namespace.

> Learning/demo project: services use in-memory sample data, mock payments and local demo credentials. Do not use for real customers, real payment data, or production authentication without hardening.

## Run locally

Requirements: Docker Desktop / Docker Engine + Compose.

```bash
docker compose up --build
```

Open http://localhost:8080. API health checks:
- http://localhost:8001/health (auth)
- http://localhost:8002/health (profile)
- http://localhost:8003/health (product)
- http://localhost:8004/health (order)
- http://localhost:8005/health (payment)
- http://localhost:8006/health (message)
- http://localhost:8007/health (history)

Stop: `docker compose down`.

## Repository layout

```text
services/                 Seven FastAPI microservices
frontend/                 BrightCart storefront UI
deploy/helm/brightcart/   Helm chart and image values
deploy/argocd/            Argo CD Application
.github/workflows/        CI, image publishing and GitOps tag update
```

## GitHub setup (GHCR + GitOps)

1. Create a GitHub repository and push this project to its default branch.
2. In **Settings → Actions → General**, enable read/write workflow permissions (or use a dedicated GitOps token if your organization restricts `GITHUB_TOKEN`).
3. Update `.github/workflows/ci-cd.yml` if your default branch is not `main`.
4. The workflow publishes images to `ghcr.io/<owner>/<repo>-<service>:<commit-sha>` and commits the resulting tags into `deploy/helm/brightcart/values.yaml`. Argo CD then detects the Git change.
5. For a private GHCR package, configure Kubernetes `imagePullSecrets` in the target namespace. Public packages are easier for a demo cluster.
6. Set `repoURL` in `deploy/argocd/application.yaml` to your repository URL, then apply it:
   ```bash
   kubectl create namespace argocd --dry-run=client -o yaml | kubectl apply -f -
   kubectl apply -f deploy/argocd/application.yaml
   ```
   Argo CD must already be installed in the cluster. The Application creates/uses namespace `brightcart`.

### Image tag flow

1. Push code → GitHub Actions tests and builds images.
2. Images are pushed with immutable commit-SHA tags.
3. CI updates `values.yaml` with those tags and commits the change.
4. Argo CD sees the Git commit, Helm renders the chart, and Kubernetes rolls out the new image.
5. Check status with `kubectl -n brightcart get pods,svc,deploy`.

**Important:** CI writes the GitOps values back to the same repo. The workflow ignores commits whose message starts with `chore(gitops):` to avoid an infinite workflow loop. For a larger team, a separate GitOps repository and protected promotion PRs are recommended.

## Local Kubernetes preview

With Docker images built locally, you can use the Helm chart after loading/pushing images to a registry accessible by your cluster. Edit `values.yaml` image repository/tag values first.

```bash
helm lint deploy/helm/brightcart
helm template brightcart deploy/helm/brightcart -n brightcart
```

## Senior DevOps improvement checklist

- Replace in-memory stores with PostgreSQL per service or a managed database.
- Add service-to-service authentication, JWT validation, secrets management, and network policies.
- Add unit/integration tests, coverage gates, dependency and container scanning (Trivy), SBOM, image signing, and provenance.
- Use a separate GitOps repo, PR-based promotion, environment overlays (`dev/stage/prod`), and rollback policy.
- Add readiness/liveness probes, resource requests/limits, HPA, PodDisruptionBudgets, observability (Prometheus/Grafana), logs/traces (OpenTelemetry), and alerts.
- Replace mock payment handling with a PCI-compliant provider integration; never store card numbers/CVV.
- Add database migrations, idempotency keys, retries, timeouts, circuit breakers, and event-driven messaging (RabbitMQ/Kafka).
- Pin GitHub Actions by commit SHA and use least-privilege permissions before production.

## Resume bullet (edit to match what you actually deploy)

**BrightCart — GitOps E-commerce Platform:** Built a containerized 7-microservice e-commerce demo with GitHub Actions CI, GHCR image publishing, Helm-based Kubernetes deployment, and Argo CD continuous delivery. Automated immutable image tagging and GitOps values updates to trigger declarative rollouts; packaged a responsive storefront with an Nginx same-origin proxy to the product service, and documented local-to-cluster workflows.
