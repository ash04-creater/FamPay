## Youtube Intermediary Search
-----------------------------------------------------------------------------------------------

The backend has been divided into two parts : client_server and microservice.

Firstly, the microservice needs to be run (which will trigger the youtube_data_api every 10 seconds and the videos will be stored in the database) and then the client_server needs to be run will connect the apis with the postgresql database

------------------------------------------------------------------------------------------------

### **Setup for both the modules**

A virtual environment needs to be created :

> `py -m venv env `   
> `.\env\Scripts\activate`

Dependencies needs to be installed :

> `pip install -r requirements.txt`  


------------------------------------------------------------------------------------------------

### **microservice**

The `variables.ini` file should be configured with the **databse credentials** and the youtube data api's **developer key**.

The following commands needs to be executed :

>`py createTable.py`        ---> To create the database table  
>`py insertTable.py`        ---> To store the youtube api response in the databse periodically


------------------------------------------------------------------------------------------------

### **client_server**

A `.env` file needs to be created with stores the `SQLALCHEMY_DATABASE_URI` and the `SCHEMA_NAME`

For example,

SQLALCHEMY_DATABASE_URI ="postgresql://postgres:root@127.0.0.1:5432/postgres"  
SCHEMA_NAME ="public"

Then the following command needs to be executed :

>`py run.py`                 ---> To run the flask server    

#### **Two apis** are available here .

>`get()`          --> To get the paginated response of the videos added in the database   

The get() api is called by requesting response at [http://127.0.0.1:5000/get/pageNumber](http://127.0.0.1:5000/get/pageNumber)

_where pageNumber should be integer page no.s_

**Sample url** : http://127.0.0.1:5000/get/2

>`search_video()`  --> To get the search result from the database    

The search_video() api is called by requesting response at http://127.0.0.1:5000/search/video/searchKey

_where searchKey should be string input_

**Sample url** : http://127.0.0.1:5000/search/video/virat$kohli








   
