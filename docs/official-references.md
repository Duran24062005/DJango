# Referencias oficiales

Estas son las fuentes primarias recomendadas para continuar estudiando. La guía del proyecto explica el concepto con ejemplos locales; la documentación oficial explica el comportamiento completo de Django y sus APIs.

## Django

- [Documentación general de Django 5.2](https://docs.djangoproject.com/en/5.2/) — índice principal, tutoriales, guías y referencias.
- [Instalación](https://docs.djangoproject.com/en/5.2/intro/install/) — Python, entornos virtuales y verificación de la instalación.
- [Crear un proyecto y una aplicación](https://docs.djangoproject.com/en/5.2/intro/tutorial01/) — estructura inicial, `startproject`, `startapp`, URLs y servidor.
- [Modelos y admin](https://docs.djangoproject.com/en/5.2/intro/tutorial02/) — modelos, migraciones, base de datos y panel administrativo.
- [Modelos](https://docs.djangoproject.com/en/5.2/topics/db/models/) — campos, relaciones y opciones de los modelos.
- [QuerySets](https://docs.djangoproject.com/en/5.2/topics/db/queries/) — consultas, filtros, relaciones y ordenamiento con el ORM.
- [Migraciones](https://docs.djangoproject.com/en/5.2/topics/migrations/) — cómo Django versiona y aplica cambios de esquema.
- [URLconfs](https://docs.djangoproject.com/en/5.2/topics/http/urls/) — cómo Django encuentra la vista que responde a una URL.
- [Vistas](https://docs.djangoproject.com/en/5.2/topics/http/views/) — funciones, respuestas HTTP y vistas basadas en clases.
- [Vistas genéricas](https://docs.djangoproject.com/en/5.2/topics/class-based-views/) — `ListView`, `DetailView`, formularios y mixins.
- [Templates](https://docs.djangoproject.com/en/5.2/topics/templates/) — contexto, herencia, etiquetas, filtros y motores de templates.
- [Formularios](https://docs.djangoproject.com/en/5.2/topics/forms/) — validación, `Form`, `ModelForm` y procesamiento de datos.
- [Autenticación](https://docs.djangoproject.com/en/5.2/topics/auth/) — usuarios, sesiones, login, logout y permisos.
- [Protección CSRF](https://docs.djangoproject.com/en/5.2/ref/csrf/) — por qué se protegen los formularios que modifican datos.
- [Pruebas](https://docs.djangoproject.com/en/5.2/topics/testing/overview/) — `TestCase`, cliente de pruebas y ejecución de tests.
- [Archivos estáticos](https://docs.djangoproject.com/en/5.2/howto/static-files/) — `STATIC_URL`, `collectstatic` y despliegue.
- [Checklist de despliegue](https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/) — comprobaciones de seguridad antes de producción.

## Django REST Framework

- [Guía oficial de Django REST Framework](https://www.django-rest-framework.org/) — introducción y tutorial.
- [Serializers](https://www.django-rest-framework.org/api-guide/serializers/) — representación y validación de datos.
- [ViewSets](https://www.django-rest-framework.org/api-guide/viewsets/) — agrupar operaciones de un recurso.
- [Routers](https://www.django-rest-framework.org/api-guide/routers/) — generar rutas consistentes para ViewSets.
- [Permisos](https://www.django-rest-framework.org/api-guide/permissions/) — controlar quién puede leer o modificar recursos.
- [Filtros y búsqueda](https://www.django-rest-framework.org/api-guide/filtering/) — búsqueda, filtros y ordenamiento.

## Cómo usar estas referencias

1. Lee primero el apunte correspondiente de la wiki.
2. Abre la guía oficial enlazada y compara la terminología.
3. Prueba el ejemplo en este repositorio.
4. Registra en un nuevo apunte qué diferencia encontraste entre el ejemplo mínimo y la documentación completa.

