# epai-session10

## Problem statement
1. Use Faker library to get 10000 random profiles. Using namedtuple, calculate the largest blood type, mean-current_location, oldest_person_age and average age (add proper doc-strings). - 250
2. Do the same thing above using a dictionary. Prove that namedtuple is faster. - 250

The driver notebook for 1. and 2. is DriverProfile.ipyb

## Conclusion
### From the logs above the time taken by namedtuple is less than dict
| Task | Time taken by namedtuple | Time taken by dict |
| --- | --- | --- |
| Largest Blood group | 0.003495931625366211 | 0.00608515739440918 |
| Mean current location | 0.008796215057373047 | 0.009984016418457031 |
| Oldest person age | 0.02734375 | 0.03199577331542969 |
| Average age | 0.020982027053833008 | .0.024750947952270508 |

### NamedTuple

Help on class Profile in module NamedTuple:
class Profile(builtins.tuple)
 |  Profile(job, company, ssn, residence, current_location, blood_group, website, username, name, sex, address, mail, birthdate)
 |  
 |  Profile namedtuple that contains the fake profile fields generated by faker library
 |  
 |  Method resolution order:
 |      Profile
 |      builtins.tuple
 |      builtins.object
 |  
 |  Methods defined here:
 |  
 |  __getnewargs__(self)
 |      Return self as a plain tuple.  Used by copy and pickle.
 |  
 |  __repr__(self)
 |      Return a nicely formatted representation string
 |  
 |  _asdict(self)
 |      Return a new dict which maps field names to their values.
 |  
 |  _replace(self, /, **kwds)
 |      Return a new Profile object replacing specified fields with new values
 |  
 |  ----------------------------------------------------------------------
 |  Class methods defined here:
 |  
 |  _make(iterable) from builtins.type
 |      Make a new Profile object from a sequence or iterable
 |  
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |  
 |  __new__(_cls, job, company, ssn, residence, current_location, blood_group, website, username, name, sex, address, mail, birthdate)
 |      Create new instance of Profile(job, company, ssn, residence, current_location, blood_group, website, username, name, sex, address, mail, birthdate)
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  job
 |      Job designation of the person
 |  
 |  company
 |      Company where the person is employed in
 |  
 |  ssn
 |      Social security number of the person
 |  
 |  residence
 |      Residence of the person
 |  
 |  current_location
 |      Current location coordinates (latitude, longitude) of the person
 |  
 |  blood_group
 |      Blood group of the person
 |  
 |  website
 |      List of websites of the person
 |  
 |  username
 |      username of the person
 |  
 |  name
 |      Name of the person
 |  
 |  sex
 |      Gender of the person
 |  
 |  address
 |      address of the person
 |  
 |  mail
 |      E-mail address of the person
 |  
 |  birthdate
 |      birthdate of the person
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |  
 |  _field_defaults = {}
 |  
 |  _fields = ('job', 'company', 'ssn', 'residence', 'current_location', '...
 |  
 |  _fields_defaults = {}
 |  
 |  ----------------------------------------------------------------------
 |  Methods inherited from builtins.tuple:
 |  
 |  __add__(self, value, /)
 |      Return self+value.
 |  
 |  __contains__(self, key, /)
 |      Return key in self.
 |  
 |  __eq__(self, value, /)
 |      Return self==value.
 |  
 |  __ge__(self, value, /)
 |      Return self>=value.
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __getitem__(self, key, /)
 |      Return self[key].
 |  
 |  __gt__(self, value, /)
 |      Return self>value.
 |  
 |  __hash__(self, /)
 |      Return hash(self).
 |  
 |  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  __le__(self, value, /)
 |      Return self<=value.
 |  
 |  __len__(self, /)
 |      Return len(self).
 |  
 |  __lt__(self, value, /)
 |      Return self<value.
 |  
 |  __mul__(self, value, /)
 |      Return self*value.
 |  
 |  __ne__(self, value, /)
 |      Return self!=value.
 |  
 |  __rmul__(self, value, /)
 |      Return value*self.
 |  
 |  count(self, value, /)
 |      Return number of occurrences of value.
 |  
 |  index(self, value, start=0, stop=9223372036854775807, /)
 |      Return first index of value.
 |      
 |      Raises ValueError if the value is not present.

FUNCTIONS
    calculate_avg_age(profileList) -> tuple
        Function to average person age
        :param profileList: namedtuple which contains generated fake profiles
        :return: tuple of average person age and time taken to execute this function
    
    calculate_largest_blood_type(profileList) -> tuple
        Function to calculate the blood type with most number of people
        :param profileList: namedtuple which contains generated fake profiles
        :return: tuple of blood type with most number of people and time taken to execute this function
    
    calculate_mean_current_location(profileList) -> tuple
        Function to mean current location
        :param profileList: namedtuple which contains generated fake profiles
        :return: tuple of mean current location (which is a tuple of latitude and longitude coordinates)
        and time taken to execute this function
    
    calculate_oldest_person_age(profileList) -> tuple
        Function to oldest person age
        :param profileList: namedtuple which contains generated fake profiles
        :return: tuple of oldest person age and time taken to execute this function
    
    form_profile_named_tuple() -> NamedTuple.ProfileList
        Function to form the namedtuple which contains 10000 generated fake profiles
        :return: namedtuple which contains generated fake profiles
DATA
    NUM_PROFILE = 10000
    faker = <faker.proxy.Faker object>

### Dict

NAME
    Dict
FUNCTIONS
    calculate_avg_age(profile_dict)
    
    calculate_largest_blood_type(profile_dict) -> tuple
        Function to calculate the blood type with most number of people
        :param profile_dict: dict which contains generated fake profiles
        :return: tuple of blood type with most number of people and time taken to execute this function
    
    calculate_mean_current_location(profile_dict) -> tuple
        Function to mean current location
        :param profile_dict: dict which contains generated fake profiles
        :return: tuple of mean current location (which is a tuple of latitude and longitude coordinates)
        and time taken to execute this function
    
    calculate_oldest_person_age(profile_dict) -> tuple
        Function to oldest person age
        :param profile_dict: dict which contains generated fake profiles
        :return: tuple of oldest person age and time taken to execute this function
    
    form_profile_dict() -> dict
        Function to form the dict which contains 10000 generated fake profiles
        :return: dict which contains generated fake profiles
    
    form_profile_dict_from_namedtuple(profile_named_tuple) -> dict
        Function to form the dict which contains 10000 generated fake profiles, this dict is generated
        from the profile named tuple that us given as parameter
        :return: dict which contains generated fake profiles
DATA
    NUM_PROFILE = 10000
    faker = <faker.proxy.Faker object>


3. Create a fake data (you can use Faker for company names) for imaginary stock exchange for top 100 companies (name, symbol, open, high, close). Assign a random weight to all the companies. Calculate and show what value stock market started at, what was the highest value during the day and where did it end. Make sure your open, high, close are not totally random. You can only use namedtuple. - 500

The driver notebook for 3. is Driver_Stock.ipyb
Sample index price movement that was simulated is as below
Index(open=10.709508534335471, high=10.595688699324919, low=10.787254670554056, close=10.860249128913186)

### Stock
Help on class Stock in module Stock:
class Stock(builtins.tuple)
 |  Stock(name, symbol, open, high, low, close)
 |  
 |  This namedtuple represents a stock and its daily change
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  name
 |      Stock name
 |  
 |  symbol
 |      Stock symbol used on ticker
 |  
 |  open
 |      Day's Opening price of the stock
 |  
 |  high
 |      Day's High price of the stock
 |  
 |  low
 |      Day's low price of the stock
 |  
 |  close
 |      Day's Closing price of the stock
 |  
 |  ----------------------------------------------------------------------
 
 class StockExt(builtins.tuple)
 |  StockExt(name, symbol, open, high, low, close, weight)
 |  
 |  This namedtuple extends a stock and adds the weightage of the stock in the index
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  name
 |      Alias for field number 0
 |  
 |  symbol
 |      Alias for field number 1
 |  
 |  open
 |      Alias for field number 2
 |  
 |  high
 |      Alias for field number 3
 |  
 |  low
 |      Alias for field number 4
 |  
 |  close
 |      Alias for field number 5
 |  
 |  weight
 |      Represents the weightage of the stock in the index
 |  
 |  ----------------------------------------------------------------------

class StockExt(builtins.tuple)
 |  StockExt(name, symbol, open, high, low, close, weight)
 |  
 |  This namedtuple extends a stock and adds the weightage of the stock in the index
 |  
 |  ----------------------------------------------------------------------

class Index(builtins.tuple)
 |  Index(open, high, low, close)
 |  
 |  This namedtuple represents the daily movement of the index
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  open
 |      Day's opening price of the index
 |  
 |  high
 |      Day's high price of the index
 |  
 |  low
 |      Day's low price of the index
 |  
 |  close
 |      Day's close price of the index
 |  
 |  ----------------------------------------------------------------------

FUNCTIONS
    calculate_index(stock_market) -> Stock.Index
        Function to calculate the index's price movement
        :param stock_market: namedtuple representing the stock market which comprises of many stocks
        :return: index namedtuple which contains the index's price movement (open, high, low, close)
    
    create_stock_market() -> Stock.StockMarket
        Function to create random stocks
        :return: namedtuple representing the stock market which comprises of many stocks
    
    get_random_stock() -> Stock.Stock
        Function to create random stock and its day's price movement using faker lib
        :return: randomly generated Stock
    
    get_random_weights(num) -> list
        Functions to create index weightage distribution
        :param num: number of stocks in the market
        :return: list of weights of stocks in the index
DATA
    NUM_COMPANIES = 100
    faker = <faker.proxy.Faker object>
    
## Test Results

test_Dict.py::test_readme_exists PASSED                                  [  5%]
test_Dict.py::test_readme_contents PASSED                                [ 10%]
test_Dict.py::test_readme_proper_description PASSED                      [ 15%]
test_Dict.py::test_readme_file_for_formatting PASSED                     [ 21%]
test_Dict.py::test_indentations PASSED                                   [ 26%]
test_Dict.py::test_function_name_had_cap_letter PASSED                   [ 31%]
test_Dict.py::test_mandatory_fuctions_availability PASSED                [ 36%]
test_Dict.py::test_dict_avg_age PASSED                                   [ 42%]
test_Dict.py::test_dict_oldest_age PASSED                                [ 47%]
test_Dict.py::test_dict_mean_current_location PASSED                     [ 52%]
test_Dict.py::test_dict_largest_blood_grp PASSED                         [ 57%]
test_NamedTuple.py::test_namedtuple_avg_age PASSED                       [ 63%]
test_NamedTuple.py::test_namedtuple_oldest_age PASSED                    [ 68%]
test_NamedTuple.py::test_namedtuple_mean_current_location PASSED         [ 73%]
test_NamedTuple.py::test_namedtuple_largest_blood_grp PASSED             [ 78%]
test_Stock.py::test_weights_add_to_one PASSED                            [ 84%]
test_Stock.py::test_random_stock PASSED                                  [ 89%]
test_Stock.py::test_index PASSED                                         [ 94%]
test_Stock.py::test_index_calculation PASSED                             [100%]

============================== 19 passed in 0.34s ==============================
