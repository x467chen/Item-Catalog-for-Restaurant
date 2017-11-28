# Item Catalog for Restaurant

## Synopsis
This application allows users to read some restaurants infomation and their menu. Besides, this app also provides a user registration and authentication system which means the user can safely add, edit and delete their restaurants and menu item and store the status with database after ahthentication and authorization. All the data in this application are provided in a JSON endpoint.


## Motivaton
Through this project, I am more familiar with developing a RESTful web application using the Python framework Flask and implementing third-party OAuth authentication such as Google+ and Facebook. Besside, I also learnt when to properly use the various HTTP methods and how these methods relate to CRUD (create, read, update and delete) operations. I learnt how to write developer-friendly APIs in JSON endpoint. Findlly, I am more experienced with using Boostrap to design UX websites.



## Installation
1.Preparation<br />
Install Python2.7<br />
Install [Vagrant](https://www.vagrantup.com/) and [VirtualBox](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1).<br />



2.Clone the github repository into a vagrant environment using the cmd:
``` xml
git clone https://github.com/x467chen/Item-Catalog-for-Restaurant
```
3.Configure and open your repo by the following cmd:
``` xml
vagrant up
vagrant ssh
cd /vagrant/
```
4.Add some data into database by the following cmd:
``` xml
python userData.py
```

5.Setup the database by the following cmd:
``` xml
python database_setup.py
```

6.Start the program by the following cmd:
``` xml
python project.py
```

7.Open your browser and visit [http://localhost:8000](http://localhost:8000) to explore this app<br />

8.If you want yourself OAuth 2.0<br />
Go to [Google Official Website](http://console.developers.google.com) to set up a client id and client secret.<br />
You can also do the same implenment from other third party OAuth authentication such as [Facebook](https://developers.facebook.com/)
