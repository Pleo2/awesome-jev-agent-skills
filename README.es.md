# JevScope — Skills de IA para revisión de código y pruebas

**Revisiones más precisas. Evidencia más sólida.**

JevScope es una colección open source de cinco skills para agentes de programación: revisión de código, cobertura de escenarios de prueba, diagnóstico de errores, validación de datos extraídos y verificación de evidencia de QA. Utiliza TypeSafe Jev para aportar evaluaciones semánticas que el agente contrasta con código y pruebas.

[English documentation](README.md) · [Licencia MIT](LICENSE) · [Contribuir](CONTRIBUTING.md)

## Instalación

```sh
npx skills add Pleo2/jevscope --skill jev-test-coverage
```

Selecciona tu agente cuando lo solicite el instalador. Omite `--skill` para elegir las skills de forma interactiva. Cada skill incluye instrucciones en inglés, ejemplos sintéticos y un cliente Python independiente.

## Skills disponibles

| Skill | Uso |
| --- | --- |
| [jev-diagnose-failures](skills/jev-diagnose-failures/SKILL.md) | Priorizar qué investigar ante logs y pruebas fallidas |
| [jev-test-coverage](skills/jev-test-coverage/SKILL.md) | Comparar criterios de aceptación con assertions reales |
| [jev-review-diff](skills/jev-review-diff/SKILL.md) | Revisar cambios contra reglas explícitas del código |
| [jev-extraction-review](skills/jev-extraction-review/SKILL.md) | Contrastar campos extraídos con textos y documentos |
| [jev-qa-evidence](skills/jev-qa-evidence/SKILL.md) | Revisar si la evidencia respalda una afirmación de QA |

## Ejemplo de uso

Pide a tu agente: “Usa jev-test-coverage para identificar qué criterios de aceptación no están cubiertos por estas pruebas y confirma los huecos leyendo las assertions”.

Para consultas reales necesitas Python 3.9 o superior y una clave de TypeSafe en `TYPESAFE_API_KEY`. Las consultas pueden tener costo; la validación local y CI no llaman a la API. Consulta los [comandos y la configuración](README.md#use).

Las respuestas de Jev son apoyo para la revisión. No sustituyen pruebas ejecutadas, análisis estático ni comprobaciones independientes. El proyecto es de propósito general y no está vinculado oficialmente a TypeSafe.
