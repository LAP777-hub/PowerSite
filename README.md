# ⚡ PowerSite — Electricity Fault Reporting System

**Academic Django Project** | *Electricity Fault Reporting & Tracking Platform*

---

## One-Sentence Summary

> *"PowerSite is a Django-based web application developed to help residents of Masibekela Village report electricity faults, distinguish between loadshedding and unplanned outages, track repair progress, and receive timely updates through a centralized digital platform."*

---

## About the Project

PowerSite was developed as part of the **NHCI63110 Human-Computer Interaction** module.

The system addresses a common challenge faced by residents in Masibekela Village, Nkomazi Municipality, where electricity interruptions caused by faults, cable theft, damaged infrastructure, or household overloads are often confused with scheduled loadshedding.

Instead of relying on multiple communication channels, PowerSite provides a single platform where residents can:

| Resident Can |
|---|
| Check electricity status |
| View loadshedding schedules |
| Report electricity faults |
| Pin fault locations on an interactive map |
| Track repair progress |
| Receive notifications |
| Monitor previously submitted reports |

---

## Project Information

| Detail | Information |
|---|---|
| Project Name | PowerSite |
| Project Type | Academic Project |
| Module | NHCI63110 – Human Computer Interaction |
| Framework | Django |
| Language | Python |
| Database | SQLite (Django ORM) + Browser Local Storage |
| Frontend | HTML, CSS, JavaScript |
| Repository | https://github.com/LAP777-hub/PowerSite |

---

## Data & Storage

PowerSite uses two storage layers, each serving a different purpose:

| Storage Layer | Used For |
|---|---|
| SQLite (Django database) | Core account data and authentication — including creating the **Administrator** and **Technician** accounts as Django superusers via `createsuperuser`, plus registered resident accounts and role-based permissions. |
| Browser Local Storage | Lightweight client-side data such as UI preferences (e.g. dark mode), in-progress form data, and temporary session state on the resident's device. |

> Note: All persistent, shared, and role-critical data (users, fault reports, repair status, notifications) lives in the Django/SQLite database. Local storage is used only for client-side convenience and is not a substitute for the backend database.

---

## Installation

**Clone the repository**

```bash
git clone https://github.com/LAP777-hub/PowerSite.git
```

**Navigate into the project**

```bash
cd PowerSite
```

**Create a virtual environment**

```bash
python -m venv venv
```

**Activate it**

Windows
```bash
venv\Scripts\activate
```

Linux / macOS
```bash
source venv/bin/activate
```

**Install dependencies**

```bash
pip install -r requirements.txt
```

**Run migrations**

```bash
python manage.py migrate
```

**Create an administrator or technician account**

```bash
python manage.py createsuperuser
```

**Start the server**

```bash
python manage.py runserver
```

**Open**

```
http://127.0.0.1:8000/
```

---

## User Roles

### Resident

Residents can:

| Capability |
|---|
| Register an account |
| Log in securely |
| Report electricity faults |
| Upload supporting images |
| Pin the fault location on a map |
| View report history |
| Track repair progress |
| Receive notifications |

### Administrator

Administrators can:

| Capability |
|---|
| View submitted reports |
| Assign technicians |
| Update repair status |
| Manage users |
| Monitor all reported issues |

> Administrator accounts are created via the Django database as superusers (`python manage.py createsuperuser`).

### Technician

Technicians can:

| Capability |
|---|
| View assigned faults |
| Update repair progress |
| Mark issues as resolved |
| Provide repair updates |

> Technician accounts are also created via the Django database as superusers, then assigned the Technician role.

---

## Features

| Feature | Description |
|---|---|
| Secure Authentication | Django-backed login and registration |
| Electricity Status Dashboard | At-a-glance community power status |
| Loadshedding Schedule Checker | View scheduled outage times |
| Fault Reporting | Report unplanned electricity faults |
| Interactive Map Location Pinning | Pin the exact fault location on a map |
| Image Upload | Attach supporting photos to a report |
| Issue Tracking | Track a report from submission to resolution |
| Notifications | Alerts on report status changes |
| Admin Dashboard | Manage reports, technicians, and users |
| Technician Dashboard | View and update assigned repairs |
| User Profiles | Manage personal account details |
| Dark Mode Support | Light/dark UI toggle (stored locally) |
| Search & Filtering | Quickly find reports and records |

---

## System Modules

| Module | Description |
|---|---|
| Accounts | Registration, Login, Profile Management |
| Dashboard | Electricity Status & Community Information |
| Reports | Fault Reporting & Tracking |
| Notifications | User Alerts |
| Admin | User & Report Management |
| Technician | Repair Progress Management |

---

## Tech Stack

| Technology | Purpose |
|---|---|
| Python | Backend |
| Django | Web Framework |
| HTML5 | Structure |
| CSS3 | Styling |
| JavaScript | Client-side Functionality |
| SQLite (Django ORM) | Core Database — accounts, reports, roles |
| Browser Local Storage | Client-side UI state & preferences |
| Bootstrap | Responsive Design |
| Git | Version Control |
| GitHub | Repository Hosting |
| Visual Studio Code | Development Environment |

---

## Project Structure

```text
PowerSite/
│
├── accounts/
├── reports/
├── templates/
├── static/
├── media/
├── manage.py
├── requirements.txt
├── db.sqlite3
└── README.md
```

---

## Project Objectives

The project aims to:

| Objective |
|---|
| Improve community electricity fault reporting. |
| Reduce confusion between loadshedding and unexpected faults. |
| Improve communication between residents and service providers. |
| Demonstrate user-centred interface design. |
| Apply Human-Computer Interaction principles. |
| Develop a responsive web application using Django. |

---

## Human-Computer Interaction Principles Applied

| Principle |
|---|
| User-Centred Design |
| Visibility |
| Consistency |
| Feedback |
| Learnability |
| Error Prevention |
| Accessibility |
| Simplicity |
| Efficiency |
| User Control |

---

## What I Learned

Developing PowerSite significantly improved my understanding of Human-Computer Interaction and full-stack web development using Django.

Throughout the project, I learned how to:

| Skill Gained |
|---|
| Conduct user and problem analysis. |
| Create user personas and usage scenarios. |
| Apply usability and user experience principles. |
| Design intuitive interfaces. |
| Build a role-based Django application. |
| Connect frontend interfaces with backend functionality. |
| Design database models and user workflows. |
| Iteratively improve a system using AI-assisted usability evaluation. |

The project reinforced the importance of designing technology around users rather than expecting users to adapt to technology.

---

## Developer

| Name | Role |
|---|---|
| **Lucky Pinga** | Sole Developer, UI/UX Designer, Django Developer, System Designer & Researcher |

---

## Academic Notice

PowerSite was developed as an academic project for the NHCI63110 Human-Computer Interaction module. The system serves as a prototype demonstrating user-centered design principles and Django web development. It is intended for educational purposes and is not connected to any live municipal electricity infrastructure.

---

## License

This project is licensed under the MIT License.

---

*"Improving community electricity reporting through user-centered digital innovation."*
