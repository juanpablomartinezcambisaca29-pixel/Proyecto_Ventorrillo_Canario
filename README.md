# Ventorrillo Canario — Sistema de Gestión

Este proyecto es una aplicación web profesional tipo CRUD (Crear, Leer, Actualizar, Borrar) diseñada para la gestión integral del restaurante **Ventorrillo Canario**. 

## 🌐 Acceso Público (Demo en Vivo)
La aplicación está desplegada actualmente y es accesible desde cualquier lugar a través del siguiente túnel seguro:
- **URL:** [https://unpadded-poison-pod.ngrok-free.dev](https://unpadded-poison-pod.ngrok-free.dev)

---

## 🛠️ Tecnologías Utilizadas
- **Backend:** Python 3 con el micro-framework **Flask**.
- **Base de Datos:** **MariaDB** (MySQL).
- **Frontend:** HTML5, CSS3 y **Bootstrap 5** para un diseño responsivo.
- **Túnel de Red:** **ngrok** (utilizado para hacer la web pública saltando el CG-NAT del router).

---

## 🏗️ Infraestructura y Despliegue
El sistema funciona en una arquitectura distribuida de dos servidores (Máquinas Virtuales con Debian):

1. **Servidor de Base de Datos (VM1):** - IP Local: `192.168.1.214`
   - Gestiona toda la persistencia de datos de forma independiente.
2. **Servidor Web (VM2):** - IP Local: `192.168.1.215`
   - Aloja la lógica de Flask y sirve los archivos estáticos (imágenes y estilos).

---

## 📊 Base de Datos
El repositorio incluye el archivo `ventorrillo_canario.sql` con la estructura completa de las tablas:
- **Categorías:** Clasificación de los productos.
- **Platos:** Información detallada del menú.
- **Mesas:** Gestión del estado de las mesas del local.
- **Pedidos:** Registro de las comandas realizadas.

---

## 🚀 Instalación Local
Si deseas clonar este proyecto en tu entorno local:

1. **Clonar el repositorio:**
   ```bash
   git clone [https://github.com/TU_USUARIO/ventorrillo-canario.git](https://github.com/TU_USUARIO/ventorrillo-canario.git)
