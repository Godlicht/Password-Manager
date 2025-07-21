<h1>Password Manager</h1>

This is a simple password manager with a graphical interface built using Tkinter.  
It allows you to:
- Generate secure random passwords
- Store website login data (address, username, password)
- Automatically encrypt passwords using Fernet encryption (from `cryptography`)
- Open saved addresses in a browser
- Copy usernames and passwords to clipboard

---

<h2>Requirements</h2>

<ul>
  <li>Python 3.13+</li>
</ul>

---

<h2>Used Python Libraries</h2>

<ul>
  <li>tkinter</li>
  <li>secrets</li>
  <li>string</li>
  <li>json</li>
  <li>os</li>
  <li>webbrowser</li>
  <li>cryptography</li>
</ul>

---

<h2>How to Run</h2>

<pre>
git clone https://github.com/godlicht/password-manager.git
cd password-manager
pip install cryptography
python "Password Manager.py"
</pre>

---

<h2>Notes</h2>

- Passwords are encrypted using `cryptography.fernet` before being saved to `passwords.json`.
- The encryption key is automatically generated and saved as `secret.key` on the first run.
- Saved passwords are decrypted and displayed only inside the app.
