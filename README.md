# projectManagement
OOP model for project management \

3 - Actor is used 

    1) Admin - who can access all database permission and has actions of followings
        a)create a new project
        b)modify the project
        c)view all project
        d)check timeline
        e) del project

    2) Team manager - who has little permission in application , those are
        a)assign project to particular team member
        b)Add timeline
        c)view all project
        d)check timeline

    3) Team member -  has permission to follow up above hierarchy
        a) view all project
        b) check timeline



create a new projectVisiblityClass for using all (admin, team member , team manager)

create a new projectCreation Class  for only admin.

create a new projectUpdateClass for admin and team manager


how  they are access each other in terms of using SOLID principle and any patterns used , will follow up in next commit



