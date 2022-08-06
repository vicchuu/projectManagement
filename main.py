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



# class teamVisisblity :
#     def __init__(self,teammember):
#         self.name=teammember
#         self.status = project_status.PROGRESSING
#     def viewProject(self):
#         pass
#     def checkTimeLine(self):
#         pass


class projectCreation(ABC): #only limited to admin and team manager
    @abstractmethod
    def __init__(self): #initiating a new project
        """
        constructor for creating a empty project structire which holds all attributes in commmon ,
        with few public and private attribs
        """
        global tot_proj
        self.projId=tot_proj
        self.projName=None
        self.projMember=[]
        self.__projTimeline = None
        self.timecreation = None
        self.status = project_status.CREATED

        tot_proj+=1
        #super().__init__()
        print("Obj created")



    @abstractmethod
    def _createNewProject(self,projName,projMember,lastDate):
        """
        creation of new project name and details
        :param projName:  pro name
        :param projMember: [porj memnbers assign with the project ]
        :param lastDate: last date of the project
        :return: no retuen AS ONLy logged its success creation
        """
        self.projName = projName
        self.projMember = self.projMember.append(projMember)

        self.timecreation = time.time()
        self.__projTimeline = lastDate-self.timecreation
        self.status = project_status.PROGRESSING
        print("new proj createdwith name :",projName)
        print("Timeline to close the project is :",self.__projTimeline)
        print("Including team member's ",projMember," On time :",self.timecreation)


    @abstractmethod
    def _deleteProj(self,projectId):
        """
              To delete project and neeed to know about the project detail completed and stauts must be completed
              :param projId: projId is needed to find particular project
              :return: no return
        """
        if self.projId == projectId and self.status == project_status.COMPLETED:
            #del project
            global tot_proj
            tot_proj -=1
        print("sucessfully deleted a project")

    def getProjectdetails(self,projId):
        """
              To check current project and neeed to know about the project detail
              :param projId: projId is needed to find particular project
              :return: return a list , containing all details about the project
              """
        return [self.projId, \
        self.projName, \
        self.projMember, \
        self.__projTimeline ,\
        self.status]


class modifyProj(projectCreation):

    def __init__(self):
        pass

    def modfifyProjectDetail(self,projId,projName,projMember,newTimeline,status):
        """
        Method is so powerfull to use or enhance to proj details
        :param projId: Proj Id is mandatory
        :param projName:  name of the project
        :param projMember: [list of new proj Member]
        :param newTimeline: new timeline
        :param status: change the status oof of sstatus
        :return:  return the proj Id
        """
        proj = super().getProjectdetails(projId=projId)

        #change in new project details
        return proj



class projectVisiblityClass(projectCreation): #visible for all

    def viewAllProject(self):
        """
        returen all avalilabel projet created
        :return:  list of project details
        """
        global tot_proj
        for project_id in range(tot_proj):
            """print all project details"""
            pass
    def viewParticularproj(self,projId):
        """
           To check current project and neeed to know about the project detail
           :param projId: projId is needed to find particular project
           :return: return a list , containing all details about the project
           """
        return super().getProjectdetails(projId=projId)

    def checkTimeline(self,projId):
        """
        e=method find its timielone wrt proj id
        :param projId: projId is mandatory for fetching particular proj
        :return:  no return
        """
        proj = super().getProjectdetails()
        #check project time line


    @abstractmethod
    def modeifiedProjDetails(self):
        print(self.projName,self.projMember,self.projTimeline)



class projectManager(projectCreation):

    def __init__(self):
        pass
    def allotProjForteamMember(self,projId,teammemberName):
        """
        A project manager os responsible for alloting team members to its super class
        :param projId:  projId is mandatory for fetching particular proj
        :param teammemberName:  assigned a list of team members to pariticular project
        :return:
        """
        self.status = project_status.ASSIGNED

        pass

    def checkProject(self, projId):
        """
        check partucular proj with wrt to proj ID
        :param projId:  projId is mandatory for fetching particular proj
        :return: list of detail related to project
        """
        super().viewParticularproj(projId=projId)

    def checkTimeLine(self, projId):
        """
        To check remaining time line
        :param projId: proj Id is needed to fetch proj
        :return: estimated timeline as string
        """
        super().checkTimeline(projId=projId)

    def modifyProjDetails(self,projId,projName,projMember,newTimeline,status):
        """
        modify the project with concerned project and details
        :param projId:  to fetch particular project
        :return: no return
        """
        super().modfifyProjectDetail(projId=projId,projName=projName,projMember=projMember,newTimeline=newTimeline,status=status)

    def setProjectedTimeLine(self,projId, projTimeline):
        """
          Project manager can set desired timeline
        :param projId:  for particular projOD
        :param projTimeline:  new timeline
        :return: no return
        """

        self.__projTimeline = projTimeline
        return

    def _createNewProject(self, projName, projMember):
        """
        Project manager can create a new project by calling its super class
        :param projName:  name of project
        :param projMember:  a list of team members
        :return:  no return
        """
        super()._createNewProject(projName,projMember)
    def getRemainingTimeLine(self,projId):
        """
        A project manager can find remaining timeline by calling this method for his team members
        :return: remining timeline
        """
        return super().checkTimeline(projId=projId)



class admin(projectCreation):

    def __init__(self):
        #super().__init__()
        pass
    def createProj(self):
        """
        Admin can create a new project by calling its super class project creation constructor
        :return: no return
        """
        super().__init__()

    def viewAllProj(self):
        """
        Admin can check all project details , which created before
        :return: a list of array sequential order
        """
        super().viewAllProject()

    def _createNewProject(self, projName, projMember):
        """
        Admin can create a new project to DB , assigned to particular team
        :param projName:  defining a project name
        :param projMember:  it defines a list of projct members to team
        :return: print sucessfull message
        """
        super()._createNewProject(projName,projMember)
        #pass
    def _deleteProj(self,projId):
        """
        Admin method can delete a project from DB , when may be finished or wrongly created
        :param projId: projId is needed to find particular project
        :return:  no return
        """
        super()._deleteProj(projId=projId)
        #pass

class teamMember(projectVisiblityClass):
    def __init__(self):
        pass

    def checkProject(self,projId):
        """
        To check current project and neeed to know about the project detail
        :param projId: projId is needed to find particular project
        :return: return a list , containing all details about the project
        """
        super().viewParticularproj(projId=projId)
    def checkTimeLine(self,projId):
        """
        method will check the remaining timeline and from current time
        :param projId: projId is needed to find particular project
        :return: remining date or timeline  return in string
        """
        super().checkTimeline(projId=projId)
    def changeProjStatus(self,projId):
        """
        After completing all project workss he can change the project status from progressing to complete
        :param status: project Id is needed to find the project and change desired status
        :return:  nothing
        """
        pass






""""
create a new projectAccessClass for using all (admin, team member , team manager)

create a new projectCreationClass  for only admin.

create a new projectUpdateClass for admin and team manager


"""

# ad =admin()
# ad.createProj()
# ad._createNewProject(projName="python soon" , projMember=["vishnu", "google"])
# ad._deleteProj(1)

# lets check with team managers

#mg = projectManager()


