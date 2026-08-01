# Newspaper Agency Management Platform

A robust web application designed to streamline the operations of a newspaper editorial office. This platform allows administrators and chief editors to manage topics, track newspaper publications, and organize editorial staff efficiently.

## 🚀 Features

* **Topic Management**: Create, edit, and delete news categories and topics.
* **Newspaper Management**: Publish, update, and track different newspaper editions and articles.
* **Editor Management**: Manage editorial staff profiles, track their articles, and assign roles.
* **User Authentication**: Secure login, logout, and registration system with permission-based access control.
* **Responsive UI**: Clean and modern user interface built for both desktop and mobile devices.

## 🛠️ Technologies Used

* **Backend**: Django 4.2 (Python)
* **Frontend**: Bootstrap 5, HTML5, CSS3
* **Database**: SQLite (Development default)

---

## 💻 Getting Started

Follow these steps to set up and run the project locally on your machine.

### Prerequisites

Ensure you have **Python 3.10+** and **git** installed.

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/viakol-prog/newspaper-agency-mate.git
   cd newspaper-agency-mate
   ```

2. **Create and activate a virtual environment (Optional but recommended)**
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run database migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create an administrative user (Superuser)**
   To access the Django admin panel, create an admin account:
   ```bash
   python manage.py createsuperuser
   ```
   *Follow the on-screen prompts to set your username, email, and password.*

6. **Start the development server**
   ```bash
   python manage.py runserver
   ```

Open your browser and navigate to `http://127.0.0.1:8000/` to view the application. Access the admin dashboard at `http://127.0.0.1:8000/admin/`.

---

## 📜 License

This project is licensed under the **MIT License**.

```text
MIT License

Copyright (c) 2026 viakol-prog

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
