<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://capsule-render.vercel.app/api?type=soft&color=0:020617,100:0f172a&height=120&section=header&text=Matheus%20Oliveira&fontSize=40&fontColor=f8fafc&fontAlignY=55&fontAlign=28&desc=Full%20Stack%20%E2%80%94%20Java%20%C2%B7%20Next.js%20%C2%B7%20Flutter&descAlignY=75&descAlign=28&descSize=13&descColor=64748b">
  <img alt="Matheus Oliveira dos Santos" src="https://capsule-render.vercel.app/api?type=soft&color=0:f8fafc,100:f1f5f9&height=120&section=header&text=Matheus%20Oliveira&fontSize=40&fontColor=0f172a&fontAlignY=55&fontAlign=28&desc=Full%20Stack%20%E2%80%94%20Java%20%C2%B7%20Next.js%20%C2%B7%20Flutter&descAlignY=75&descAlign=28&descSize=13&descColor=475569">
</picture>

<br/>

<p>
  APIs robustas em Java/Spring, produtos web em Next.js e apps Flutter —<br/>
  com PostgreSQL, segurança bem definida e integrações reais em produção.
</p>

<p>
  <a href="https://www.linkedin.com/in/matheusoliveiradosantos/"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=flat-square&logo=linkedin&logoColor=white"/></a>&nbsp;
  <a href="https://www.instagram.com/devmatheusbb"><img src="https://img.shields.io/badge/Instagram-E4405F?style=flat-square&logo=instagram&logoColor=white"/></a>&nbsp;
  <a href="mailto:matheusos1912@icloud.com"><img src="https://img.shields.io/badge/E--mail-EA4335?style=flat-square&logo=gmail&logoColor=white"/></a>&nbsp;
  <img src="https://komarev.com/ghpvc/?username=devmatheus1912&color=64748b&style=flat-square&label=visitas"/>
</p>

<br/>

---

## Faculdade Goiás

> Site institucional de alta conversão · CMS headless · Área da equipe

Marketing acadêmico com Payload CMS 3 em PT-BR, páginas ricas de curso, painel de credenciamento e-MEC gerado server-side, rastreamento UTM preservado, CI/CD documentado e deploy em Vercel + Neon.

<table>
<tr><td><b>Camada</b></td><td><b>Tecnologia</b></td></tr>
<tr><td>Framework</td><td>Next.js 15 · App Router · React Server Components · <code>force-dynamic</code></td></tr>
<tr><td>UI</td><td>React 19 · Tailwind v4 · shadcn/ui · Framer Motion 12</td></tr>
<tr><td>CMS</td><td>Payload CMS 3.84 · Lexical · db-postgres · translations PT-BR</td></tr>
<tr><td>Auth</td><td>NextAuth 5 beta (Credentials + JWT) · Prisma 6 (<code>StaffAccount</code>)</td></tr>
<tr><td>Banco</td><td>PostgreSQL 16 — dois schemas isolados (CMS / staff)</td></tr>
<tr><td>Mídia</td><td>sharp · Vercel Blob · imageSizes WebP automático</td></tr>
<tr><td>Deploy</td><td>Vercel · Neon · GitHub Actions (migrate → lint → build)</td></tr>
<tr><td>Tipografia</td><td>Outfit · Geist · Geist Mono · Instrument Serif</td></tr>
</table>

<br/>

---

## Focux — API

> SaaS multi-tenant · Personal trainers · Produção no Railway

REST multi-tenant com segregação por `personal_id` derivado do JWT; domínios de negócio completos (alunos, treinos, financeiro, CRM, alertas, chat, feed, IA); confiabilidade com circuit breaker, lock distribuído e tracing.

<table>
<tr><td><b>Camada</b></td><td><b>Tecnologia</b></td></tr>
<tr><td>Core</td><td>Java 21 · Spring Boot 3.4.4 · Gradle</td></tr>
<tr><td>Segurança</td><td>Spring Security · <code>@EnableMethodSecurity</code> · jjwt 0.12.5</td></tr>
<tr><td>Banco</td><td>PostgreSQL · Spring Data JPA · Flyway</td></tr>
<tr><td>Pagamentos</td><td>Mercado Pago SDK 2.1.7 — PIX, preferências, webhooks</td></tr>
<tr><td>Realtime</td><td>STOMP sobre Spring WebSocket</td></tr>
<tr><td>Push</td><td>Firebase Admin 9.4.1</td></tr>
<tr><td>Mídia</td><td>Cloudinary HTTP client</td></tr>
<tr><td>IA</td><td>Claude API (Anthropic)</td></tr>
<tr><td>Contratos</td><td>Springdoc OpenAPI 2.7.0 · Swagger UI</td></tr>
<tr><td>Confiabilidade</td><td>Resilience4j 2.2.0 · Shedlock (jdbc-template) · Micrometer Tracing (Brave) · Prometheus</td></tr>
<tr><td>Deploy</td><td>Railway · CI/CD na branch <code>master</code></td></tr>
</table>

<br/>

---

## Focux — App Mobile

> Cliente Flutter · Dois perfis · Android em produção

Cliente com perfis Personal e Aluno, navegação declarativa, consumo da API com JWT, realtime via STOMP, push Firebase e módulos completos de produto.

<table>
<tr><td><b>Camada</b></td><td><b>Tecnologia</b></td></tr>
<tr><td>Core</td><td>Flutter 3.29.3 · Dart sdk ^3.7.2</td></tr>
<tr><td>Estado</td><td>flutter_riverpod</td></tr>
<tr><td>Navegação</td><td>go_router</td></tr>
<tr><td>HTTP</td><td>dio · interceptor JWT</td></tr>
<tr><td>Armazenamento</td><td>flutter_secure_storage · shared_preferences</td></tr>
<tr><td>Realtime</td><td>stomp_dart_client</td></tr>
<tr><td>Push</td><td>firebase_messaging</td></tr>
<tr><td>UI & conteúdo</td><td>flutter_markdown · video_player · fl_chart</td></tr>
<tr><td>Documentos</td><td>pdf · printing</td></tr>
<tr><td>Distribuição</td><td>appbundle → Play Console · estrutura iOS no projeto</td></tr>
</table>

<br/>

---

<div align="center">

<img height="165" src="https://github-readme-stats.vercel.app/api?username=devmatheus1912&show_icons=true&hide_border=true&include_all_commits=true&rank_icon=github&bg_color=0d1117&title_color=e2e8f0&icon_color=38bdf8&text_color=cfd8e3&border_radius=8" alt="GitHub stats"/>
&nbsp;&nbsp;
<img height="165" src="https://github-readme-stats.vercel.app/api/top-langs/?username=devmatheus1912&layout=compact&hide_border=true&langs_count=8&bg_color=0d1117&title_color=e2e8f0&text_color=cfd8e3&border_radius=8" alt="Top langs"/>

<br/><br/>

<img src="https://streak-stats.demolab.com?user=devmatheus1912&hide_border=true&border_radius=8&background=0D1117&stroke=1e293b&ring=38BDF8&fire=F97316&currStreakLabel=E2E8F0&sideLabels=94A3B8&currStreakNum=FFFFFF&sideNums=E2E8F0&dates=475569" alt="Streak"/>

</div>

<br/>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://capsule-render.vercel.app/api?type=soft&color=0:0f172a,100:020617&height=60&section=footer">
  <img alt="" src="https://capsule-render.vercel.app/api?type=soft&color=0:f1f5f9,100:f8fafc&height=60&section=footer">
</picture>
