# generate_report.py
# This script generates a Markdown report summarizing the analysis results
import os
import pandas as pd
from analysis_agent import AnalysisAgent

def main():
    # Load the unified dataset (adjust path if needed)
    unified_path = os.path.join("outputs", "unified_dataset_sample.csv")
    df = pd.read_csv(unified_path)

    # Run analysis with your existing agent
    analysis = AnalysisAgent(df)

    lines = []
    total = len(df)
    passed = int(df["pass_flag"].sum())
    failed = int((df["pass_flag"] == False).sum())

    # Pass/Fail summary
    lines.append("# Analysis Report\n")
    lines.append("## Pass/Fail Summary\n")
    lines.append(f"- Total merged rows: {total}")
    lines.append(f"- Passed: {passed} ({(passed/total)*100:.2f}%)")
    lines.append(f"- Failed: {failed} ({(failed/total)*100:.2f}%)")

    # Defects by CMM lots
    if "lot_id_cmm" in df.columns:
        lines.append("\n## Top Defect Lots (CMM)\n")
        defects_cmm = (
            df[df["pass_flag"] == False]
            .groupby("lot_id_cmm")
            .size()
            .reset_index(name="num_defects")
            .sort_values("num_defects", ascending=False)
        )
        if not defects_cmm.empty:
            for row in defects_cmm.head(10).to_dict("records"):
                lines.append(f"- Lot {row['lot_id_cmm']}: {row['num_defects']} defects")
        else:
            lines.append("No CMM lot-level defect aggregation available.")

    # Defects by ERP lots
    if "lot_id_erp" in df.columns:
        lines.append("\n## Top Defect Lots (ERP)\n")
        defects_erp = (
            df[df["pass_flag"] == False]
            .groupby("lot_id_erp")
            .size()
            .reset_index(name="num_defects")
            .sort_values("num_defects", ascending=False)
        )
        if not defects_erp.empty:
            for row in defects_erp.head(10).to_dict("records"):
                lines.append(f"- Lot {row['lot_id_erp']}: {row['num_defects']} defects")
        else:
            lines.append("No ERP lot-level defect aggregation available.")

    # Anomaly detection summary (if column exists)
    if "anomaly_iforest" in df.columns:
        num_anoms = int(df["anomaly_iforest"].sum())
        lines.append("\n## Anomaly Detection\n")
        lines.append(f"- isolationforest: {num_anoms}")

    # Save to Markdown file
    output_path = "analysis_report.md"
    with open(output_path, "w") as f:
        f.write("\n".join(lines))

    print(f"Analysis report generated and saved to {output_path}")

if __name__ == "__main__":
    main()
