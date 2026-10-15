# FastAPI + React — interview-lite

A stripped-down fork of [fastapi/full-stack-fastapi-template](https://github.com/fastapi/full-stack-fastapi-template)
for **timeboxed builds** (take-home / "vibe code this in 2 hours" interviews).
Same stack, minus everything that slows a 2-hour build.

Based on upstream `master` @ `7257e60` — branch `interview-lite`.

## Kept
- **Backend:** FastAPI, SQLModel, Pydantic settings
- **Frontend:** React, TypeScript, Vite, Tailwind, shadcn/ui, TanStack Query/Router, dark mode
- **Generated, typed API client** (regenerated on every `./verify` so it never drifts)
- **Playwright** e2e
- An example `Items` CRUD resource (list, add, edit, delete) to copy for the real domain

## Removed
Auth/users/JWT, email + Mailpit, Postgres → **SQLite**, Alembic → `create_all` on startup,
Docker Compose, Traefik, Sentry, CI, react-email package.

## Prerequisites
- [uv](https://docs.astral.sh/uv/): `curl -LsSf https://astral.sh/uv/install.sh | sh`
- [bun](https://bun.sh): `curl -fsSL https://bun.sh/install | bash`
- `git`, `curl`

## Scripts
| | |
|---|---|
| `./setup` | install Python + JS deps and Playwright Chromium (~30s cold) |
| `./run` | dev: FastAPI :8000 (reload) + Vite :5173 (HMR, proxies `/api`) |
| `./run --prod` | build frontend, serve everything from FastAPI on :8000 |
| `./verify` | ruff → pytest → regenerate client → biome → build → boot → Playwright. Last line `VERIFY: GREEN` or `VERIFY: RED (stage)`. `--quiet` for one line. |
| `./commit "msg"` | runs `./verify --quiet`, commits only if GREEN |
| `./milestone [next-branch]` | verify, commit, fast-forward `main`, start next branch |

## Configuration
Settings are read from `APP_*` env vars (prefixed so a machine-wide `DATABASE_URL` can't leak in):
`APP_DATABASE_URL` (default `sqlite:///./app.db`), `APP_PROJECT_NAME`.

## Notes
- JS tools run on bun's runtime (`--bun`) so native packages match bun's architecture
  (avoids x64-Node-under-Rosetta vs arm64-package mismatches on Apple Silicon).

## License
MIT, same as upstream — see LICENSE.
