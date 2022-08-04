from abc import ABC, abstractmethod
tot_proj=0
import time
from enum import Enum
from datetime import date
import random
class project_status(Enum):
	CREATED = 1
	ASSIGNED = 2
	PROGRESSING = 3
COMPLETED = 4



class team :
    def __init__(self,teammember):
        self.name=teammember
        self.status = project_status.PROGRESSING
    def viewProject(self):
        pass
    def checkTimeLine(self):
        pass


class projectCreation(ABC): #only limited to admin and team manager
    def __init__(self):
        global tot_proj
        self.projId=tot_proj
        self.projName=None
        self.projMember=[]
        self.__projTimeline = None
        self.status = project_status.CREATED

        tot_proj+=1

    def setProjectedTimeLine(self,projTimeline):
        self.__projTimeline = projTimeline
        return

    def getRemainingTimeLine(self):
        return (time.getself.__projTimeline -date.today())

        #self.totProj= x+=1

    def createNewProject(self,projName,projMember):
        self.projName = projName
        self.projMember = self.projMember.append(projMember)

        self.timecreation = time.time()
    def _deleteProj(self,projectId):
        if self.projId == projectId and self.status == project_status.COMPLETED:
            del project
            global tot_proj
            tot_proj -=1


class projectVisiblityClass: #visible for all
    @abstractmethod
    def viewAllProject(self):
        global tot_proj
        for project_id in range(tot_proj):
            """print all project details"""
            pass

    @abstractmethod
    def projDetails(self):
        print(self.projName,self.projMember,self.projTimeline)



class projectManager(projectCreation,projectVisiblityClass):

    def allotProjForteamMember(self,teammemberName):
        self.status = project_status.ASSIGNED
        pass
    def viewProject(self):
        pass
    def checkTimeLine(self):
        pass
    def modifyProjDetails(self):
        pass



class admin(projectCreation,projectVisiblityClass):

    def createProj(self):
        self.__init__()
    def viewAllProj(self):
        pass
    def _deleteProj(self,projId):
        pass





""""
create a new projectAccessClass for using all (admin, team member , team manager)

create a new projectCreationClass  for only admin.

create a new projectUpdateClass for admin and team manager


"""



ad =admin()
ad.createProj()
ad.projDetails()
