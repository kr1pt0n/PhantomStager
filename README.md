# 🧠 PHANTOM STAGER LAB

> Plataforma de laboratorio para generación, análisis y compilación de payloads en entornos controlados de Red Team.

---

## 🚀 Descripción

**Phantom Stager Lab** es una aplicación web desarrollada en Flask que permite:

* Generar payloads en PowerShell
* Aplicar técnicas de ofuscación (Base64)
* Simular evasión (AMSI patch + delay)
* Compilar stagers a múltiples formatos:

  * `.exe` (C# + Mono)
  * `.bat`
  * `.js`
* Visualizar estado en tiempo real desde un panel tipo dashboard

---

## 🖥️ Vista general

Interfaz estilo cyber/dashboard con:

* 🔹 Motor de compilación
* 🔹 Generador de payloads
* 🔹 Checklist de ejecución (RT_CHECKLIST)
* 🔹 Consola de salida
* 🔹 Panel dinámico de sistema (`/api/info`)

---

## ⚙️ Tecnologías utilizadas

### Backend

* Python 3
* Flask

### Frontend

* HTML5
* CSS3 (custom cyber UI)
* JavaScript (vanilla)

### Compilación

* Mono (`mcs`) para generación de ejecutables `.exe`

---

## 📦 Instalación

### 1. Clonar repositorio

```bash
git clone https://github.com/tu-usuario/phantom-stager.git
cd phantom-stager
```

---

### 2. Instalar dependencias

```bash
pip install flask
```

---

### 3. Instalar Mono (para EXE)

```bash
sudo apt update
sudo apt install mono-mcs -y
```

---

## ▶️ Ejecución

```bash
python3 app.py
```

Luego abrir:

```
http://127.0.0.1:5000
```

---

## 🧩 Estructura del proyecto

```
phantom-stager/
│
├── app.py
├── templates/
│   └── index.html
├── static/
│   └── favicon.ico
└── README.md
```

---

## 🔌 API interna

### `GET /api/info`

Devuelve información simulada del sistema:

```json
{
  "ip": "192.168.x.x",
  "port": 4443,
  "os": "Linux",
  "time": "12:00:00",
  "cpu": 45,
  "ram": 60
}
```

---

## ⚠️ Nota importante

Este proyecto está diseñado exclusivamente para:

* 🔬 Entornos de laboratorio
* 🧪 Pruebas controladas
* 🎓 Aprendizaje en ciberseguridad ofensiva

**NO debe utilizarse en sistemas sin autorización.**

---

## 🧠 Roadmap (futuro)

* [ ] Migración a WebSockets (tiempo real real)
* [ ] Panel multi-sesión
* [ ] Control de clientes
* [ ] Logs avanzados
* [ ] Arquitectura tipo C2

---

## 👨‍💻 Autor

**kr1pt0n**

> desarrollado por kr1pt0n

---

## 📜 Licencia

Uso educativo y de investigación.

---
