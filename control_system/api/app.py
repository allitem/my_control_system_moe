from flask import Flask, request, jsonify
from control_system.controller import run_pipeline_version
from control_system.reports.export_report import export_pdf, export_excel
app = Flask(__name__)
@app.route("/run_pipeline", methods=["POST"])
def run_pipeline():
    data = request.json
    repo = data.get("repo")
    version = data.get("version", "default")
    result = run_pipeline_version(repo, version)
    return jsonify(result)
@app.route("/export_report", methods=["POST"])
def export_report_api():
    data = request.json
    repo = data.get("repo")
    report_type = data.get("type", "pdf")
    out_file = f"reports/{repo}_report.{report_type}"
    if report_type == "pdf":
        export_pdf(repo, "reports", out_file)
    else:
        export_excel(repo, "reports", out_file)
    return jsonify({"status": "exported", "file": out_file})
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
