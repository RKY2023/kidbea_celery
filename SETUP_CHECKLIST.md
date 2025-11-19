# kidbea_celery Setup Checklist

## ✅ Phase 2: kidbea_celery Complete

This repository has been fully created with all necessary files and configurations.

### Files Created

**Configuration** (4 files):
- [x] config/__init__.py
- [x] config/celery_app.py - Celery client configuration
- [x] config/beat_schedule.py - All 7 scheduled tasks
- [x] config/settings.py - Django settings (minimal)
- [x] config/logging_config.py - Logging setup

**Tasks** (4 files):
- [x] tasks/__init__.py
- [x] tasks/csv_tasks.py - CSV import/export (placeholder)
- [x] tasks/email_tasks.py - Email notifications (placeholder)
- [x] tasks/notification_tasks.py - Push notifications (placeholder)

**Monitoring** (2 files):
- [x] monitoring/__init__.py
- [x] monitoring/flower_config.py - Flower dashboard configuration

**Testing** (2 files):
- [x] tests/__init__.py
- [x] tests/test_tasks.py - Unit tests (placeholder)

**Deployment** (5 files):
- [x] requirements.txt - All dependencies (~100MB)
- [x] Dockerfile - Docker container configuration
- [x] .dockerignore - Docker build exclusions
- [x] railway.toml - Railway deployment config
- [x] Procfile - Process definitions

**Configuration Files** (3 files):
- [x] .env.example - Environment variables template
- [x] .gitignore - Git exclusions
- [x] README.md - Documentation

### Services Ready

1. **Celery Worker**
   - Queue: `default`
   - Concurrency: 2
   - Handles: CSV, Email, Notifications
   - Status: ✅ Ready

2. **Celery Beat Scheduler**
   - 7 scheduled tasks configured
   - All tasks route to `ml_tasks` queue
   - Status: ✅ Ready

3. **Flower Dashboard**
   - Port: 5555
   - Authentication: Enabled
   - Status: ✅ Ready

### Next Steps

#### 1. Create GitHub Repository
```bash
# On GitHub.com:
# 1. Click + → New repository
# 2. Name: kidbea_celery
# 3. Description: "Celery worker, beat scheduler, and Flower monitoring"
# 4. Make it PRIVATE
# 5. Create repository
```

#### 2. Initialize Git and Push
```bash
cd kidbea_celery

# Initialize git
git init
git add .
git commit -m "Initial kidbea_celery setup with worker, beat, and flower"

# Add remote
git remote add origin https://github.com/YOUR_USERNAME/kidbea_celery.git
git branch -M main
git push -u origin main
```

#### 3. Deploy to Railway
```bash
# Install Railway CLI
npm install -g @railway/cli

# Login
railway login

# Create new project
railway init

# Set environment variables
railway variables

# Add these:
# DB_NAME=kidbea
# DB_USER=postgres
# DB_PASSWORD=[your-password]
# DB_HOST=[your-host].pooler.supabase.co
# DB_PORT=6543
# CELERY_BROKER_URL=redis://...
# CELERY_RESULT_BACKEND=redis://...
# SECRET_KEY=[your-secret-key]
# FLOWER_BASIC_AUTH=admin:secure_password

# Deploy
railway up
```

#### 4. Verify Deployment
```bash
# Check logs
railway logs --follow

# Get URL
railway domains

# Access Flower
# Visit: https://[your-railway-url]:5555
# Login: admin / secure_password

# Expected output in logs:
# celery_worker: Started consuming from default queue
# celery_beat: Starting scheduler
# flower: Listening on port 5555
```

### Environment Variables Needed

```
DB_NAME=kidbea
DB_USER=postgres
DB_PASSWORD=xxx
DB_HOST=xxx.pooler.supabase.co
DB_PORT=6543
CELERY_BROKER_URL=redis://default:password@host:port
CELERY_RESULT_BACKEND=redis://default:password@host:port
SECRET_KEY=xxx
FLOWER_BASIC_AUTH=admin:secure_password
```

### File Structure
```
kidbea_celery/
├── config/
│   ├── __init__.py
│   ├── celery_app.py
│   ├── beat_schedule.py
│   ├── settings.py
│   └── logging_config.py
├── tasks/
│   ├── __init__.py
│   ├── csv_tasks.py
│   ├── email_tasks.py
│   └── notification_tasks.py
├── monitoring/
│   ├── __init__.py
│   └── flower_config.py
├── tests/
│   ├── __init__.py
│   └── test_tasks.py
├── requirements.txt
├── Dockerfile
├── .dockerignore
├── railway.toml
├── Procfile
├── .env.example
├── .gitignore
└── README.md
```

### Verification Checklist

- [ ] All files created
- [ ] GitHub repository created
- [ ] Code pushed to GitHub
- [ ] Railway project created
- [ ] Environment variables set
- [ ] Deployed to Railway
- [ ] Celery worker running (check logs)
- [ ] Celery beat running (check logs)
- [ ] Flower dashboard accessible (https://[url]:5555)
- [ ] Can login to Flower
- [ ] Beat scheduler executing tasks
- [ ] ml_tasks queue populated with scheduled tasks
- [ ] kidbea_ml worker processing tasks from ml_tasks queue

### Success Criteria

✅ **Phase 2 Complete when:**
1. kidbea_celery deployed on Railway
2. All 3 services running (worker, beat, flower)
3. Flower dashboard accessible with correct login
4. Logs show no errors
5. Scheduled tasks appear in ml_tasks queue

### Troubleshooting

**Worker not starting?**
→ Check CELERY_BROKER_URL is correct
→ Check database connection
→ Check logs for errors

**Flower 404 error?**
→ Check service is deployed and running
→ Check Railway URL is correct
→ Check FLOWER_BASIC_AUTH is set

**Beat not scheduling tasks?**
→ Check Beat service is running
→ Check logs for "scheduled" messages
→ Verify task queue is being populated

### Next Phase

After Phase 2 is complete and verified:
→ Begin **Phase 3: Create kidbea_ml repository**
→ See: `DEPLOYMENT_COMMANDS.md` (Phase 3 section)

---

**Status**: ✅ Repository structure complete | Ready for GitHub & Railway deployment
