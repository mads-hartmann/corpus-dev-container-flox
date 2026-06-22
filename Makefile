.PHONY: check run

HOST ?= 0.0.0.0
PORT ?= 8000
PYTHON ?= python3

check:
	$(PYTHON) -m compileall -q app.py scripts/check_http.py
	PYTHONPATH=. $(PYTHON) scripts/check_http.py

run:
	HOST=$(HOST) PORT=$(PORT) $(PYTHON) app.py
