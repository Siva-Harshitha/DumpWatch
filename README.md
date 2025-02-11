# DumpWatch

https://github.com/user-attachments/assets/7c4e4c7e-95fb-4595-88a5-72fc8e3b3f09

**“DUMPWATCH”**
It is regarding a "Garbage Collection Management System” that allows users to raise complaints (about garbage issues) and enables administrators to manage and resolve those complaints. The system also sends email notifications to users when their complaints are marked as resolved.

**Technologies Used**
1. Frontend
- HTML
- CSS
-Bootstrap
- JavaScript
- Leaflet.js
2. Backend
- Django.
- SQLite
- Django ORM
3. Email Integration
- Gmail SMTP
- Django Email Backend
  
**Features**
1. User Dashboard
    - Raise a Complaint
    - Users can fill out this form to submit a complaint.
    - This form includes fields for:
    - Name
    - Email
    - Location (here location is automatically fetched using Leaflet.js, The location coordinates (latitude and longitude) are automatically filled in the form.)
    - City
    - Date
    - Complaint description
    - Photo upload 
    The form is submitted, and the complaint is saved to the database.
    The user sees a confirmation message.
2. Admin Login
  - The admin must login to enter the Admin Dashboard.
3. Admin Dashboard
  - Admins can see a list of all complaints.
  -Here the admin can view details of each complaint, including the uploaded photo.
  - Admins can mark complaints as resolved.
  - When a complaint is marked as resolved, an email is sent to the user.
  - Admins can delete complaints from the system.
4. Email Notifications
 - When a complaint is marked as resolved, the system sends an email notification to the user's  
    provided email address with a confirmation message by thanking the user for their complaint and  
    informing them that it has been resolved.
