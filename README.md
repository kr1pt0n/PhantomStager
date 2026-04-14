# 🧠 PHANTOM STAGER

> Plataforma de laboratorio para generación, análisis y compilación de payloads en entornos controlados de Red Team.

---

## 🚀 Descripción

**Phantom Stager** es una aplicación web desarrollada en Flask que permite:

* Generar payloads en PowerShell
* Aplicar técnicas de ofuscación (Base64)
* Simular evasión (AMSI patch + delay)
* Compilar stagers a múltiples formatos:

  * `.exe` (C# + Mono)
  * `.bat`
  * `.js`
    
---

## 🖥️ Vista general

Interfaz estilo cyber/dashboard con:

* 🔹 Motor de compilación
* 🔹 Generador de payloads
* 🔹 Checklist de ejecución (RT_CHECKLIST)
* 🔹 Consola de salida

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
git clone https://github.com/kr1pt0n/PhantomStager.git
cd PhantomStager
```

---

### 2. Instalar dependencias

```bash
sudo apt install python3-flask -y
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
chmod +x app.py
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
