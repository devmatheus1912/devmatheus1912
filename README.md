<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://capsule-render.vercel.app/api?type=waving&color=0:0f172a,50:1e293b,100:334155&height=160&section=header&text=Matheus%20Oliveira%20dos%20Santos&fontSize=34&fontColor=e2e8f0&fontAlignY=36&desc=Full%20Stack%20%E2%80%94%20SaaS%20%C2%B7%20CMS%20institucional%20%C2%B7%20Mobile&descAlignY=55&descSize=14&descColor=94a3b8&animation=twinkling">
  <img alt="Capa do perfil — Matheus Oliveira dos Santos" src="https://capsule-render.vercel.app/api?type=waving&color=0:e2e8f0,50:f1f5f9,100:cbd5e1&height=160&section=header&text=Matheus%20Oliveira%20dos%20Santos&fontSize=34&fontColor=0f172a&fontAlignY=36&desc=Full%20Stack%20%E2%80%94%20SaaS%20%C2%B7%20CMS%20institucional%20%C2%B7%20Mobile&descAlignY=55&descSize=14&descColor=475569&animation=twinkling">
</picture>

<div align="center">

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/matheusoliveiradosantos/)
[![Instagram](https://img.shields.io/badge/Instagram-E4405F?style=flat-square&logo=instagram&logoColor=white)](https://www.instagram.com/devmatheusbb)
[![E-mail](https://img.shields.io/badge/E--mail-EA4335?style=flat-square&logo=gmail&logoColor=white)](mailto:matheusos1912@icloud.com)

</div>

<br/>

### Sobre

Desenvolvedor **Full Stack** com entregas de ponta a ponta: **APIs** robustas em Java/Spring, **aplicativos** Flutter e **produtos web** em Next.js — sempre com **PostgreSQL**, segurança bem definida (JWT/credentials) e integrações reais (pagamentos, mídia, notificações, IA).

Abaixo, **stacks por produto**, no nível de especificação que eu uso em documentação de projeto e portfólio técnico.

<br/>

---

### Faculdade Goiás — site institucional · CMS · área da equipe

**Escopo:** marketing acadêmico de alta conversão, páginas ricas de curso, credenciamento e-MEC, Payload CMS em PT-BR, `/equipe` com NextAuth e Prisma, CI/CD e deploy documentado.

**Stack**

- **Next.js 16.2.6** — App Router, React Server Components; `force-dynamic` onde o conteúdo depende do CMS.
- **React 19**
- **Tailwind v4** — `@import "tailwindcss"`, `@theme inline`, `@tailwindcss/postcss`
- **shadcn/ui** + utilitários Tailwind
- **Framer Motion 12** — entradas, carrossel, respeito a `prefers-reduced-motion`
- **Payload CMS 3.84** — `@payloadcms/db-postgres`, `@payloadcms/richtext-lexical`, `@payloadcms/translations` (**PT-BR**)
- **PostgreSQL 16** — Docker local na porta **5433**
- **Prisma 6** — modelo `StaffAccount` (área `/equipe`)
- **NextAuth 5 beta** — Credentials + JWT
- **sharp** — pipeline de imagens + remoção de fundo do logo
- **Tipografia** — **Outfit**, **Geist**, **Geist Mono**, **Instrument Serif** (todas via `next/font/google`)

---

### Focux — API (SaaS multi-tenant · personal trainers)

**Escopo:** REST multi-tenant com segregação por `personal_id` derivado do JWT; segurança por método; domínios de negócio (alunos, treinos, financeiro, CRM, alertas, chat, feed, IA); deploy contínuo.

**Stack**

- **Java 21** · **Spring Boot 3.4.4** · **Gradle**
- **PostgreSQL** · **Flyway** (`flyway-database-postgresql`)
- **Spring ecosystem** — Web, Data JPA, **Security** (`@EnableMethodSecurity`), Validation, Mail, **WebSocket**, **Actuator**, **Cache** (Caffeine)
- **JWT** — jjwt **0.12.5** (api / impl / jackson)
- **Pagamentos** — Mercado Pago Java SDK **2.1.7** (PIX, preferências, webhooks)
- **Mídia** — Cloudinary HTTP client
- **Push** — Firebase Admin **9.4.1**
- **Realtime** — STOMP sobre Spring WebSocket
- **IA** — Claude API (Anthropic)
- **Contratos & DX** — Springdoc OpenAPI **2.7.0** (Swagger UI)
- **Confiabilidade** — Resilience4j **2.2.0**, Shedlock (**jdbc-template**), Micrometer **Tracing (Brave)** + registry **Prometheus**
- **Deploy** — **Railway** · CI/CD na branch `master`

---

### Focux — App mobile

**Escopo:** cliente Flutter com dois perfis (**Personal** e **Aluno**), navegação declarativa, consumo da API com JWT, realtime, push e módulos de produto (financeiro, CRM, chat, IA, mídia).

**Stack**

- **Flutter 3.29.3** · **Dart** (`sdk: ^3.7.2`)
- **Estado** — `flutter_riverpod`
- **Rotas** — `go_router`
- **HTTP** — `dio` (cliente + interceptor JWT)
- **Armazenamento** — `flutter_secure_storage` · `shared_preferences` (web)
- **Realtime** — `stomp_dart_client` (STOMP)
- **Push** — `firebase_messaging`
- **UI & conteúdo** — `flutter_markdown` · `video_player` · `fl_chart`
- **Documentos** — `pdf` · `printing`
- **Distribuição** — pipeline Android (`appbundle` → Play Console), estrutura iOS no projeto

<br/>

---

<div align="center">

<img height="170" src="https://github-readme-stats.vercel.app/api?username=devmatheus1912&show_icons=true&hide_border=true&include_all_commits=true&rank_icon=github&bg_color=0d1117&title_color=e2e8f0&icon_color=38bdf8&text_color=cfd8e3&border_radius=10" alt="Estatísticas do GitHub" />
<img height="170" src="https://github-readme-stats.vercel.app/api/top-langs/?username=devmatheus1912&layout=compact&hide_border=true&langs_count=8&bg_color=0d1117&title_color=e2e8f0&text_color=cfd8e3&border_radius=10" alt="Linguagens mais usadas" />

<img src="https://streak-stats.demolab.com?user=devmatheus1912&hide_border=true&border_radius=10&background=0D1117&stroke=334155&ring=38BDF8&fire=F97316&currStreakLabel=E2E8F0&sideLabels=E2E8F0&currStreakNum=FFFFFF&sideNums=CFE1FF&dates=94A3B8" alt="Sequência de contribuições no GitHub" />

![](https://komarev.com/ghpvc/?username=devmatheus1912&color=334155&style=flat-square&label=Visitas)

</div>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://capsule-render.vercel.app/api?type=waving&color=0:0f172a,100:020617&height=90&section=footer">
  <img alt="" src="https://capsule-render.vercel.app/api?type=waving&color=0:e2e8f0,100:f8fafc&height=90&section=footer">
</picture>
