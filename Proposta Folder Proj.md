
# Archidetture scelte

## MVVM - Model View ViewModel

```markdown
identity-service/
├── prisma/
│   ├── schema.prisma
│   └── migrations/
├── src/
│   ├── main.ts
│   ├── app.module.ts
│   ├── config/                       # configurazione e validazione env (zod)
│   │   ├── configuration.ts
│   │   └── env.schema.ts
│   ├── common/                       # codice trasversale a tutti i layer
│   │   ├── guards/
│   │   │   ├── session-auth.guard.ts # verifica la sessione
│   │   │   └── roles.guard.ts        # controllo ruoli (ADMIN, USER...)
│   │   ├── decorators/
│   │   └── filters/
│   │       └── domain-exception.filter.ts # traduce errori di dominio in HTTP
│   │
│   ├── model/                        # MODEL: dati, regole di dominio, accesso al DB
│   │   ├── users/
│   │   │   ├── user.ts               # tipo User (senza passwordHash)
│   │   │   └── users.repository.ts
│   │   ├── credentials/
│   │   │   └── credentials.service.ts # hash e verifica password
│   │   └── errors/
│   │       └── domain.errors.ts      # es. EmailAlreadyUsedError
│   │
│   ├── viewmodel/                    # VIEWMODEL: casi d'uso, orchestrazione, nessun HTTP
│   │   ├── auth/
│   │   │   └── auth.viewmodel.ts     # signUp, signIn, signOut
│   │   ├── users/
│   │   │   └── users.viewmodel.ts    # deleteUser con le sue regole
│   │   └── email-verification/
│   │       └── email-verification.viewmodel.ts
│   │
│   ├── view/                         # VIEW: HTTP, validazione input, formato output
│   │   ├── auth/
│   │   │   ├── auth.controller.ts
│   │   │   ├── auth.schemas.ts       # schemi zod per input
│   │   │   └── dto/
│   │   │       ├── sign-up.dto.ts
│   │   │       └── auth-response.dto.ts
│   │   ├── users/
│   │   │   └── users.controller.ts
│   │   ├── email-verification/
│   │   │   └── email-verification.controller.ts
│   │   └── health/
│   │       └── health.controller.ts
│   │
│   ├── infrastructure/               # dettagli tecnici che implementano le interfacce del model
│   │   ├── prisma/
│   │   │   ├── prisma.module.ts
│   │   │   └── prisma.service.ts
│   │   ├── session/
│   │   │   └── session.store.ts      # DB o Redis
│   │   └── mail/
│   │       ├── mail.module.ts
│   │       ├── mailer.service.ts
│   │       ├── templates/verify-email.html
│   │       └── assets/logo.jpeg
│   │
│   └── modules/                      # composizione: collega i layer per funzionalità
│       ├── auth.module.ts
│       ├── users.module.ts
│       └── email-verification.module.ts
│
├── test/
│   ├── unit/
│   │   ├── viewmodel/auth.viewmodel.spec.ts
│   │   └── model/credentials.service.spec.ts
│   └── e2e/
│       └── auth.e2e-spec.ts
├── scripts/
├── keys/                             # gitignored
├── .env.example
├── README.md
└── package.json
```

**Dove finiscono i file attuali**

| Ora | Nuovo percorso |
|---|---|
| `auth/auth.controller.ts` | `view/auth/auth.controller.ts` |
| `auth/auth.schemas.ts` | `view/auth/auth.schemas.ts` |
| `auth/auth.service.ts` | `viewmodel/auth/auth.viewmodel.ts` |
| `auth/credentials/credentials.service.ts` | `model/credentials/credentials.service.ts` |
| `auth/session/session-auth.provider.ts` | `common/guards/session-auth.guard.ts` |
| `auth/session/session.store.ts` | `infrastructure/session/session.store.ts` |
| `users/users.repository.ts` | `model/users/users.repository.ts` |
| `users/user.ts` | `model/users/user.ts` |
| `prisma/*` | `infrastructure/prisma/*` |
| `mail/mailer.service.ts` | `infrastructure/mail/mailer.service.ts` |
| `mail/email-verification/*.controller.ts` | `view/email-verification/` |
| `mail/email-verification/*.service.ts` | `viewmodel/email-verification/` |
| `health/` | `view/health/` |

**Come procedere con git**

Fai un commit per ogni layer spostato, come discusso prima. Usa `git mv` per conservare la cronologia. Il primo commit sposta `prisma/` e `mail/` in `infrastructure/`, perché sono le dipendenze più basse. Poi sposti `model/`, poi `viewmodel/`, infine `view/` e `modules/`. Dopo ogni commit il progetto deve compilare e i test devono passare. Gli import si aggiornano in ogni commit, non alla fine.

**Nota per il front-end**

MVVM è più naturale nel front-end. Lì il **View** è il componente React, il **ViewModel** è un hook (`useSignIn`, `useSignUp`) che gestisce stato e chiamate, e il **Model** è il client API con i tipi condivisi. Se la web app è in React, potremmo applicare MVVM anche lì, con la stessa struttura a tre cartelle.