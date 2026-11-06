"""Configuração central. Valores vêm de variáveis de ambiente (ver .env.example)."""

import os
from pathlib import Path

# Execute sempre a partir da raiz do repositório (caminhos relativos a ela).
WAREHOUSE_PATH = Path(os.environ.get("WAREHOUSE_PATH", "warehouse/analytics.duckdb"))
BRONZE_DIR = Path(os.environ.get("BRONZE_DIR", "data/bronze"))
