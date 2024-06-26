#!/usr/bin/python3
"""Contains Database class for working with stylemate database"""

from models.bottom import Bottom
from models.top import Top
from models.user import User
from models.base import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class Database:
    """Database class with useful methods for working with stylemate database"""

    table_classes = {"tops": Top, "bottoms": Bottom, "user": User}

    def __init__(self, username, password):
        """Object instatiation"""
        self.__engine__ = create_engine("mysql://{}:{}@localhost/stylemate_db".
                                        format(username, password))
        Base.metadata.create_all(self.__engine__)
        Session = sessionmaker(bind=self.__engine__)
        self.__session__ = Session()

    def get_all_cty(self, table_name):
        """Return list of all clothing item categories in given table"""
        if table_name not in Database.table_classes.keys():
            return ("'{}' table does not exist".format(table_name))
        cty_result = self.__session__.query(Database.table_classes.get(table_name)).all()
        cty_list = []
        for cty in cty_result:
            cty_list.append(cty.name)
        return (cty_list)

    def get_cty_numbers(self, table_name):
        """Return dictionary of all clothing item categories in given table and their numbers"""
        if table_name not in Database.table_classes.keys():
            return ("'{}' table does not exist".format(table_name))
        cty_result = self.__session__.query(Database.table_classes.get(table_name)).all()
        cty_dict = {}
        for cty in cty_result:
            cty_dict.update({cty.name: cty.number})
        return (cty_dict)

    def close_session(self):
        """Close current session"""
        self.__session__.close()

    def add_cty(self, cty, table_name):
        """
        Add a clothing item category to a table; accepts dictionary
        Sample input: {'name': 'shirt', 'number': 5}
        """
        if table_name not in Database.table_classes.keys():
            return ("'{}' table does not exist".format(table_name))
        possible_dup = self.__session__.query(Database.table_classes.get(table_name))\
                       .filter_by(name=cty.get('name')).first()
        if possible_dup is None:
            self.__session__.add(Database.table_classes.get(table_name)(**cty))
            self.__session__.commit()
        else:
            for key, value in cty.items():
                setattr(possible_dup, key, value)
            self.__session__.commit()
        return_result = self.__session__.query(Database.table_classes.get(table_name))\
            .filter_by(name=cty.get('name')).first()
        return([return_result.name, return_result.number])

    def get_user_sex(self):
        """Gets the gender of the user"""
        result = self.__session__.query(Database.table_classes.get("user")).first()
        return (result.sex)

    def get_user_name(self):
        """Gets the name of the user"""
        result = self.__session__.query(Database.table_classes.get("user")).first()
        return (result.name)

    def get_cty(self, cty_name):
        """Return description dictionary of a clothing item category"""
        cty_result = self.__session__.query(Database.table_classes.get("tops")).all()
        for cty in cty_result:
            if cty.name == cty_name:
                return ({cty.name: cty.number})
        else:
            cty_result = self.__session__.query(Database.table_classes.get("bottoms")).all()
            for cty in cty_result:
                if cty.name == cty_name:
                    return ({cty.name: cty.number})
            else:
                return ("User does not have any '{}'".format(cty_name))

    def delete_cty(self, table_name, cty_name):
        """Delete a particular category in a table"""
        if table_name not in Database.table_classes.keys():
            return ("'{}' table does not exist".format(table_name))
        cty_result = self.__session__.query(Database.table_classes.get(table_name)).all()
        for cty in cty_result:
            if cty.name == cty_name:
                self.__session__.delete(cty)
                self.__session__.commit()
                return ({})
        else:
            return ("User does not have any '{}'".format(cty_name))

    def no_of_items(self):
        """Return dictionary containing number of items in total in user wardrobe"""
        return_dict = {
            "tops": 0,
            "bottoms": 0
            }
        cty_result = self.__session__.query(Database.table_classes.get("tops")).all()
        for item in cty_result:
            return_dict["tops"] += item.number
        cty_result = self.__session__.query(Database.table_classes.get("bottoms")).all()
        for item in cty_result:
            return_dict["bottoms"] += item.number
        return (return_dict)

    def set_user(self, dict):
        """Set name and sex of user in database table user"""
        if len(dict['name']) == 0:
            return("Name field empty. Please fill.")
        if int(dict['age']) == 0:
            return ("Please input valid age")
        present_users = self.__session__.query(Database.table_classes.get("user")).all()
        for user in present_users:
            self.__session__.delete(user)
        self.__session__.commit()
        new_user = Database.table_classes.get("user")(**dict)
        self.__session__.add(new_user)
        self.__session__.commit()
        print(dict)
        return ("User info updated")


