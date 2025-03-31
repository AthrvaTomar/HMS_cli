
# Hostel Management System

A Hostel Management System helps manage a hostel efficiently. It allows warden login, student registration, student login and visitor logs. Wardens can approve room requests, check fees, handle issues, issue fines, and manage visitors. Students can request rooms, pay fees and fines, and report issues. Visitor details include names and entry/exit times. This system improves efficiency and reduces mistakes.

## Roles 

* Hostel Warden
* Students
* Visitor

## Register / Login

* Warden login
    * checks the credentials of warden and redirects to warden dashboard
* Student registration
    * allows students to register themselves on the portal
* Student login
    * checks the credentials of student and redirects to student dashboard
* Visitors (without authentication)
    * allows visitors to give prior information of their visit so that easy communication can be established

## Warden Dashboard

### View 
These are the values the warden will be able to see at warden dashboard after login.

* Number of students
* Number of total rooms
* Number of Occupied rooms
* Number of students on waiting list
* Number of students with fines
* Number of Issues Raised
* Number of room change requests

### Features
These are the features(functions) given to warden for smooth operations.

* Approve room requests
    * after checking the details of students
* Check waiting list
    * Check which students are left on the waiting list
* Change room
    * Change the room of students if needed
* Check on student issues
    * See detailed report of issues
* Issue fine
    * put fine on students in case of misconduct
* See number of visitors by date/month/year
    * helps keep record of visitors and look them up
* Search students by room and vis-versa
    * to see which room has been alloted to which student and vis-versa

## Student Dashboard

### View
These are the values the student will be able to see at student dashboard after login.

* Request status 
    * request : unpaid fees/paid fees/Number in waiting list/approved
    * leave : unpaid fine/paid fine/approved
* Allocated room (not Allocated/room Number)
* Fine Due

### Features
These are the features(functions) given to student for smooth communication.

* Request room
    * This will generate a request for room and send it to wrden for approval 
* Pay fees
    * Allows student to pay thier fees
* Pay fine
    * Allows student to pay their fine
* Raise issues
    * To raise anonymous issue that the student is facing 
* Change room request
    * Allows student to rquest for a change of room
* Leave room request
    * Help student to generate request to vacate the room
* Read Code of Conduct
    * Allows students to read all the rules and guidelines of hostel

## Visitors
This will be the information a visitor will have to provide before coming for visit so that the warden can efficiently manage them.
max duration: 2 hours
max concurrent slot: 5

* Visitor Name
* student visited
* Entry date
* Entry time 
* Exit Date
* Exit time


### DB files
* visitor
* registered
* student
* rooms
* room request (allot/change/leave)
* waitlist
* issues
* code of conduct
