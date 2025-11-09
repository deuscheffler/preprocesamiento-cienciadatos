Autor: Jefferson Sandoval — Universidad Nacional de Chimborazo
Usuario GitHub: deuscheffler

# 1. Introducción
## Objetivo del proyecto

El objetivo de este proyecto es desarrollar un flujo completo de preprocesamiento de datos como parte de la asignatura de Ciencia de Datos, implementando técnicas de limpieza, transformación y normalización de conjuntos de datos.

Además, se busca fortalecer el uso de Git y GitHub como herramientas de control de versiones y trabajo colaborativo, incluyendo la automatización mediante GitHub Actions.

## Funcionalidades implementadas

Archivo preprocesamiento.py: Implementa funciones para limpiar, codificar y escalar datos.

Control de versiones Git:

Creación del repositorio en GitHub.

Manejo de ramas (feature-preprocesamiento).

Commit y push de los cambios.

Integración y despliegue continuo:
Configuración de un flujo automatizado mediante GitHub Actions para verificar el código en cada actualización.

# 2. Comandos Git usados

## Comando	Descripción

git clone https://github.com/deuscheffler/preprocesamiento-cienciadatos.git	    *Clona el repositorio desde GitHub al entorno local.*

git config --global user.name "deuscheffler"	    *Configura el nombre de usuario en Git.*

git config --global user.email "jefferson.sandoval@unach.edu.ec"

<img width="580" height="379" alt="image" src="https://github.com/user-attachments/assets/cdc7bc27-e246-483d-84e2-42a558a4d602" />

git checkout -b feature-preprocesamiento	*Crea y cambia a una nueva rama de desarrollo.*

git add scripts/preprocesamiento.py	*Agrega el nuevo archivo al área de preparación.*

git commit -m "Agregar script de preprocesamiento con funciones básicas"

<img width="582" height="374" alt="image" src="https://github.com/user-attachments/assets/9ab3496f-8677-4d4f-9870-3c50eb2d5bdd" />

git checkout main	*Cambia a la rama principal.*

git pull origin main	*Actualiza la rama principal con los cambios fusionados.*

git branch -d feature-preprocesamiento	*Elimina la rama local después de la fusión.*

<img width="581" height="550" alt="image" src="https://github.com/user-attachments/assets/5fec9b3f-bd78-4a08-a159-7295778486fb" />




