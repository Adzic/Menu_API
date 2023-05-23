# Menu_API
This is a simple API that takes json files as input and can be called using REST API.  <br>
This repository cointains 20 json files, Menu_api.py and Dockerfile. <br>
There are two endpoints where you can enter **id** or a **food term**. <br>

To run Docker image navigate to the location of the folder in terminal and use this command: <br>
`docker run my-python-app` <br>

Run python script and open your browser. <br>
There you will need to type in:  <br>
http://127.0.0.1:5000//api/customers/1364 or any customer id after the slash.  <br>
![](http://url/to/img.png](https://github.com/Adzic/Menu_API/blob/main/customer_id_example.jpg)

You can also run http://127.0.0.1:5000///api/foods/sandwich (pizza or anything else even if it has two words browser will add %20 in between words)








