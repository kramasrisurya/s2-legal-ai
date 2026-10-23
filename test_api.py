"""
S2 Legal AI Pro - Automated Test Runner
Reads test_queries.json and verifies end-to-end routing against http://127.0.0.1:8000/api/chat.
"""

import json
import sys
import time
from pathlib import Path
import urllib.request
import urllib.error

# Ensure UTF-8 output on Windows terminals
if sys.platform == "win32" and hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

API_URL = "http://127.0.0.1:8000/api/chat"
QUERIES_FILE = Path(__file__).resolve().parent / "test_queries.json"

def run_test_suite():
    if not QUERIES_FILE.exists():
        print(f"[ERROR] Test queries file not found: {QUERIES_FILE}")
        sys.exit(1)

    with open(QUERIES_FILE, "r", encoding="utf-8") as f:
        test_cases = json.load(f)

    print("\n" + "=" * 80)
    print("  S2 LEGAL AI PRO: AUTOMATED ROUTER BENCHMARK TEST SUITE")
    print(f"  Target Endpoint: {API_URL}")
    print(f"  Test Cases Count: {len(test_cases)}")
    print("=" * 80 + "\n")

    passed_count = 0
    failed_count = 0

    for tc in test_cases:
        tc_id = tc["id"]
        tc_name = tc["name"]
        query = tc["query"]
        expected_src = tc["expected_source"]
        min_conf = tc.get("min_expected_confidence", 0.0)

        payload = json.dumps({
            "query": query,
            "role": "advocate",
            "history": []
        }).encode("utf-8")

        req = urllib.request.Request(
            API_URL,
            data=payload,
            headers={"Content-Type": "application/json"}
        )

        start_t = time.time()
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                data = json.loads(resp.read().decode("utf-8"))
                latency_ms = (time.time() - start_t) * 1000

                actual_src = data.get("source")
                actual_conf = data.get("confidence_score", 0.0)
                citations = data.get("citations", [])

                passed = (actual_src == expected_src)
                if expected_src == "local_rag" and min_conf > 0.0:
                    passed = passed and (actual_conf >= min_conf)

                status_str = "[PASS]" if passed else "[FAIL]"
                badge_str = "[LOCAL_RAG (Verified Context)]" if actual_src == "local_rag" else "[CLOUD_FALLBACK (Search Grounded)]"

                if passed:
                    passed_count += 1
                else:
                    failed_count += 1

                print(f"{status_str} {tc_id}: {tc_name}")
                print(f"       Query      : '{query}'")
                print(f"       Route      : {badge_str} (Score: {actual_conf:.2f} | Latency: {latency_ms:.0f}ms)")
                print(f"       Citations  : {len(citations)} source snippet(s)")
                if citations:
                    first_line = citations[0].split("\n")[0]
                    print(f"       First Cit  : {first_line[:75]}...")
                print()

        except urllib.error.URLError as e:
            failed_count += 1
            print(f"[ERROR] {tc_id}: Connection failed to {API_URL}. Is the server running? Details: {e}\n")

    print("=" * 80)
    print(f"  BENCHMARK SUMMARY: {passed_count}/{len(test_cases)} Passed | {failed_count} Failed")
    print("=" * 80 + "\n")

if __name__ == "__main__":
    run_test_suite()
