# PRD — Wiki personal para aprender Django

## Problema y objetivo

La persona propietaria necesita un lugar vivo donde guardar lo que aprende sobre Django y, al mismo tiempo, pueda leer un ejemplo completo de una aplicación Django. El objetivo es que el repositorio sea simultáneamente producto, cuaderno y material de estudio.

## Alcance de la primera versión

Incluye una wiki privada de un solo propietario, notas en Markdown, categorías, etiquetas, dificultad, orden de aprendizaje, búsqueda, autenticación, una interfaz HTML y una API REST documentada. No incluye colaboración, comentarios, notificaciones, ejercicios interactivos ni despliegue productivo.

## Arquitectura

`learning` es el dominio: `Note`, `Category` y `Tag`. `web` es la superficie HTML: templates, formularios y vistas. `webapi` es la superficie JSON: serializers, permisos, viewsets y routers. Ninguna superficie reutiliza archivos de presentación de la otra. `config` contiene settings y URLs raíz.

## Datos y permisos

Un apunte tiene título, slug, resumen, Markdown original, HTML sanitizado, estado, categoría, etiquetas, dificultad y posición. Los visitantes leen apuntes publicados. El usuario propietario autenticado crea y edita; la API permite escritura únicamente a un usuario autenticado y con permisos de staff.

## Validaciones y riesgos

- El Markdown se transforma y limpia con una lista explícita de etiquetas y protocolos seguros.
- Los slugs, categorías y etiquetas son únicos.
- Las categorías usadas por apuntes no se eliminan accidentalmente (`PROTECT`).
- PostgreSQL local puede levantarse con Docker Compose, pero una base administrada puede configurarse mediante `DATABASE_URL`. Esta URL tiene prioridad sobre las variables `POSTGRES_*` individuales; las credenciales viven en `.env`, nunca en Git.

## Evolución posible

Multiusuario, historial de versiones, progreso por lección, tests interactivos, búsqueda full-text de PostgreSQL y despliegue con variables secretas gestionadas.
