from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# ---------------- DATABASE ----------------

def create_tables():
    conn = sqlite3.connect("soc.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS profile(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT,
        phone TEXT,
        department TEXT
    )
    """)

    conn.commit()
    conn.close()

create_tables()

# ---------------- HOME ----------------

@app.route("/")
def home():
    return render_template("index.html")


# ---------------- LOGIN PAGES ----------------

@app.route("/admin-login")
def admin_login():
    return render_template("admin_login.html")


@app.route("/user-login")
def user_login():
    return render_template("user_login.html")


# ---------------- ADMIN LOGIN ----------------

# ---------------- ADMIN LOGIN ----------------

ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "admin123"

@app.route("/admin-auth", methods=["POST"])
def admin_auth():

    username = request.form.get("username", "").strip()
    password = request.form.get("password", "").strip()

    if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
        return redirect("/admin-dashboard")

    return """
    <script>
    alert("Invalid Username or Password");
    window.location.href="/admin-login";
    </script>
    """


# ---------------- USER LOGIN ----------------

@app.route("/user-auth", methods=["POST"])
def user_auth():

    username = request.form.get("username", "").strip()

    if username:
        return redirect("/user-dashboard")

    return """
    <script>
    alert("Please Enter Username");
    window.location.href="/user-login";
    </script>
    """


# ---------------- DASHBOARDS ----------------

@app.route("/admin-dashboard")
def admin_dashboard():
    return render_template("admin_dashboard.html")


@app.route("/user-dashboard")
def user_dashboard():

    conn = sqlite3.connect("soc.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM profile LIMIT 1")
    data = cursor.fetchone()

    conn.close()

    return render_template("user_dashboard.html", data=data)


# ---------------- ADMIN PAGES ----------------

@app.route("/users")
def users():
    return render_template("users.html")


@app.route("/logs")
def logs():
    return render_template("logs.html")


@app.route("/alerts")
def alerts():
    return render_template("alerts.html")


@app.route("/analytics")
def analytics():
    return render_template("analytics.html")


@app.route("/settings")
def settings():
    return render_template("settings.html")


# ---------------- PROFILE ----------------

@app.route("/profile")
def profile():

    conn = sqlite3.connect("soc.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM profile LIMIT 1")
    data = cursor.fetchone()

    conn.close()

    return render_template("profile.html", data=data)


@app.route("/save-profile", methods=["POST"])
def save_profile():

    name = request.form.get("name")
    email = request.form.get("email")
    phone = request.form.get("phone")
    department = request.form.get("department")

    conn = sqlite3.connect("soc.db")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM profile")

    cursor.execute("""
        INSERT INTO profile(name,email,phone,department)
        VALUES(?,?,?,?)
    """, (name, email, phone, department))

    conn.commit()
    conn.close()

    return """
    <script>
    alert("Profile Saved Successfully");
    window.location.href="/profile";
    </script>
    """
# ---------------- USER PAGES ----------------

@app.route("/login-history")
def login_history():
    return render_template("login_history.html")


@app.route("/notifications")
def notifications():
    return render_template("notification.html")


# ---------------- CHANGE PASSWORD ----------------

@app.route("/change-password")
def change_password():
    return render_template("change_password.html")


@app.route("/update-password", methods=["POST"])
def update_password():

    old_password = request.form.get("old_password")
    new_password = request.form.get("new_password")
    confirm_password = request.form.get("confirm_password")

    if old_password == "" or new_password == "" or confirm_password == "":
        return """
        <script>
        alert("Please Fill All Fields");
        window.location.href="/change-password";
        </script>
        """

    if new_password != confirm_password:
        return """
        <script>
        alert("New Password and Confirm Password do not match");
        window.location.href="/change-password";
        </script>
        """

    return """
    <script>
    alert("Password Updated Successfully");
    window.location.href="/change-password";
    </script>
    """


# ---------------- LOGOUT ----------------
@app.route("/logout")
def logout():
    return redirect("/")

# ---------------- RUN ----------------

if __name__ == "__main__":
    app.run(debug=True)
