# Desarrollo de una API REST con Autenticación

La empresa necesita una API REST para gestionar productos y usuarios con autenticación. Los productos tienen nombre, precio, stock y categoría. Los usuarios deben poder registrarse, iniciar sesión y acceder a sus datos. La API debe manejar errores como precios negativos y nombres duplicados, y debe ser idempotente para las solicitudes de registro de productos.

## Informacion General

| Campo | Valor |
|-------|-------|
| **Tema** | Python Django REST |
| **Nivel** | junior-l1 |
| **Tipo** | practical |
| **Tiempo estimado** | 10 horas |

## Fases del Reto

### Fase 0: Configuración del Proyecto

**Objetivo:** Obtener el proyecto base funcional enviando el Código Base a un asistente de IA, que lo analizará, corregirá errores y generará un ZIP listo para usar.

**Tiempo estimado:** 15-30 minutos

**Instrucciones:**

- Asegúrate de tener instalado para ejecutar el proyecto: Un IDE o editor de código.
- Copia todo el contenido del campo **Código Base** de este reto — incluyendo el texto de instrucciones que aparece al inicio.
- Abre un asistente de IA (Claude en claude.ai, ChatGPT o Gemini — se recomienda Claude), pega el contenido copiado en el chat y envíalo.
- El asistente analizará los archivos, corregirá errores y generará un archivo ZIP descargable. Descárgalo y extráelo en la carpeta donde quieras trabajar.
- Verifica que el proyecto arranca sin errores.

**Entregable:** El proyecto compila/arranca sin errores.

<details>
<summary>Pistas de conocimiento</summary>

- Copia el Código Base completo incluyendo el texto de instrucciones al inicio — esas instrucciones le indican al asistente exactamente qué hacer con los archivos.
- Si el asistente no genera el ZIP automáticamente al terminar el análisis, escríbele: "genera el ZIP ahora".
- Si el proyecto tiene errores al arrancar, comparte el mensaje de error con el mismo asistente para que lo corrija.

</details>

### Fase 1: Definición de la API y Modelos

**Objetivo:** Definir la estructura básica de la API y los modelos de datos para productos y usuarios.

**Tiempo estimado:** 2 horas

**Instrucciones:**

- Identificar los campos necesarios para los modelos de productos y usuarios.
- Definir las restricciones y validaciones para cada campo (ej. precios positivos, nombres únicos).
- Establecer la relación entre productos y usuarios.

**Entregable:** Modelos de datos definidos y validaciones implementadas.

<details>
<summary>Pistas de conocimiento</summary>

- Considera cómo representar las relaciones entre entidades.
- Piensa en los posibles errores y cómo manejarlos.

</details>

### Fase 2: Implementación de la Autenticación

**Objetivo:** Implementar la autenticación de usuarios en la API.

**Tiempo estimado:** 3 horas

**Instrucciones:**

- Configurar el sistema de autenticación para que los usuarios puedan registrarse e iniciar sesión.
- Asegurar que los usuarios autenticados puedan acceder a sus datos.
- Implementar la idempotencia para las solicitudes de registro de productos.

**Entregable:** Sistema de autenticación funcional con idempotencia en las solicitudes de registro de productos.

<details>
<summary>Pistas de conocimiento</summary>

- Considera cómo almacenar y verificar las credenciales de los usuarios.
- Piensa en cómo manejar las solicitudes idempotentes.

</details>

### Fase 3: Manejo de Errores y Validaciones

**Objetivo:** Mejorar el manejo de errores y validaciones en la API.

**Tiempo estimado:** 2 horas

**Instrucciones:**

- Implementar manejo de errores para las solicitudes de registro y autenticación.
- Asegurar que las validaciones de campos se realicen correctamente.
- Documentar los posibles errores y sus soluciones.

**Entregable:** API con manejo de errores y validaciones mejoradas, y documentación de errores.

<details>
<summary>Pistas de conocimiento</summary>

- Considera cómo comunicar los errores al usuario de manera clara.
- Piensa en cómo documentar los errores para facilitar la resolución.

</details>

### Fase 4: Optimización y Refactorización

**Objetivo:** Optimizar y refactorizar el código de la API.

**Tiempo estimado:** 3 horas

**Instrucciones:**

- Identificar áreas de optimización en el código.
- Refactorizar el código para mejorar su legibilidad y mantenibilidad.
- Asegurar que la API cumpla con los requisitos de rendimiento y escalabilidad.

**Entregable:** Código optimizado y refactorizado, con mejoras en rendimiento y escalabilidad.

<details>
<summary>Pistas de conocimiento</summary>

- Considera cómo mejorar la legibilidad y mantenibilidad del código.
- Piensa en cómo asegurar que la API cumpla con los requisitos de rendimiento y escalabilidad.

</details>

## Dimensiones Evaluadas

- **queEs**: ¿Qué son los modelos de datos y por qué son importantes en una API REST?
- **paraQueSirve**: ¿Para qué sirve la autenticación en una API y cómo se implementa?
- **comoSeUsa**: ¿Cómo se usa la idempotencia en las solicitudes de registro de productos?
- **erroresComunes**: ¿Cuáles son los errores comunes en la implementación de una API REST y cómo se manejan?
- **queDecisionesImplica**: ¿Qué decisiones implica la optimización y refactorización del código de una API?

## Criterios de Evaluacion

- Definición correcta de modelos de datos.
- Implementación funcional de la autenticación.
- Manejo adecuado de errores y validaciones.
- Código optimizado y refactorizado.

---

*Reto generado automaticamente por Challenge Generator - Pragma*
