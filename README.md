# Virginia Guide Service Website

The official website for the **Virginia Guide Service**, a student organization
at the University of Virginia that offers historical walking tours of Grounds —
including standard tours, specialty tours, and private admission tours upon request.

🌐 [Live Site](https://virginiaguides.org)

---

## Overview

This is a full-stack monorepo containing both the frontend and backend for the
Virginia Guide Service website. The platform was built as a full migration away
from a legacy WordPress site, delivering a modernized, scalable codebase with
greater flexibility for future development. The two services are deployed
independently and communicate via a REST API.

| Layer | Technology | Deployed On |
|---|---|---|
| Frontend | Nuxt.js / Vue.js | Vercel |
| Backend | Django (Python) | Render |
| Database | PostgreSQL | Render |
| File Storage | Amazon S3 | AWS |
| Email | Mailgun | Bluehost / Mailgun |
| Domain | virginiaguides.org | Bluehost |

---

## Repository Structure

```
guides-website/
├── frontend/                   # Nuxt.js / Vue.js application
│   ├── app/                    # Pages, components, layouts
│   ├── assets/                 # Images, fonts, global styles
│   ├── nuxt.config.ts          # Nuxt configuration (API base, meta tags, fonts)
│   ├── tsconfig.json           # TypeScript configuration
│   └── package.json            # Frontend dependencies
├── backend/                    # Django REST API
│   ├── api/                    # API views, serializers, URLs
│   ├── guides_website_backend/ # Django project config
│   ├── utils/                  # Shared utility functions
│   ├── manage.py               # Django management CLI
│   └── requirements.txt        # Backend dependencies
├── .gitignore
└── README.md
```

---

## Features

- **Tour Information** — Overview of all available tour types offered by the club
- **Specialty Tours** — Dedicated page for themed specialty tours
- **Tour Sign-Ups** — Online sign-up flow for prospective visitors
- **Automated Email Confirmations** — Mailgun-powered confirmation emails
  sent automatically on sign-up
- **Event Listings** — Up-to-date schedule of events
- **REST API** — Django backend serving content to the Nuxt frontend

---

## Getting Started

### Prerequisites
- Node.js 18+
- Python 3.10+
- PostgreSQL

---

### Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

The frontend will be running at `http://localhost:3000`.

> **No `.env` file needed for local development.** The API base URL is
> configured in `nuxt.config.ts` and defaults to `http://127.0.0.1:8000`
> automatically when `NUXT_PUBLIC_API_BASE` is not set. For production,
> this variable is set directly in the Vercel dashboard.

---

### Backend Setup

```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

The backend API will be running at `http://127.0.0.1:8000`.

Create a `.env` file inside `backend/`:
```
# Django
SECRET_KEY=your_django_secret_key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Mailgun
EMAIL_BACKEND=anymail.backends.mailgun.EmailBackend
MAILGUN_API_KEY=your_mailgun_api_key
MAILGUN_DOMAIN=virginiaguides.org
DEFAULT_FROM_EMAIL=no-reply@virginiaguides.org

# Scheduler, Chair, Vice Chair email recipients (update for production)
EMAIL_SCHEDULER_RECEIVER=tech@virginiaguides.org
EMAIL_CHAIR_RECEIVER=tech@virginiaguides.org
EMAIL_CHAIR_RECEIVER2=tech@virginiaguides.org
EMAIL_CHAIR_RECEIVER3=tech@virginiaguides.org

# Local dev email testing only (remove in production)
EMAIL_HOST=mail.virginiaguides.org
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=no-reply@virginiaguides.org
EMAIL_HOST_PASSWORD=your_email_host_password
```

> **Note:** The `EMAIL_HOST` block is for local development testing only.
> In production, all email is handled through Mailgun.

---

## Deployment

The frontend and backend are deployed independently. Each platform is pointed
at its respective subfolder in this monorepo.

| Service | Platform | Root Directory |
|---|---|---|
| Frontend | Vercel | `frontend/` |
| Backend | Render | `backend/` |

The `NUXT_PUBLIC_API_BASE` environment variable must be set in the **Vercel
dashboard** to point to the live Render backend URL.

---

## Related Links

- 🎓 [University of Virginia](https://www.virginia.edu)
- 🔗 [Virginia Guide Service](https://virginiaguides.org)

---

## License

MIT License — see [LICENSE](LICENSE) for details.

---

Built with ❤️ for the storytellers who walk these Grounds and the trailblazers who paved the way 🌿
