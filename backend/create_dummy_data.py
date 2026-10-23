"""
Dummy Legal Corpus Generator for S2 Legal AI Pro
Generates sample statutory PDF documents in backend/data/ to test multi-document ingestion:
1. sample_arbitration_act.pdf
2. sample_commercial_contracts.pdf
"""

import sys
from pathlib import Path

# Add project root to sys.path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from backend.corpus_builder import create_pdf_binary

DATA_DIR = Path(__file__).resolve().parent / "data"

def build_arbitration_act():
    return [
        (
            "ARBITRATION AND CONCILIATION ACT 1996 - GENERAL PROVISIONS",
            "SECTION 7. ARBITRATION AGREEMENT: (1) An agreement by the parties to submit to arbitration "
            "all or certain disputes which have arisen or which may arise between them in respect of a defined "
            "legal relationship, whether contractual or not.\n\n"
            "(2) An arbitration agreement may be in the form of an arbitration clause in a contract or in the form of a separate agreement.\n\n"
            "(3) An arbitration agreement shall be in writing: contained in a document signed by the parties, "
            "an exchange of letters, telex, telegrams or other means of telecommunication including electronic communication."
        ),
        (
            "ARBITRATION AND CONCILIATION ACT 1996 - JUDICIAL INTERVENTION",
            "SECTION 8. POWER TO REFER PARTIES TO ARBITRATION WHERE THERE IS AN ARBITRATION AGREEMENT: "
            "A judicial authority, before which an action is brought in a matter which is the subject of an arbitration agreement shall, "
            "if a party applies not later than the date of submitting his first statement on the substance of the dispute, "
            "refer the parties to arbitration unless it finds that prima facie no valid arbitration agreement exists.\n\n"
            "SECTION 9. INTERIM MEASURES BY COURT: A party may, before, or during arbitral proceedings or at any time "
            "after the making of the arbitral award but before it is enforced, apply to a Court for interim protection, "
            "preservation or custody of goods, securing the amount in dispute, or interim injunction."
        ),
        (
            "ARBITRATION AND CONCILIATION ACT 1996 - APPOINTMENT & AWARDS",
            "SECTION 11. APPOINTMENT OF ARBITRATORS: Procedure for appointment. Failing agreement, Chief Justice of High Court "
            "or Supreme Court or designated arbitral institution may appoint the arbitrator upon application.\n\n"
            "SECTION 34. APPLICATION FOR SETTING ASIDE ARBITRAL AWARD: Recourse to a Court against an arbitral award may be made "
            "only by an application for setting aside such award in accordance with sub-section (2) and sub-section (3). "
            "Grounds: Incapacity of party, invalid agreement, lack of notice, dispute beyond scope of submission, "
            "composition of tribunal not in accordance with agreement, or conflict with public policy of India (patent illegality)."
        ),
    ]

def build_commercial_contracts():
    return [
        (
            "INDIAN CONTRACT ACT 1872 - FORMATION AND VALIDITY",
            "SECTION 10. WHAT AGREEMENTS ARE CONTRACTS: All agreements are contracts if they are made by the free consent "
            "of parties competent to contract, for a lawful consideration and with a lawful object, and are not hereby expressly declared to be void.\n\n"
            "SECTION 14. FREE CONSENT: Consent is free when it is not caused by coercion (Section 15), undue influence (Section 16), "
            "fraud (Section 17), misrepresentation (Section 18), or mistake (Sections 20, 21, 22).\n\n"
            "SECTION 23. WHAT CONSIDERATIONS AND OBJECTS ARE LAWFUL: The consideration or object of an agreement is lawful, unless: "
            "it is forbidden by law, or is of such a nature that, if permitted, it would defeat the provisions of any law, "
            "or is fraudulent, or involves injury to the person or property of another, or the Court regards it as immoral or opposed to public policy."
        ),
        (
            "INDIAN CONTRACT ACT 1872 - REMEDIES FOR BREACH",
            "SECTION 73. COMPENSATION FOR LOSS OR DAMAGE CAUSED BY BREACH OF CONTRACT: When a contract has been broken, the party who suffers "
            "by such breach is entitled to receive, from the party who has broken the contract, compensation for any loss or damage "
            "caused to him thereby, which naturally arose in the usual course of things from such breach, or which the parties knew, "
            "when they made the contract, to be likely to result from the breach of it (Rule in Hadley v. Baxendale). Remote damages not recoverable.\n\n"
            "SECTION 74. COMPENSATION FOR BREACH OF CONTRACT WHERE PENALTY STIPULATED FOR: When a contract has been broken, "
            "if a sum is named in the contract as the amount to be paid in case of such breach, the party complaining is entitled "
            "to receive reasonable compensation not exceeding the amount so named (Kailash Nath Associates v. DDA precedent)."
        ),
    ]

def generate_dummy_files():
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    arb_path = DATA_DIR / "sample_arbitration_act.pdf"
    arb_bytes = create_pdf_binary(build_arbitration_act())
    arb_path.write_bytes(arb_bytes)
    print(f"[DUMMY DATA] Generated: {arb_path.name} ({len(arb_bytes)} bytes)")

    contracts_path = DATA_DIR / "sample_commercial_contracts.pdf"
    contracts_bytes = create_pdf_binary(build_commercial_contracts())
    contracts_path.write_bytes(contracts_bytes)
    print(f"[DUMMY DATA] Generated: {contracts_path.name} ({len(contracts_bytes)} bytes)")

if __name__ == "__main__":
    generate_dummy_files()
