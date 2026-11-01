"""
Web-to-Desktop Data Bridge (Core Companion Server)
Generic, scalable local service that receives structured payloads from browser extensions
and persists them into formatted Excel/CSV datasets.
"""
import os
import logging
from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("DataBridge")

app = Flask(__name__)
CORS(app)  # Permite requisicoes da extensao web local

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
EXPORT_DIR = os.environ.get("BRIDGE_EXPORT_DIR", os.path.join(BASE_DIR, "exports"))
os.makedirs(EXPORT_DIR, exist_ok=True)


class DataExporter:
    """Modulo escalavel para exportacao e append de dados estruturados."""

    @staticmethod
    def append_records(collection_name: str, records: list) -> str:
        if not collection_name.replace("_", "").isalnum():
            raise ValueError("Nome de colecao invalido.")

        target_file = os.path.join(EXPORT_DIR, f"{collection_name}.xlsx")
        new_df = pd.DataFrame(records)

        if os.path.exists(target_file):
            try:
                existing_df = pd.read_excel(target_file)
                combined_df = pd.concat([existing_df, new_df], ignore_index=True)
            except Exception as e:
                logger.warning(f"Erro ao ler arquivo existente ({e}), criando novo dataframe.")
                combined_df = new_df
        else:
            combined_df = new_df

        combined_df.to_excel(target_file, index=False)
        logger.info(f"Gravados {len(records)} registros em: {target_file}")
        return target_file


@app.route("/api/v1/health", methods=["GET"])
def health_check():
    """Endpoint de checagem de conexao para a extensao."""
    return jsonify({"status": "online", "version": "1.0.0"})


@app.route("/api/v1/export", methods=["POST"])
def export_data():
    """
    Endpoint generico de exportacao.
    Espera JSON:
    {
        "collection": "nome_do_dataset",
        "records": [ { "col1": "val1", "col2": "val2" }, ... ]
    }
    """
    payload = request.get_json(silent=True)
    if not payload:
        return jsonify({"error": "Payload JSON invalido ou ausente."}), 400

    collection = payload.get("collection", "dados_exportados")
    records = payload.get("records", [])

    if not isinstance(records, list) or len(records) == 0:
        return jsonify({"error": "Campo 'records' deve ser uma lista nao-vazia."}), 400

    try:
        saved_path = DataExporter.append_records(collection, records)
        return jsonify({
            "status": "success",
            "message": f"{len(records)} registros exportados com sucesso.",
            "file": os.path.basename(saved_path)
        }), 200
    except Exception as exc:
        logger.error(f"Falha ao exportar registros: {exc}")
        return jsonify({"error": str(exc)}), 500


if __name__ == "__main__":
    port = int(os.environ.get("BRIDGE_PORT", 5000))
    logger.info(f"Servidor Bridge inicializado em http://localhost:{port}")
    app.run(host="127.0.0.1", port=port, debug=False)
