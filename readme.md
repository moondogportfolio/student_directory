## Description

- A student directory and administration app for the Guidance Office of the Cavite State University Indang.
- Displays basic student information as well as violations committed.
- Administrator can add violation records.
- Can generate a printable Certificate of Good Moral Character if a student has no violations on record.

## Technical
- GUI is a collaborative effort between the Jinja2 templating system and Vue.
- Was originally connected to a MongoDB database, but for the sake of demonstration, pertinent code has been commented out and replaced by in-memory data. Will still work if commented data is restored.
- Server is handled by the Flask library, and is written in Python.
- 
[Link](https://studentdirectory.onrender.com/)