# Passive Reconnaissance Report – holbertonschool.com

## 1. Introduction
This report presents passive reconnaissance information collected on the domain **holbertonschool.com** using **Shodan**.
The objective is to identify IP ranges, technologies, and frameworks used across the domain and its subdomains without actively interacting with the target systems.

---

## 2. Methodology
The information was gathered using the Shodan search engine with the following techniques:
- Domain-based search
- IP-based results correlation
- Technology fingerprinting provided by Shodan

No active scanning was performed.

---

## 3. IP Ranges
Based on Shodan results, holbertonschool.com infrastructure is mainly hosted on cloud services (Google Cloud).

Identified IP ranges include:
- 34.0.0.0/8 (Google Cloud Platform)
- 35.0.0.0/8 (Google Cloud Platform)

These ranges indicate that the domain relies on Google-managed infrastructure.

---

## 4. Subdomains Observed
The following subdomains were identified via Shodan and related passive sources:
- holbertonschool.com
- www.holbertonschool.com
- apply.holbertonschool.com
- intranet.holbertonschool.com

---

## 5. Technologies and Frameworks
Shodan identified the following technologies across the domain and its subdomains:

### Web Servers
- Nginx
- Google Frontend (GFE)

### Programming Languages & Frameworks
- JavaScript
- PHP
- Python (backend services)

### Cloud & Hosting
- Google Cloud Platform (GCP)
- Google App Engine

### Security & Network
- HTTPS / TLS
- Cloud-based firewalls (Google-managed)

---

## 6. Observations
- The domain relies heavily on cloud infrastructure, reducing exposure to direct IP-based attacks.
- Use of managed services increases availability and security.
- Most services are protected behind HTTPS and cloud frontends.

---

## 7. Conclusion
Passive reconnaissance using Shodan reveals that **holbertonschool.com** is hosted on a modern cloud infrastructure with common web technologies and strong network protections.
No critical exposure was observed through passive analysis.

---

## 8. Disclaimer
This report is based solely on publicly available information obtained via Shodan and other passive reconnaissance techniques.

