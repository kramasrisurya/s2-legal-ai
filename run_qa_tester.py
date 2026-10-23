"""
S2 Legal AI Pro - 20-Question Comprehensive QA & Comparative Accuracy Benchmark
Tests direct Article queries, Citizen scenario stories, Statutory concordance, and SC Precedents.
"""

import sys
import io
import json
import time
import requests

# Fix Windows console encoding
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

API_URL = "http://127.0.0.1:8000/api/chat"

TEST_QUESTIONS = [
    {
        "id": "Q01",
        "category": "Constitutional Law (Direct Statutory)",
        "role": "advocate",
        "persona": "Advocate",
        "query": "What are the specific rights protected under Article 21, and how does the procedure established by law test apply after Maneka Gandhi?",
        "intent_type": "Direct Constitutional Article & Doctrine",
    },
    {
        "id": "Q02",
        "category": "Citizen Story / Scenario (Illegal Police Custody)",
        "role": "client",
        "persona": "Client (Citizen)",
        "query": "My brother was picked up by the local police 36 hours ago without an arrest memo, and they have not produced him before any Magistrate. What sections protect him and what immediate legal steps should our family take?",
        "intent_type": "Factual Scenario - Unlawful Detention & Habeas Corpus",
    },
    {
        "id": "Q03",
        "category": "Constitutional Law (Writ Jurisdiction)",
        "role": "advocate",
        "persona": "Advocate",
        "query": "What is the scope of writ jurisdiction under Article 226 versus Article 32, and which writs can be issued against private bodies performing public duty?",
        "intent_type": "Direct Constitutional Article & High Court Jurisdiction",
    },
    {
        "id": "Q04",
        "category": "Citizen Story / Scenario (Marital Cruelty & Dowry)",
        "role": "client",
        "persona": "Client (Citizen)",
        "query": "My sister is facing severe physical abuse and constant dowry demands from her husband and in-laws. What sections under the new criminal law apply, and how can we get immediate protection?",
        "intent_type": "Factual Scenario - Cruelty & Domestic Violence",
    },
    {
        "id": "Q05",
        "category": "Constitutional Law (Equality Doctrine)",
        "role": "advocate",
        "persona": "Advocate",
        "query": "How does Article 14 prohibit manifest arbitrariness in state action following the Shayara Bano and E.P. Royappa doctrine?",
        "intent_type": "Direct Constitutional Article & Non-Arbitrariness Doctrine",
    },
    {
        "id": "Q06",
        "category": "Citizen Story / Scenario (Cheque Dishonour)",
        "role": "client",
        "persona": "Client (Business Owner)",
        "query": "A business vendor gave me a cheque for Rs. 15 lakhs for delivered materials, but the bank bounced it due to insufficient funds. What legal notice and sections apply under Indian law?",
        "intent_type": "Factual Scenario - Negotiable Instruments Act S. 138",
    },
    {
        "id": "Q07",
        "category": "Landmark Supreme Court Precedent",
        "role": "advocate",
        "persona": "Advocate",
        "query": "What was the core ratio decidendi of Kesavananda Bharati v. State of Kerala regarding Article 368 and the unamendable basic structure of the Constitution?",
        "intent_type": "Landmark Precedent & Basic Structure Doctrine",
    },
    {
        "id": "Q08",
        "category": "Citizen Story / Scenario (Unlawful Municipal Demolition)",
        "role": "client",
        "persona": "Client (Shop Owner)",
        "query": "The municipal corporation demolished my shop's boundary wall without any prior notice or compensation. Does the Constitution protect my property rights and what emergency court remedy can I seek?",
        "intent_type": "Factual Scenario - Property Rights (Art 300A) & Natural Justice",
    },
    {
        "id": "Q09",
        "category": "Statutory Concordance (IPC vs BNS 2023)",
        "role": "advocate",
        "persona": "Advocate",
        "query": "What is the concordance between Section 420 IPC and Section 318 BNS 2023, and how are pending investigations for pre-July 2024 offences governed?",
        "intent_type": "Statutory Transition & Criminal Code Concordance",
    },
    {
        "id": "Q10",
        "category": "Citizen Story / Scenario (Urgent Anticipatory Bail)",
        "role": "client",
        "persona": "Client (Accused Citizen)",
        "query": "A business rival filed a false police complaint alleging criminal breach of trust against me, and police are threatening to arrest me tomorrow. Can I get anticipatory bail and under what section?",
        "intent_type": "Factual Scenario - Anticipatory Bail (CrPC 438 vs BNSS 482)",
    },
    {
        "id": "Q11",
        "category": "Landmark Supreme Court Precedent (Bail Jurisprudence)",
        "role": "advocate",
        "persona": "Advocate",
        "query": "What are the binding bail guidelines established by the Supreme Court in Satender Kumar Antil v. CBI, especially for Category A offences?",
        "intent_type": "Landmark Precedent & Bail Administration",
    },
    {
        "id": "Q12",
        "category": "Citizen Story / Scenario (Cyber Financial Fraud)",
        "role": "client",
        "persona": "Client (Scam Victim)",
        "query": "I was duped of Rs. 4 lakhs through a fraudulent UPI phishing link yesterday. What immediate cyber cell steps and legal sections under IT Act and criminal law apply?",
        "intent_type": "Factual Scenario - Cybercrime & Phishing Recovery",
    },
    {
        "id": "Q13",
        "category": "Constitutional Law (Freedom of Speech)",
        "role": "advocate",
        "persona": "Advocate",
        "query": "What are the eight exhaustive grounds of reasonable restrictions on freedom of speech under Article 19(2) of the Constitution?",
        "intent_type": "Direct Constitutional Article - Fundamental Freedoms",
    },
    {
        "id": "Q14",
        "category": "Citizen Story / Scenario (Breach of Employment Contract)",
        "role": "client",
        "persona": "Client (Employee)",
        "query": "My software company terminated my contract without giving the 3-month notice period mentioned in my offer letter and has withheld 2 months of salary. Can I sue them under contract law?",
        "intent_type": "Factual Scenario - Indian Contract Act S. 73 Breach",
    },
    {
        "id": "Q15",
        "category": "Commercial Arbitration (Section 34)",
        "role": "advocate",
        "persona": "Advocate",
        "query": "Under Section 34 of the Arbitration and Conciliation Act 1996, what constitutes 'patent illegality' and 'conflict with public policy' for setting aside a domestic award?",
        "intent_type": "Statutory Interpretation - Arbitration & Conciliation Act",
    },
    {
        "id": "Q16",
        "category": "Citizen Story / Scenario (Online Defamation)",
        "role": "client",
        "persona": "Client (Doctor)",
        "query": "An anonymous user posted false, defamatory allegations about my medical clinic on Facebook and Google Reviews causing severe loss of patients. Can I file a criminal and civil case?",
        "intent_type": "Factual Scenario - Criminal Defamation & Civil Damages",
    },
    {
        "id": "Q17",
        "category": "Constitutional Law (Arrest & Detention Safeguards)",
        "role": "advocate",
        "persona": "Advocate",
        "query": "What are the mandatory constitutional safeguards guaranteed to an arrested person under Article 22(1) and Article 22(2)?",
        "intent_type": "Direct Constitutional Article - Safeguards against Arrest",
    },
    {
        "id": "Q18",
        "category": "Citizen Story / Scenario (Consumer Product Defect)",
        "role": "client",
        "persona": "Client (Consumer)",
        "query": "I bought an electric scooter whose battery caught fire while charging, damaging my garage and injuring my hand. What compensation and claims can I file under the Consumer Protection Act 2019?",
        "intent_type": "Factual Scenario - Product Liability & Consumer Commission",
    },
    {
        "id": "Q19",
        "category": "Landmark Supreme Court Precedent (Privacy Jurisprudence)",
        "role": "advocate",
        "persona": "Advocate",
        "query": "How did the 9-judge bench in Justice K.S. Puttaswamy v. Union of India define the informational privacy and proportionality standard under Article 21?",
        "intent_type": "Landmark Precedent - Proportionality & Fundamental Rights",
    },
    {
        "id": "Q20",
        "category": "Citizen Story / Scenario (Unlawful Police Search)",
        "role": "client",
        "persona": "Client (Citizen)",
        "query": "Police officers barged into my private residence at midnight without a search warrant or female officers and searched my bedrooms. Was this lawful and what legal action can I initiate against the officers?",
        "intent_type": "Factual Scenario - Search Without Warrant & D.K. Basu Guidelines",
    },
]

def main():
    print("=" * 80)
    print("  S2 LEGAL AI PRO: 20-QUESTION BENCHMARK & COMPARATIVE EVALUATION")
    print(f"  Target Endpoint: {API_URL}")
    print("=" * 80)

    results = []

    for item in TEST_QUESTIONS:
        qid = item["id"]
        query = item["query"]
        role = item["role"]
        cat = item["category"]

        print(f"\n[RUNNING {qid}] [{item['persona']}] ({cat})")
        print(f"Query: '{query}'")

        payload = {
            "query": query,
            "history": [],
            "role": role,
        }

        t0 = time.time()
        try:
            res = requests.post(API_URL, json=payload, timeout=40)
            latency_ms = int((time.time() - t0) * 1000)
            if res.status_code == 200:
                data = res.json()
                source = data.get("source")
                score = data.get("confidence_score", 0.0)
                citations = data.get("citations", [])
                text = data.get("text", "")

                result_entry = {
                    "id": qid,
                    "category": cat,
                    "role": role,
                    "persona": item["persona"],
                    "query": query,
                    "intent_type": item["intent_type"],
                    "latency_ms": latency_ms,
                    "source": source,
                    "confidence_score": score,
                    "citations_count": len(citations),
                    "first_citation": citations[0][:120] if citations else "N/A",
                    "response_text": text,
                }
                results.append(result_entry)
                print(f"  -> Route: [{source.upper()}] | Score: {score:.2f} | Latency: {latency_ms}ms | Cits: {len(citations)}")
                preview = text[:140].replace("\n", " ")
                print(f"  -> Answer Preview: {preview}...")
            else:
                print(f"  -> ERROR HTTP {res.status_code}: {res.text}")
        except Exception as e:
            print(f"  -> REQUEST EXCEPTION: {e}")

    # Save to JSON
    with open("benchmark_20_results.json", "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    print("\n" + "=" * 80)
    print(f"  COMPLETED {len(results)}/{len(TEST_QUESTIONS)} TESTS. Saved to benchmark_20_results.json")
    print("=" * 80)

if __name__ == "__main__":
    main()
