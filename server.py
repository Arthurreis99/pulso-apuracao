#!/usr/bin/env python3
"""Servidor local mínimo para o painel Pulso, com proxy limitado ao JSON oficial do TSE."""
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen
from pathlib import Path
import json
import os

BASE_DIR = Path(__file__).resolve().parent
OFFICIAL_URL = (
    "https://resultados.tse.jus.br/oficial/ele2026/6258/dados/br/"
    "br-c0001-e006258-u.json"
)
HOST = "127.0.0.1"
PORT = 8000

class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(BASE_DIR), **kwargs)

    def do_GET(self):
        if self.path.split("?", 1)[0] == "/api/apuracao":
            self._proxy_results()
            return
        if self.path.split("?", 1)[0] == "/":
            self.path = "/index.html"
        return super().do_GET()

    def _proxy_results(self):
        req = Request(
            OFFICIAL_URL,
            headers={
                "User-Agent": "PulsoPainel/1.0 (consulta de arquivo publico do TSE)",
                "Accept": "application/json",
                "Cache-Control": "no-cache",
                "Pragma": "no-cache",
            },
            method="GET",
        )
        try:
            with urlopen(req, timeout=15) as response:
                body = response.read()
                # Validar JSON antes de encaminhar ao navegador.
                json.loads(body.decode("utf-8-sig"))
                self.send_response(200)
                self.send_header("Content-Type", "application/json; charset=utf-8")
                self.send_header("Cache-Control", "no-store, max-age=0")
                self.send_header("Pragma", "no-cache")
                self.send_header("Content-Length", str(len(body)))
                self.end_headers()
                self.wfile.write(body)
        except HTTPError as exc:
            self._json_error(502, f"O servidor do TSE respondeu com HTTP {exc.code}.")
        except URLError:
            self._json_error(502, "Não foi possível conectar ao servidor do TSE. Verifique a conexão com a internet.")
        except TimeoutError:
            self._json_error(504, "A consulta ao TSE demorou mais do que o esperado. Tente novamente.")
        except (ValueError, UnicodeDecodeError, json.JSONDecodeError):
            self._json_error(502, "A resposta recebida da fonte oficial não pôde ser interpretada como JSON.")
        except Exception:
            self._json_error(502, "Erro inesperado ao consultar a fonte oficial do TSE.")

    def _json_error(self, status, message):
        body = json.dumps({"error": message}, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Cache-Control", "no-store, max-age=0")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, fmt, *args):
        # Log simples no terminal, sem dados pessoais do usuário.
        super().log_message(fmt, *args)

if __name__ == "__main__":
    os.chdir(BASE_DIR)
    server = ThreadingHTTPServer((HOST, PORT), Handler)
    print("\nPulso — painel de apuração presidencial")
    print(f"Abra no navegador: http://{HOST}:{PORT}")
    print("Fonte: arquivos públicos do TSE; atualização automática a cada 30 segundos.")
    print("Para encerrar, pressione Ctrl+C.\n")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nServidor encerrado.")
    finally:
        server.server_close()
