---
name: security-best-practices
description: >
  Comprehensive security hardening for web applications covering HTTPS, input validation,
  authentication, and OWASP Top 10 vulnerabilities. Enforces security headers, CSRF protection,
  JWT auth with refresh token rotation, and secret management. Use for new projects, security
  audits, public APIs, and compliance.
tags:
  - security
  - owasp
  - web
  - authentication
license: MIT
metadata:
  version: "1.0.0"
  source-repo: "https://github.com/supercent-io/skills-template"
  source-ref: "main"
  installed-from: "npx-skills"
  weekly-installs: "14.1K"
  fetched-at: "2026-04-14"
  last-reviewed: "2026-04-14"
---

# Security Best Practices

## When to use this skill

- **New project**: consider security from the start
- **Security audit**: inspect and fix vulnerabilities
- **Public API**: harden APIs accessible externally
- **Compliance**: comply with GDPR, PCI-DSS, etc.

## Instructions

### Step 1: Enforce HTTPS and security headers

```typescript
import express from 'express';
import helmet from 'helmet';
import rateLimit from 'express-rate-limit';

const app = express();

app.use(helmet({
  contentSecurityPolicy: {
    directives: {
      defaultSrc: ["'self'"],
      scriptSrc: ["'self'", "'unsafe-inline'", "https://trusted-cdn.com"],
      styleSrc: ["'self'", "'unsafe-inline'"],
      imgSrc: ["'self'", "data:", "https:"],
      connectSrc: ["'self'", "https://api.example.com"],
      fontSrc: ["'self'", "https:", "data:"],
      objectSrc: ["'none'"],
      mediaSrc: ["'self'"],
      frameSrc: ["'none'"],
    },
  },
  hsts: {
    maxAge: 31536000,
    includeSubDomains: true,
    preload: true
  }
}));

app.use((req, res, next) => {
  if (process.env.NODE_ENV === 'production' && !req.secure) {
    return res.redirect(301, `https://${req.headers.host}${req.url}`);
  }
  next();
});

const limiter = rateLimit({
  windowMs: 15 * 60 * 1000,
  max: 100,
  message: 'Too many requests from this IP, please try again later.',
  standardHeaders: true,
  legacyHeaders: false,
});

app.use('/api/', limiter);

const authLimiter = rateLimit({
  windowMs: 15 * 60 * 1000,
  max: 5,
  skipSuccessfulRequests: true
});

app.use('/api/auth/login', authLimiter);
```

### Step 2: Input validation (SQL Injection, XSS prevention)

```typescript
import Joi from 'joi';

const userSchema = Joi.object({
  email: Joi.string().email().required(),
  password: Joi.string().min(8).pattern(/^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]/).required(),
  name: Joi.string().min(2).max(50).required()
});

app.post('/api/users', async (req, res) => {
  const { error, value } = userSchema.validate(req.body);

  if (error) {
    return res.status(400).json({ error: error.details[0].message });
  }

  const user = await db.query('SELECT * FROM users WHERE email = ?', [value.email]);

  import DOMPurify from 'isomorphic-dompurify';
  const sanitized = DOMPurify.sanitize(userInput);

  res.json({ user: sanitized });
});
```

### Step 3: Prevent CSRF

```typescript
import csrf from 'csurf';
import cookieParser from 'cookie-parser';

app.use(cookieParser());

const csrfProtection = csrf({ cookie: true });

app.get('/api/csrf-token', csrfProtection, (req, res) => {
  res.json({ csrfToken: req.csrfToken() });
});

app.post('/api/*', csrfProtection, (req, res, next) => {
  next();
});
```

### Step 4: Manage secrets

Never commit secrets. Use environment variables:

```typescript
const dbUrl = process.env.DATABASE_URL;
if (!dbUrl) {
  throw new Error('DATABASE_URL environment variable is required');
}
```

### Step 5: Secure API authentication

**JWT + Refresh Token Rotation**:

```typescript
const accessToken = jwt.sign({ userId }, ACCESS_SECRET, { expiresIn: '15m' });
const refreshToken = jwt.sign({ userId }, REFRESH_SECRET, { expiresIn: '7d' });

app.post('/api/auth/refresh', async (req, res) => {
  const { refreshToken } = req.body;
  const payload = jwt.verify(refreshToken, REFRESH_SECRET);

  await db.refreshToken.delete({ where: { token: refreshToken } });

  const newAccessToken = jwt.sign({ userId: payload.userId }, ACCESS_SECRET, { expiresIn: '15m' });
  const newRefreshToken = jwt.sign({ userId: payload.userId }, REFRESH_SECRET, { expiresIn: '7d' });

  res.json({ accessToken: newAccessToken, refreshToken: newRefreshToken });
});
```

## Constraints

### Required (MUST)
1. **HTTPS Only** in production
2. **Separate secrets** via environment variables
3. **Input Validation** on all user input
4. **Parameterized Queries** to prevent SQL Injection
5. **Rate Limiting** for DDoS prevention

### Prohibited (MUST NOT)
1. No `eval()` — code injection risk
2. No direct `innerHTML` — XSS risk
3. No committing secrets or `.env` files

## OWASP Top 10 Checklist

- [ ] A01: Broken Access Control — RBAC, authorization checks
- [ ] A02: Cryptographic Failures — HTTPS, encryption
- [ ] A03: Injection — Parameterized Queries, Input Validation
- [ ] A04: Insecure Design — Security by Design
- [ ] A05: Security Misconfiguration — Helmet, change default passwords
- [ ] A06: Vulnerable Components — npm audit, regular updates
- [ ] A07: Authentication Failures — strong auth, MFA
- [ ] A08: Data Integrity Failures — signature validation, CSRF prevention
- [ ] A09: Logging Failures — security event logging
- [ ] A10: SSRF — validate outbound requests

## Best Practices

1. **Principle of Least Privilege**: grant minimal privileges
2. **Defense in Depth**: layered security
3. **Security Audits**: regular security reviews

## References

- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [helmet.js](https://helmetjs.github.io/)
- [API Security Checklist](https://github.com/shieldfy/API-Security-Checklist)
