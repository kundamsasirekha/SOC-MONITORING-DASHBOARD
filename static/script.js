// ===============================
// SOC Monitoring Dashboard Script
// ===============================

// Logout Confirmation
function confirmLogout() {

    let result = confirm("Are you sure you want to logout?");

    if (result) {
        window.location.href = "/logout";
    }

    return false;
}


// Welcome Message
window.onload = function () {

    console.log("Employee Login Monitoring System Loaded Successfully");

};


// Notification Alert
function showNotification(message) {

    alert(message);

}


// Save Profile Success
function profileSaved() {

    alert("Profile Saved Successfully");

}


// Change Password Success
function passwordChanged() {

    alert("Password Updated Successfully");

}


// Future Functions

function refreshDashboard() {

    location.reload();

}