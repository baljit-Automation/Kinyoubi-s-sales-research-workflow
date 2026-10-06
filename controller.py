import json
from datetime import datetime

def load_campaign_data(filepath="Kinyoubi_India_Campaign.json"):
    print("📂 Loading campaign data...")
    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)
    print(f"✅ Successfully loaded campaign: {data.get('name')}")
    return data

def update_sent_status(data):
    """Reconciles leads L001 to L005 as sent, preserving messages and excluding from drafts."""
    target_ids = ["L001", "L002", "L003", "L004", "L005"]
    for lead in data.get("leads", []):
        if lead.get("id") in target_ids:
            lead["status"] = "sent"
            lead["next_action"] = "Already contacted. Excluded from new first-touch drafts."
    return data

def audit_lead_scores_and_evidence(data):
    """Audits leads to show scores, evidence status, and highlight any unknowns."""
    print("\n🔍 --- RUNNING LEAD AUDIT & EVIDENCE CHECK ---")
    
    for lead in data.get("leads", [])[:5]:  # Let's check the first 5 leads as a sample
        lead_id = lead.get("id")
        company = lead.get("company")
        scores = lead.get("scores", {})
        total_score = sum(scores.values())
        unknowns_count = len(lead.get("unknowns", []))
        
        print(f"\nLead [{lead_id}]: {company}")
        print(f"  • Priority Score: {total_score}/100")
        print(f"  • Score Breakdown -> Service Fit: {scores.get('service_fit')}, Business Signal: {scores.get('business_signal')}, Proof Fit: {scores.get('proof_fit')}, Buyer Role: {scores.get('buyer_role')}, Contact Route: {scores.get('contact_route')}")
        print(f"  • Unconfirmed Factors (Unknowns): {unknowns_count} items flagged")

def save_campaign_data(data, filepath="Kinyoubi_India_Campaign.json"):
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    print("\n💾 Campaign data successfully saved!")

def review_menu(data):
    """Interactive CLI menu to view leads, check drafts, and simulate approval."""
    while True:
        print("\n==============================")
        print("📋 KINYOUBI CAMPAIGN REVIEW MENU")
        print("============================== \n")
        print("1. View all leads summary")
        print("2. Inspect a specific lead & email draft")
        print("3. Run Lead & Evidence Audit (New Step 2)")
        print("4. Exit and save")
        
        choice = input("\nEnter your choice (1-4): ").strip()
        
        if choice == "1":
            print("\n--- LEADS SUMMARY ---")
            for lead in data.get("leads", []):
                print(f"[{lead.get('id')}] {lead.get('company')} | Status: {lead.get('status').upper()} | Decision Maker: {lead.get('decision_maker', {}).get('name', 'N/A')}")
        
        elif choice == "2":
            lead_id = input("Enter Lead ID to inspect (e.g., L001, L002): ").strip().upper()
            found = False
            for lead in data.get("leads", []):
                if lead.get("id") == lead_id:
                    found = True
                    print(f"\n🏢 Company: {lead.get('company')}")
                    print(f"👤 Decision Maker: {lead.get('decision_maker', {}).get('name')} ({lead.get('decision_maker', {}).get('role')})")
                    print(f"📧 Contact Email: {lead.get('contact', {}).get('email')}")
                    print(f"📌 Status: {lead.get('status').upper()}")
                    
                    draft = lead.get("draft")
                    if draft:
                        print(f"\n--- EMAIL DRAFT (Subject: {draft.get('subject')}) ---")
                        print(draft.get("body"))
                        print("--------------------------------------------------")
                        
                        action = input("Do you want to approve this draft? (y/n): ").strip().lower()
                        if action == 'y':
                            lead["approval"] = {"approved": True, "at": datetime.now().strftime("%Y-%m-%d")}
                            lead["next_action"] = "Draft approved by user. Manual sending required (Auto-send disabled)."
                            print("✅ Draft approved locally! (Remember: Email sending is safely disabled).")
                    else:
                        print("\n❌ No email draft available for this lead yet.")
                    break
            if not found:
                print(f"❌ Lead ID {lead_id} not found.")

        elif choice == "3":
            audit_lead_scores_and_evidence(data)
                
        elif choice == "4":
            print("Exiting review menu...")
            break
        else:
            print("❌ Invalid choice. Please choose 1, 2, 3, or 4.")

if __name__ == "__main__":
    campaign_data = load_campaign_data()
    campaign_data = update_sent_status(campaign_data)
    review_menu(campaign_data)
    save_campaign_data(campaign_data)