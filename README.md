# Examen de selección

## Introducción a la kata

Por favor lee la siguiente nota:
- [Códigos de cuatro letras para las aves](https://islasgeci.github.io/2020/08/06/kata)

## Instrucciones

Debes crear una aplicación de cualquier tipo que reciba el nombre común de un ave y devuelva el
código de cuatro letras correspondiente. Esperamos ver avances graduales en ciclos cortos. Nos
gustaría que la aplicación la desarrolles con varios _pull requests_ y que cada _pull request_ tenga
un avance pequeño. Por lo que te proponemos: 

1. Crea un
   [_fork_](https://docs.github.com/en/github/getting-started-with-github/fork-a-repo#fork-an-example-repository)
   del repositorio `https://github.com/IslasGECI/kata_flbc_jesus1497`
1. Cubre tu código con pruebas
1. Haz pasar GitHub Actions (necesitarás agregar un `Makefile` y un `Dockerfile`)
1. Haz múltiples _pull requests_ pequeños 
1. Usa GitHub (_issues_ y _pull requests_) como el medio de comunicación principal

Por favor no esperes a que la aplicación esté terminada para someter tu primer _pull request_.
Recuerda que no podrás crear ningún _pull request_ hasta que tengas tu
[_fork_](https://docs.github.com/en/github/getting-started-with-github/fork-a-repo#fork-an-example-repository).

## Ejecución de la aplicación

Para revisar la versión final de la aplicación, ejecutaremos una de las siguientes opciones:

Opción 1:

```
git clone https://github.com/IslasGECI/kata_flbc_jesus1497.git
cd kata_flbc_jesus1497
docker build --tag islasgeci .
docker run islasgeci make run
```

Opción 2:

```
git clone https://github.com/IslasGECI/kata_flbc_jesus1497.git
cd kata_flbc_jesus1497
docker-compose up
```

Tú puedes elegir cualquiera de las dos opciones anteriores que prefieras.

## Rúbrica

El objetivo de este examen de selección es evaluar las habilidades para el trabajo colaborativo a
distancia. Para eso usaremos los siguientes rubros:

- **Capacidad para el trabajo remoto y colaborativo**: 
  - [ ] Uso de Git  (Los mensajes son informativos del porqué, las consignaciones son pequeñas y los
    nombres de las ramas dan información del objetivo de los cambios)
  - [ ] Habilidades de comunicación mediante GitHub (_issues_ y _pull requests_: La comunicación es
    amable, la descripción es clara y da formato utilizando _Markdown_)
  - [ ] Solicitud de revisiones (Utilización de [las
    características](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/requesting-a-pull-request-review)
    de GitHub para indicar que terminó una corrección y que está solicitando una nueva revisión)
  - [ ] Asimilación de retroalimentación (Las correcciones solicitadas en un _pull request_ ya no se
    repiten en los siguientes _pull requets_)

- **Buenas prácticas en programación**: 
  - [ ] Refactorización
  - [ ] Principios de diseño de software
  - [ ] Pruebas unitarias

- **Automatización y reproducibilidad**: 
  - [ ] Uso de GitHub Actions
  - [ ] Uso de Docker
  - [ ] Uso de Make
  - [ ] Principios ágiles y de DevOps

## Sugerencias

- Crea _pull request_ pequeños; un _pull request_ de 100 líneas podría ser demasiado grande.
- Se amable, explica el porqué de las cosas, respeta nuestro [código de
  conducta](https://islasgeci.github.io/2019/11/06/code-of-conduct), usa lenguaje simple y claro.
- Comunícate mucho y hazlo mediante GitHub.

## Referencias

- [_Forkeado_ de un repositorio](https://docs.github.com/en/github/getting-started-with-github/fork-a-repo)
- [Revisiones en GitHub](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/requesting-a-pull-request-review)
- [`Makefile` mínimo](http://kbroman.org/minimal_make/)
- [Buenas prácticas en `Dockerfile`](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/)
