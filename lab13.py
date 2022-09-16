# Name: Amena Akbary
# Pledge : I pledge my honor that I have abided by the Stevens Honor System.
# 21fa-cs115bc
#
# lab13.py
#
# A.Nicolosi
# 20211201
#
# Practice with classes.

# TODO: Write a bare-bone class InvalidDateError that inherits from ValueError
# Your constructor should allow for up to three argument (for the month,
# day, and year).  Hint: recall the syntax for default parameter values.



# Fill in the missing part in the class Date below
class InvalidDateError(ValueError):
    def __init__(self, month, day, year):
        ValueError.__init__(self,month,day,year)
    def ValueError(month, day, year):
        if month > 0 and month <= 12 and day <= 31 and year > 0:
            return True
        else:
            return False
        
class Date(object):
    '''
    Date abstraction

    Demonstrate getter/setter methods and operator overloading
    '''

    daysInMonth = [31,          # not really using index 0 (dec of prev year)
                   31, 28, 31,  # jan, (non-leap) feb, mar
                   30, 31, 30,  # apr, may, jun
                   31, 31, 30,  # jul, aug, sep
                   31, 30, 31]  # oct, nov, dec


        # Every fourth year is a leap year,
        # except that every one-hundreth year it isn't,
        # but every four-hundreth year is a leap year after all!
        

    def __init__(self, month, day, year):
        # Call self.validate to ensure that the parameters
        # make a valid date.  Raise an InvalidDateError if not.
        # If all is good, initialize the attributes _month, _day, and
        # _year
        # 
        # TODO
        self.month = month
        self.day = day
        self.year = year
        if self.validate_params() == False:
            raise InvalidDateError
            
            
    def isLeapYear(self):
        if self.year % 400 == 0:
            return True
        elif self.year % 100 == 0:
            return False
        elif self.year % 4 == 0:
            return True
        return False
        
    def __repr__(self):
        # Make sure to return a string that looks like a valid
        # call to the class constructor
        # Ex: Date(12, 31, 2021)
        #
        # TODO
        return 'Date(%d,%d,%d)' % (self.month, self.day, self.year)
        

    def __str__(self):
        # Return a string in the format mm/dd/yyyy
        #
        # TODO
        return '%02d/%02d/%04d' % (self.month, self.day, self.year)
    
    
    def _validateCheckFeb29(self):
        return 2 == self.month and 29 == self.day and Date.isLeapYear()

    def validate_params(self):
        # Return True if m, d, y represent a valid date
        # Start by checking if that's a valid Feb 29 (see
        # helper above); then check if d is a valid day
        # in month m
        #
        daysInMonth = [31,          # not really using index 0 (dec of prev year)
                        31, 28 + self.isLeapYear(), 31,  # jan, (non-leap) feb, mar
                        30, 31, 30,  # apr, may, jun
                        31, 31, 30,  # jul, aug, sep
                        31, 30, 31]
                    
        if self._validateCheckFeb29() == True:
            if self.month >= 1 and self.month <= 12:
                if self.day >= 1 and self.day <= daysInMonth[m]:
                    return True
                else:
                    return False
            else:
                return False
        
        
    # Write getters and setters
    # TODO: get_month, get_day, get_year, set_month, set_day, set_year
    # NB: Setter should check that the resulting date is valid
    # *before* affecting the change
    
    def get_month(self):
        return self.month

    def get_day(self):
        # TODO
        return self.day

    def get_year(self):
        # TODO
        return self.year

    def set_month(self, month):
        # TODO
        self.month = month

    def set_day(self, day):
        # TODO
        self.day = day

    def set_year(self, year):
        # TODO
        self.year = year

    # Date arithmetic!

    def __eq__(self, other): #==
        # TODO
        if (self.year == other.year) and (self.month == other.month) and (self.day == other.day):
            return True
        else:
            return False

    def __ne__(self, other): #=/=
        # TODO
        return not(__eq__(self,other))

    def __lt__(self, other): #<
        # TODO
        if (self.year < other.year) or (self.month < other.month) or (self.day , other.day):
            return True
        else:
            return False

    def __ge__(self, other): #>=
        # TODO
        if (self.year >= other.year) or (self.month >= other.month) or (self.day >= other.day):
            return True
        else:
            return False

    def __le__(self, other): #<=
        # TODO
        if (self.year <= other.year) or (self.month <= other.month) or (self.day <= other.day):
            return True
        else:
            return False

    def __gt__(self, other): #>
        # TODO
        if (self.year > other.year) or (self.month > other.month) or (self.day > other.day):
            return True
        else:
            return False

    def __add__(self, deltaInDays): #+
        '''Computes the date following `self` by the specified number of days'''
        # TODO
        self.day = deltaInDays + self.day
        if self.validate_params() == True:
            return
        daysInMonth = [31,          # not really using index 0 (dec of prev year)
                        31, 28 + self.isLeapYear(), 31,  # jan, (non-leap) feb, mar
                        30, 31, 30,  # apr, may, jun
                        31, 31, 30,  # jul, aug, sep
                        31, 30, 31]
        while self.day > daysInMonth[self.month-1]:
            self.day = self.day - daysInMonth[self.month]
            self.month += 1
            if self.month > 12:
                self.year += 1
                self.month = 1
            
            
        
    
a = Date(12,29,2017)
a.__add__(4)
print(a)