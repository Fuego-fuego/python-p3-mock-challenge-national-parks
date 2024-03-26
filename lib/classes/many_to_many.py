from collections import Counter
class NationalPark:
    all = []
    def __init__(self, name):
        self.name = name
        NationalPark.all.append(self)
            
    def trips(self):
        return [trip for trip in Trip.all if trip.national_park == self]
    
    def visitors(self):
        all_trips = self.trips()
        unique_visitors_list = []
        
        for trip in all_trips:
            if not (trip.visitor in unique_visitors_list):
                unique_visitors_list.append(trip.visitor)
        return unique_visitors_list
    
    def total_visits(self):
        total_trips_to_park = self.trips()
        return len(total_trips_to_park)
    
    def best_visitor(self):
        total_trips_to_park = self.trips()
        if len(total_trips_to_park) < 1:
            return None
        else:
            visitors = [trip.visitor for trip in total_trips_to_park]      
            
        all_visitor_name = []
        for visitor in visitors:
            all_visitor_name.append(visitor.name)
        
        # print(all_visitor_name)
        highest_visitor_name =  NationalPark.highest_occurrence(all_visitor_name)[0]
        best_visitor_obj = NationalPark.find_object_by_name(visitors,highest_visitor_name)
        
        print(best_visitor_obj.name)
        return best_visitor_obj
    
    def highest_occurrence(lst):
        counts = Counter(lst)    
    
        max_count = max(counts.values())    
    
        highest_occurrences = [item for item, count in counts.items() if count == max_count]    
        return highest_occurrences   
    
    def find_object_by_name(objects, name):
        for obj in objects:
            if hasattr(obj, 'name') and obj.name == name:
                return obj
        return None 
        
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,park_name):
        if hasattr(self, '_name'):
            raise AttributeError("cannot change the name of the national_park.")
        else:
            if isinstance(park_name,str) and  len(park_name) > 2:
                self._name = park_name
            else:
                raise TypeError("Names must be of type `str`.Names length must be greater or equal to 3 characters")

class Trip:
    all = []
    def __init__(self, visitor, national_park, start_date, end_date):
        self.visitor = visitor
        self.national_park = national_park
        self.start_date = start_date
        self.end_date = end_date
        Trip.all.append(self)

    @property
    def national_park(self):
        return self._national_park
    @national_park.setter
    def national_park(self,national_park_obj):
        if isinstance(national_park_obj, NationalPark):
            self._national_park = national_park_obj
        else:
            raise TypeError("National park must be an instance of the NationalPark class.")
        
    @property
    def visitor(self):
        return self._visitor
    @visitor.setter
    def visitor(self,visitor_obj):
        if isinstance(visitor_obj, Visitor):
            self._visitor = visitor_obj
        else:
            raise TypeError("Visitor must be an instance of the Visitor class.")
        
    @property
    def start_date(self):
        return self._start_date
    
    @start_date.setter
    def start_date(self,date):
        print(isinstance(date,str))
        if isinstance(date, str) and len(date) > 6:            
            if(Trip.is_valid_date_format(date)):
                self._start_date = date
            else:
                raise TypeError("date should be in the format September 1st")
        else:
            raise TypeError("Names must be of type `str`.Names must be greater than 6 character in length")    
    
        
    @property
    def end_date(self):
        return self._end_date
    
    @end_date.setter
    def end_date(self,date):
        if isinstance(date,str) and len(date) > 6:            
            if(Trip.is_valid_date_format(date)):
                self._end_date = date
            else:
                raise TypeError("date should be in the format September 1st")
        else:
            raise TypeError("Names must be of type `str`.Names must be greater than 6 character in length")
    
    @classmethod
    def is_valid_date_format(cls,date_string):
        months = ["January", "February", "March", "April", "May", "June", "July",
              "August", "September", "October", "November", "December"]
    
        parts = date_string.split()
        if len(parts) != 2:
            return False
    
        month, day = parts
        if month not in months:
            return False
    
        if not day[:-2].isdigit() or day[-2:] not in ["st", "nd", "rd", "th"]:
            return False
    
        day_number = int(day[:-2])
        if day_number < 1 or day_number > 31:
            return False
    
        return True


class Visitor:
    all=[]
    def __init__(self, name):
        self.name = name
        Visitor.all.append(self)
        
    
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,visitor_name):
        if isinstance(visitor_name,str) and 0 < len(visitor_name) < 16:
            self._name = visitor_name
        else:
            raise TypeError("Names must be of type `str`.Names must be between 1 and 15 characters, inclusive")
        
        
    def trips(self):
        return [trip for trip in Trip.all if trip.visitor == self ]
    
    def national_parks(self):
        all_trips = self.trips()
        unique_parks_list = []
        
        for trip in all_trips:
            if not (trip.national_park in unique_parks_list):
                unique_parks_list.append(trip.national_park)
        return unique_parks_list
    
    def total_visits_at_park(self, park):
        pass
    
    
# v1 = Visitor("steve")
# print(v1.name)


lst = ["ben","ben","ben","Hen","Hen","Ken"]


print (NationalPark.highest_occurrence(lst))