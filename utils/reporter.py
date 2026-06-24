import json
from datetime import datetime


def generate_report(results, output_path, fmt="txt"):
    if fmt == "json":
        with open(output_path, "w") as f:
            json.dump(results, f, indent=2, default=str)
    else:
        with open(output_path, "w") as f:
            f.write("=" * 60 + "\n")
            f.write(f"  ReconX Scan Report\n")
            f.write(f"  Target  : {results.get('target', 'N/A')}\n")
            f.write(f"  Time    : {results.get('scan_time', 'N/A')}\n")
            f.write("=" * 60 + "\n\n")

            for module, data in results.get("modules", {}).items():
                f.write(f"\n[{module.upper()}]\n")
                f.write("-" * 40 + "\n")
                if isinstance(data, dict):
                    for k, v in data.items():
                        f.write(f"  {k}: {v}\n")
                elif isinstance(data, list):
                    for item in data:
                        f.write(f"  - {item}\n")
                else:
                    f.write(f"  {data}\n")
