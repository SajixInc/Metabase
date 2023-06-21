## <h1>Metabase | business intelligence, dashboards, and data visualization tools</h1>


<img src="https://vivifyassets.s3.ap-south-1.amazonaws.com/lifeeazy-logo1.png" align="right" width="250"/>


<img src="https://vivifyassets.s3.ap-south-1.amazonaws.com/metabase_logo_icon_168103.png"
align="left" width="300" >


<br>
<br>
<br>
<br>
<br>
<br>




<div padding-top=100px><h2 align="left">About Metabase</h2></div>


Metabase is a powerful open-source business intelligence tool that allows you to easily visualize and analyze your data. With Metabase, you can connect to various data sources, create interactive dashboards, and generate insightful reports.

# Features

- Easy Setup: Metabase can be set up quickly with its intuitive installation process.

- Data Visualization: Create beautiful charts, graphs, and dashboards to visualize your data.

- Alerts and Subscriptions: Set up alerts and subscriptions to receive notifications about important data changes.

- Collaboration: Share dashboards and reports with team members for collaborative analysis.

- Embedding: Embed Metabase visualizations and dashboards in other applications or websites.

# Installation 

  1.Prerequisites:

   - First we need to install "Docker" in our local system. For Installation Refer this [Documentation](https://docs.docker.com/desktop/)

   - After "successfully Installation" of Docker in our system check the "version" of the docker with this command in Terminal.
  
                      docker --version

        

  2.To Run The  Metabase In Docker:

  - To Run the "Metabase" in our Docker Refer this [Documentation](https://www.metabase.com/docs/latest/installation-and-operation/start)


  3.Start Metabase:
  
  - After Run The Commands "Metabase" Will start. Then Access your Metabase To Access The metabase Run the localhost in web browser.

              
 4.Access Metabase:

   - Open your web browser and go to [http://localhost:3000](http://localhost:3000/) (default port) to access the Metabase web interface.
   
 5. After close the "Docker" we can open the existing Docker.With the Help of "Container ID".
 
 6. use this command it will shows the Containers in the "Docker" 
            
            docker ps -a

 7. Container ID looks like:
      
       <img src = "https://vivifyassets.s3.ap-south-1.amazonaws.com/Screenshot+from+2023-06-08+16-47-03.png" >
 
 8. use this command to start the required container.
 
            docker start <Container ID>
            
 9. If we want to stop the container use this command
 
            docker stop <Container ID>
 
 10. In Case we want to remove the Container use this command
 
            docker rm <Container Name>
        
 11. Then Run this commands Metabase Will Start But the New Metabase Will Come Not Existing Metabase. Because We remove the existing Metabase with above command.
 
            docker pull metabase/metabase:latest
            
            docker run -d -p 3000:3000 --name metabase metabase/metabase
            
            docker logs -f metabase
 
 12. After run this commands open the [localhost:3000](http://localhost:3000) "Metabase" will open.
              
  

# How To Connect DataBase

  1. After successfully Installation and Run the localhost.
      The webpage looks like:
      
        <img src = "https://vivifyassets.s3.ap-south-1.amazonaws.com/Screenshot+from+2023-06-06+13-02-51.png" >


  2.After click on "Let's get started"  it will ask the preferred language.
      - After That it will ask you about your "Name", "Email", and "Create Password".

  3.Now we can select our databases like "SQL", "MySQL", "MongoDB"  etc..

  4.After Select the DataBase It will ask the 
    "Host", "Database name", "Port", "Username", "Password" of selected DataBase.

  5.After successfully connected to the database. We can see our connected Databases.
    
   <img src = "https://vivifyassets.s3.ap-south-1.amazonaws.com/metabase.png" >


# How To Create dashboards

  1.Click on the "+ NEW" button on the top right corner of the Metabase interface.
  
   <img src = "https://vivifyassets.s3.ap-south-1.amazonaws.com/Screenshot+from+2023-06-06+14-45-50.png">

  2.After click on + NEW button Their is an another button "Question" click on it.

  3.Select a database and table to build your query.

  4.Configure your query by selecting fields, applying filters, and specifying aggregations.

  5.After Applying some filters we have to use the "Summarize" button for Available of different Charts.

   <img src = "https://vivifyassets.s3.ap-south-1.amazonaws.com/Screenshot+from+2023-06-07+17-34-50...png">
  
  6.Select any Chart option From the Available list for Data Visualization. 

      It's looks like:

   <img src = https://vivifyassets.s3.ap-south-1.amazonaws.com/Screenshot+from+2023-06-07+17-34-50+(1).png>


  7.Click on "Save" to save the question for later use.


# How To Share the Dashboard Link

1. After save the Dashboard open the "Dashboard" and we have an option for sharing in the "Right Bottom of the Dashboard".
 
   <img src = "https://vivifyassets.s3.ap-south-1.amazonaws.com/Screenshot+from+2023-06-07+16-50-08+(1).png">
   
2. Click on the sharing option it will ask you the  "Enable sharing".
3. Turn on the "Enable sharing" option.
4. Then it will Visible the "Public link" and Public embed" links.
5. "Public link" is used to Share this question with people who don't have a Metabase account. They can use this "Public link" URL.
6. "Public embed" is used to Embed this question in blog posts or web pages by copying and pasting the snippet.
    
    Both the "Public link" and "Public embed" looks like:
    
    <img src = "https://vivifyassets.s3.ap-south-1.amazonaws.com/Screenshot+from+2023-06-07+15-49-48.png">
    
 7. And we have an Another Sharing option but we have to implementing this "setup" in our "Application" like "Django", "Node", "Rails" and "Laravel".
 
      If we want to implement this Dashboards in "Application" Refer This [Document](https://github.com/metabase/embedding-reference-apps)
      
   
   
# Output Of The Created Dashboards

   <img src = "https://vivifyassets.s3.ap-south-1.amazonaws.com/Screenshot+from+2023-06-07+16-50-08.png">
    





# <hr>



# Embedding Metabase dashboard in Application with Python using API's


### Prerequisites:

Before proceeding, ensure that you have the following dependencies installed:

- Python 3.x

- PyJWT library (can be installed via pip)



### Installation:


To implement JWT authentication for Metabase embedding in your Python(Django) application, follow these steps:

1.Navigate to your project directory

2.Run the command "pip install PyJWT" to install the necessary dependency.

3.create an App and Project with these commands.



For Project Creation command

        django-admin startproject <project name>


For App creation command

        django-admin startapp <App name>


4.In "Views.py" Copy this Embed Code from the metabase.

<img src = "https://vivifyassets.s3.ap-south-1.amazonaws.com/Screenshot+from+2023-06-20+13-00-44.png">


5.create a urls.py file in App and write the urls.


6.In Project settings write the App name in "INSTALLED_APPS".

7.If any doubts refer the code in "main".

8.Then Run The server with this command.

        python manage.py runserver

9.Then open the localhost it will show like this.

<img src = "https://vivifyassets.s3.ap-south-1.amazonaws.com/metabaselocalhost.png">

10.open the path name which is given in the urls.

11.Then it will show the link open that link it will show the dashboard.


NOTE: This code is used for only  "One Dashboard"will be shown.


### How to Generate Multiple Dashboards Using Swagger:


1.If we want to generate the "multiple Dashboard Links" use this code in Views.py.


        from rest_framework import generics
        from rest_framework.permissions import IsAuthenticated
        from rest_framework.response import Response
        from genericresponse import GenericResponse
        from django.http import JsonResponse
        import jwt
        import time

        METABASE_SITE_URL = "<metabase url>"
        METABASE_SECRET_KEY = "<Metabase secret key>"


        question_list = [26,27,28,29]

    class metabaseclass(generics.GenericAPIView):
        # serializer_class = IvinSerializer
          permission_classes = (IsAuthenticated,)


    def get(self, request):
        try:
            url = []
            # Apicall(26)
            for i in question_list:
                iframeUrl = Apicall(i)
                url.append(iframeUrl)
            
            dic = {
                'total voters':url[0],
                'village voters':url[1],
                'madugula voters by lastname':url[2],
                'village voters by lastname':url[3],

            }
            print(dic)
            return Response({'Message': 'Successful',
                             'Result': dic,
                             'HasError': False,
                             'Status': 200})
        except:
            return Response({'Message': 'fail',
                             'Result': "fail",
                             'HasError': True,
                             'Status': 400})



     def Apicall(question_number):
        payload = {
                "resource": {"question": question_number},
                "params": {},
                # "exp": round(time.time()) + (60 * 20)  # 10 minute expiration
        }
   
    token = jwt.encode(payload, METABASE_SECRET_KEY, algorithm="HS256")
    
    iframeUrl = METABASE_SITE_URL + "/embed/question/" + token + "#bordered=true&titled=true"
    
    return iframeUrl

2.use this code for multiple Dashboard Links.

3.If we want to use this code we must Connect this to "swagger".

4.For Swagger Connection Refer this Documentation [Click Here](https://drf-yasg.readthedocs.io/en/stable/readme.html)

5.After Successfully Connected To swagger Their is a name with what we are give in urls.

  <img src = "https://vivifyassets.s3.ap-south-1.amazonaws.com/Screenshot+from+2023-06-20+17-30-40.png">

6.we can see All The End Points in that name.

7.once we are open that endpoint it will show the output.

## Output:

 <img src = "https://vivifyassets.s3.ap-south-1.amazonaws.com/Screenshot+from+2023-06-07+16-50-08.png">




<hr>

<p align="center">
<img src="https://vivifyassets.s3.ap-south-1.amazonaws.com/cropped-vivify_login.png" margin_left="100"/>
</p>













