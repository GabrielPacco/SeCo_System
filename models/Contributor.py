#!/usr/bin/python
#-*- coding: utf-8 -*-

from Activity import Activity

class Contributor(Activity, Activity):
    def __init__(self):
        self.id = None
        self.name = None
        self.university = None
        self.speciality = None
        self.description = None
        self.email = None
        self.linkedin = None
        self.role = None

    def conductActivity(self, ):
        pass

