#!/usr/bin/env python3

# ==========================================
# CodeSunGrab v3.0.2
# Appwrite Authentication + Email Verification
# ==========================================

import os
import json
import secrets
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from datetime import datetime, timedelta
import requests
from config import (
    APPWRITE_ENDPOINT, APPWRITE_PROJECT_ID, APPWRITE_API_KEY,
    APPWRITE_DATABASE_ID, APPWRITE_USERS_COLLECTION,
    APPWRITE_DOWNLOADS_COLLECTION, SESSION_FILE, SESSION_TIMEOUT_DAYS,
    SMTP_EMAIL, SMTP_PASSWORD, SMTP_HOST, SMTP_PORT, SMTP_FROM_NAME,
    APP_NAME, VERSION, EDITION, BRAND, AUTHOR
)
from utils import logger


class AppwriteAuth:
    def __init__(self):
        self.endpoint = APPWRITE_ENDPOINT
        self.project_id = APPWRITE_PROJECT_ID
        self.api_key = APPWRITE_API_KEY
        self.database_id = APPWRITE_DATABASE_ID

        self.headers = {
            'X-Appwrite-Project': self.project_id,
            'X-Appwrite-Key': self.api_key,
            'Content-Type': 'application/json'
        }

        self.current_user = None
        self.session_data = None
        self.load_local_session()

    def _request(self, method, path, data=None):
        url = f"{self.endpoint}{path}"
        try:
            if method == 'GET':
                response = requests.get(url, headers=self.headers)
            elif method == 'POST':
                response = requests.post(url, headers=self.headers, json=data)
            elif method == 'PUT':
                response = requests.put(url, headers=self.headers, json=data)
            elif method == 'PATCH':
                response = requests.patch(url, headers=self.headers, json=data)
            elif method == 'DELETE':
                response = requests.delete(url, headers=self.headers)

            if response.status_code in [200, 201, 204]:
                return True, response.json() if response.text else {}
            else:
                error_msg = response.json().get('message', str(response.status_code))
                return False, error_msg
        except Exception as e:
            return False, str(e)

    def generate_verification_code(self):
        return ''.join([str(secrets.randbelow(10)) for _ in range(6)])

    def send_verification_email(self, to_email, code, full_name=""):
        try:
            year = datetime.now().year
            body = f"""
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Dear user Verify Your Email - {APP_NAME}</title>
                <style>
                    * {{ margin: 0; padding: 0; box-sizing: border-box; }}
                    body {{ background: linear-gradient(135deg, #f0f4f8 0%, #d9e2ec 100%); font-family: 'Segoe UI', sans-serif; padding: 20px; }}
                    .container {{ max-width: 600px; margin: 0 auto; background: #fff; border-radius: 20px; overflow: hidden; box-shadow: 0 20px 60px rgba(0,0,0,0.15); }}
                    .header {{ background: linear-gradient(135deg, #0b1e33 0%, #1a3a5c 100%); padding: 35px 30px; text-align: center; }}
                    .header img {{ width: 65px; border-radius: 14px; border: 2px solid #FFD700; margin-bottom: 12px; }}
                    .header h1 {{ color: #FFD700; font-size: 28px; margin: 0; }}
                    .header .sub {{ color: rgba(255,255,255,0.8); font-size: 13px; margin-top: 6px; }}
                    .header .flag {{ font-size: 16px; color: #fff; margin-top: 8px; }}
                    .content {{ padding: 30px; }}
                    .code-box {{ background: #f6f8fc; border: 2px dashed #b0bec5; border-radius: 14px; padding: 25px; text-align: center; margin: 20px 0; }}
                    .code {{ font-size: 44px; font-weight: 700; letter-spacing: 12px; font-family: 'Courier New', monospace; background: #fff; padding: 10px 20px; border-radius: 8px; display: inline-block; }}
                    .footer {{ background: #0b1e33; padding: 20px; text-align: center; border-top: 3px solid #FFD700; }}
                    .footer .brand {{ color: #FFD700; font-size: 18px; font-weight: 700; }}
                    .footer .brand span {{ color: #fff; }}
                    .footer .social a {{ color: #FFD700; text-decoration: none; margin: 0 8px; }}
                    .footer .copy {{ color: #718096; font-size: 11px; margin-top: 10px; }}
                </style>
            </head>
            <body>
                <div class="container">
                    <div class="header">
                        <img src="cid:logo_image" alt="CodeSun Logo">
                        <h1>{APP_NAME}</h1>
                        <div class="sub">{BRAND} — Built for Developers</div>
                        <div class="flag">🇦🇷 {EDITION} 🇦🇷</div>
                    </div>
                    <div class="content">
                        <h2>Hello {full_name or 'Valued User'}! 👋</h2>
                        <p style="color:#4a5568;margin:15px 0;">Thank you for choosing {APP_NAME}. Use the code below to verify your email:</p>
                        <div class="code-box">
                            <p style="color:#6b7a8f;text-transform:uppercase;letter-spacing:2px;font-weight:600;">🔐 Verification Code</p>
                            <div class="code">{code}</div>
                            <p style="margin-top:8px;"> Copy & paste in terminal</p>
                            <p style="font-size:12px;color:#8a9aa8;">⏱️ Expires in 10 minutes</p>
                        </div>
                        <p style="background:#fff8e1;border-left:4px solid #ffb300;padding:10px;border-radius:4px;color:#6d5a00;font-size:13px;">⚠️ If you didn't request this, ignore this email.</p>
                    </div>
                    <div class="footer">
                        <div class="brand"><span>Code</span>Sun</div>
                        <p style="color:#cbd5e0;font-size:12px;">Building Tools for Developers 🚀</p>
                        <div class="social" style="margin-top:12px;">
                            🌐 <a href="https://codewithrafsun.com">Website</a> ·
                            🐙 <a href="https://github.com/CodeWithRafsun">GitHub</a> ·
                            🐦 <a href="https://x.com/codewithrafsun">Twitter</a>
                        </div>
                        <div class="copy">© {year} {BRAND}. All Rights Reserved.<br>🇦🇷 VAMOS ARGENTINA! 🇦🇷</div>
                    </div>
                </div>
            </body>
            </html>
            """

            msg = MIMEMultipart('related')
            msg['From'] = f"{SMTP_FROM_NAME} <{SMTP_EMAIL}>"
            msg['To'] = to_email
            msg['Subject'] = f"🔐 Verify Your Email - {APP_NAME}"

            msg_alt = MIMEMultipart('alternative')
            msg.attach(msg_alt)
            msg_alt.attach(MIMEText(body, 'html'))

            logo_path = os.path.join(os.path.dirname(__file__), 'public', 'codesun.png')
            if os.path.exists(logo_path):
                with open(logo_path, 'rb') as f:
                    img = MIMEImage(f.read(), _subtype='png')
                    img.add_header('Content-ID', '<logo_image>')
                    msg.attach(img)

            with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as server:
                server.starttls()
                server.login(SMTP_EMAIL, SMTP_PASSWORD)
                server.send_message(msg)

            logger.info(f"Verification email sent to {to_email}")
            return True, "Verification email sent successfully"
        except Exception as e:
            logger.error(f"Failed to send email: {e}")
            return False, str(e)

    # ==========================================
    # SESSION MANAGEMENT
    # ==========================================
    def load_local_session(self):
        if os.path.exists(SESSION_FILE):
            try:
                with open(SESSION_FILE, 'r') as f:
                    self.session_data = json.load(f)
                    if self.session_data:
                        created_at = datetime.fromisoformat(self.session_data.get('created_at', ''))
                        if (datetime.now() - created_at).days >= SESSION_TIMEOUT_DAYS:
                            self.clear_session()
                            return
                        self.current_user = self.session_data.get('user')
            except:
                self.session_data = None
                self.current_user = None

    def save_local_session(self, user_data, session_id=None):
        self.session_data = {'user': user_data, 'session_id': session_id, 'created_at': datetime.now().isoformat()}
        self.current_user = user_data
        try:
            os.makedirs(os.path.dirname(SESSION_FILE), exist_ok=True)
            with open(SESSION_FILE, 'w') as f:
                json.dump(self.session_data, f, indent=2)
        except Exception as e:
            logger.error(f"Failed to save session: {e}")

    def clear_session(self):
        self.session_data = None
        self.current_user = None
        if os.path.exists(SESSION_FILE):
            os.remove(SESSION_FILE)

    def is_authenticated(self):
        if not self.current_user: return False
        if self.session_data:
            created_at = datetime.fromisoformat(self.session_data.get('created_at', ''))
            if (datetime.now() - created_at).days >= SESSION_TIMEOUT_DAYS:
                self.clear_session()
                return False
        return True

    def get_current_user(self):
        return self.current_user

    def logout(self):
        try:
            if self.session_data and self.session_data.get('session_id'):
                self._request('DELETE', f"/account/sessions/{self.session_data['session_id']}")
        except: pass
        self.clear_session()
        return True, "Logged out successfully"

    def check_username_exists(self, username):
        try:
            success, result = self._request('GET',
                f'/databases/{self.database_id}/collections/{APPWRITE_USERS_COLLECTION}/documents?queries=[username="{username}"]')
            return len(result.get('documents', [])) > 0 if success else False
        except: return False

    def check_email_exists(self, email):
        try:
            success, result = self._request('GET', '/users')
            if success:
                for user in result.get('users', []):
                    if user.get('email') == email: return True
            return False
        except: return False

    def get_user_by_username_or_email(self, username_or_email):
        try:
            success, result = self._request('GET',
                f'/databases/{self.database_id}/collections/{APPWRITE_USERS_COLLECTION}/documents?queries=[username="{username_or_email}"]')
            if success and len(result.get('documents', [])) > 0:
                user_id = result['documents'][0].get('userId')
                s, u = self._request('GET', f'/users/{user_id}')
                if s: return u
            success, result = self._request('GET', '/users')
            if success:
                for user in result.get('users', []):
                    if user.get('email') == username_or_email: return user
            return None
        except: return None

    # ==========================================
    # VERIFY EMAIL (Fixed - creates doc if missing)
    # ==========================================
    def verify_email(self, code):
        if not self.current_user: return False, "Not logged in"

        user_id = self.current_user.get('id')
        user_email = self.current_user.get('email')

        try:
            # Try to find existing document
            success, result = self._request('GET',
                f'/databases/{self.database_id}/collections/{APPWRITE_USERS_COLLECTION}/documents?queries=[userId="{user_id}"]')

            if success and len(result.get('documents', [])) > 0:
                # Update existing document
                doc_id = result['documents'][0].get('$id')
                self._request('PATCH',
                    f'/databases/{self.database_id}/collections/{APPWRITE_USERS_COLLECTION}/documents/{doc_id}',
                    {'data': {'verified': True}})
            else:
                # Create new document
                self._request('POST',
                    f'/databases/{self.database_id}/collections/{APPWRITE_USERS_COLLECTION}/documents',
                    {'documentId': user_id,
                     'data': {'userId': user_id, 'username': self.current_user.get('username', ''),
                              'fullName': self.current_user.get('name', ''), 'email': user_email,
                              'verified': True, 'createdAt': datetime.now().isoformat()}})

            # Update local session
            self.current_user['verified'] = True
            if self.session_data: self.session_data['user']['verified'] = True
            self.save_local_session(self.current_user, self.session_data.get('session_id') if self.session_data else None)
            return True, "Email verified successfully"
        except Exception as e:
            return False, str(e)

    # ==========================================
    # CHANGE PASSWORD
    # ==========================================
    def change_password(self, email, old_password, new_password):
        try:
            user = self.get_user_by_username_or_email(email)
            if not user: return False, "User not found"
            user_id = user.get('$id')

            success, resp = self._request('POST', '/account/sessions/email', {'email': email, 'password': old_password})
            if not success: return False, "Current password is incorrect"

            success, _ = self._request('PATCH', f'/users/{user_id}/password', {'password': new_password})
            if success:
                return True, "Password changed successfully"
            return False, "Failed to update password"
        except Exception as e:
            return False, str(e)

    # ==========================================
    # UPDATE PROFILE
    # ==========================================
    def update_profile(self, user_id=None, name=None, username=None):
        if not user_id: user_id = self.current_user.get('id') if self.current_user else None
        if not user_id: return False, "User not found"

        try:
            if name: self._request('PUT', f'/users/{user_id}', {'name': name})

            db_data = {}
            if name: db_data['fullName'] = name
            if username: db_data['username'] = username

            if db_data:
                success, result = self._request('GET',
                    f'/databases/{self.database_id}/collections/{APPWRITE_USERS_COLLECTION}/documents?queries=[userId="{user_id}"]')
                if success and len(result.get('documents', [])) > 0:
                    doc_id = result['documents'][0].get('$id')
                    self._request('PATCH',
                        f'/databases/{self.database_id}/collections/{APPWRITE_USERS_COLLECTION}/documents/{doc_id}',
                        {'data': db_data})

            if name: self.current_user['name'] = name
            if username: self.current_user['username'] = username
            self.save_local_session(self.current_user, self.session_data.get('session_id') if self.session_data else None)
            return True, "Profile updated successfully"
        except Exception as e:
            return False, str(e)

    # ==========================================
    # SIGNUP + LOGIN
    # ==========================================
    def signup(self, full_name, email, username, password):
        if self.check_username_exists(username): return False, "Username already exists"
        if self.check_email_exists(email): return False, "Email already registered"

        user_id = secrets.token_hex(16)
        success, resp = self._request('POST', '/users', {'userId': user_id, 'email': email, 'password': password, 'name': full_name})
        if not success: return False, f"User creation failed: {resp}"

        # Create document (non-critical)
        self._request('POST', f'/databases/{self.database_id}/collections/{APPWRITE_USERS_COLLECTION}/documents',
            {'documentId': user_id,
             'data': {'userId': user_id, 'username': username, 'fullName': full_name,
                      'email': email, 'verified': False, 'createdAt': datetime.now().isoformat()}})

        user_info = {'id': user_id, 'name': full_name, 'email': email, 'username': username, 'verified': False}
        self.save_local_session(user_info)
        return True, "Account created successfully"

    def login(self, username_or_email, password):
        user = self.get_user_by_username_or_email(username_or_email)
        if not user: return False, "User not found"

        success, resp = self._request('POST', '/account/sessions/email', {'email': user['email'], 'password': password})
        if not success: return False, "Invalid credentials"

        user_id = user['$id']
        user_info = {'id': user_id, 'email': user['email'], 'name': user.get('name', ''), 'username': username_or_email, 'verified': False}

        success, docs = self._request('GET',
            f'/databases/{self.database_id}/collections/{APPWRITE_USERS_COLLECTION}/documents?queries=[userId="{user_id}"]')
        if success and docs.get('documents'):
            d = docs['documents'][0]['data']
            user_info['username'] = d.get('username', username_or_email)
            user_info['verified'] = d.get('verified', False)

        self.save_local_session(user_info, resp.get('$id'))
        return True, "Login successful"


auth = AppwriteAuth()
