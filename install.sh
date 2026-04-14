#!/bin/bash

# Colores para la consola
GREEN='\033[0;32m'
CYAN='\033[0;36m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${CYAN}===================================================="
echo -e "      kr1pt0n OFFSEC - INSTALLER (KALI-PARROT-UBUNTU)"
echo -e "====================================================${NC}"

# Verificar si se corre como root
if [[ $EUID -ne 0 ]]; then
   echo -e "${RED}[!] Este script debe ejecutarse con sudo.${NC}"
   exit 1
fi

echo -e "${GREEN}[*] Actualizando repositorios...${NC}"
apt update -y

echo -e "${GREEN}[*] Instalando dependencias del sistema (Mono para EXE)...${NC}"
apt install -y mono-mcs python3 python3-pip

echo -e "${GREEN}[*] Instalando dependencias de Python (Flask)...${NC}"
# Usamos --break-system-packages para versiones nuevas de Kali/Debian
apt install python3-flask

echo -e "${GREEN}[*] Configurando permisos...${NC}"
chmod +x app.py

echo -e "${CYAN}===================================================="
echo -e "      INSTALACIÓN COMPLETADA EXITOSAMENTE"
echo -e "===================================================="
echo -e "Para iniciar la estación de combate corre:"
echo -e "python3 app.py"
echo -e "====================================================${NC}"
