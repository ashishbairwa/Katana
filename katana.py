import sys
import os
import shutil

def create_app_py():
    #this file will create a boilerplate for app.py
    try:
        f = open("app.py","w+")
        #populate the file with template
        f.write("""
import os
from flask import Flask, render_template,request
app = Flask(__name__)

from inference import get_call_name

@app.route('/',methods=['GET','POST'])
def hello_world():
	if request.method=='GET':
		return render_template('index.html')
	if request.method=='POST':
		try:
			file=request.files['file']
			image=file.read()
			call_name=get_call_name(image_bytes=image)
			return render_template('result.html',dis=call_name)	
		except:
			return render_template('index.html')
		

if __name__ == '__main__':
	app.run(debug=True,port=os.getenv('PORT',5000))
   """)
    #close the file
        f.close()
    except Exception as e: print(e)

def create_app_json(project_name,project_des):
    
    #this file will create a boilerplate for app.json
    try:
        f = open("app.json","w+")
        f.write("{\n\t\"name\":"+"\""+project_name+"\""+",\n\t\"description\":"+"\""+project_des+"\""+",\n\t\"keywords\":[\"python\",\"flask\",\"Pytorch\"]\n}")
        f.close()
    except Exception as e: print(e)

def create_proc():
    #this file will create a boilerplate for procfile
    try:
        f = open("Procfile","w+")
        f.write("web: gunicorn app:app")
    except Exception as e: print(e)

def create_inference(n):
    #this file will create a boilerplate for inference
    n = int(n)
    classes = []
    for x in range(1,n+1):
        k = str(input("Enter name of class %d : " % x))
        classes.append(k)

    try:
        f = open("inference.py","w+")
        f.write("""
import torch
from commons import get_model,get_tensor

class_names="""+str(classes)+"""
model=get_model()
def get_call_name(image_bytes):
    tensor=get_tensor(image_bytes)
    outputs=model(tensor)
    _,prediction=outputs.max(1)
    category=prediction.item()
    call_name=class_names[category]
    return call_name
    """)
        f.close()
    except Exception as e: print(e)
        
def create_req():
    #this file will create a boilerplate for requirements
    try:
        f = open("requirements.txt","+w")
        f.write("""
Flask==1.0.2
https://download.pytorch.org/whl/cpu/torch-1.0.0-cp37-cp37m-linux_x86_64.whl
torchvision==0.2.1
numpy==1.15.4
Pillow==5.3.0
gunicorn==19.9.0
        """)
    except Exception as e: print(e)
        
def create_run():
    #this file will create a boilerplate for runtime
    try:
        f = open("runtime.txt","+w")
        f.write("python-3.7.1")
        f.close()
    except Exception as e: print(e)

def create_com():
    #this file will create a boilerplate for commons
    try:
        print("\nAlright! Now, enter the classifier code, line by line then hit Ctrl-Z ( windows ) to save it...")
        print("**Make sure that you write it by initiating a new function as class classifier(nn.Module)**")
        contents = []

        while True:
            try:
                line = input()
            except EOFError:
                break
            contents.append(line)

        p = int(input("How many transform have you used in the test loader? : "))
        transforms = []

        for x in range(1,p+1):
            d = input("Enter transform number %d : "  % x)
            transforms.append(d)

        transforms = "[{}]".format(", ".join(transforms))
                     
        checkpoint = str(input("Name of your checkpoint file: "))
        pretrain_name = str(input("Name of the pretrained model: "))
        f = open("commons.py","w+")
        f.write("""
import io
import torch 
import torch.nn as nn
from torchvision import models,transforms
from PIL import Image 

import torch.nn.functional as F


""")
        f.close()
        f = open("commons.py","a")
        for line in contents:
            f.write("%s\n" % line)
        f.close()
        f = open("commons.py","a")
        f.write("""
def get_model():
    checkpoint_path='"""+checkpoint+"""'
    model=models."""+pretrain_name+"""(pretrained=True)
    model.classifier = classifier()
    model.load_state_dict(torch.load(checkpoint_path,map_location='cpu'),strict=False)
    model.eval()
    return model

def get_tensor(image_bytes):
	my_transforms=transforms.Compose("""+str(transforms)+""")
	image=Image.open(io.BytesIO(image_bytes))
	return my_transforms(image).unsqueeze(0)
        """)
        f.close()
        
    except Exception as e: print(e)
        
        
def create_templates():
    #create directories and templates
    try:
        os.mkdir("templates")
        os.mkdir("static")
        os.mkdir("static/styles")
    except OSError:
        print ("Creation of the directories %s failed" % path)
    #writing files for templates including index.html and result.html
    dimension = str(input("Have you resized your images while performing transforms? Give the size: "))
    f = open("index.html","w+")
    f.write("""
<!doctype html>
<html lang="en" class="h-100">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta name="description" content="">
    <meta name=" """+dude_name+""" " content="">
    <title>"""+project_name+"""</title>
    <!--External CSS-->
	<link rel="stylesheet" type="text/css" href="/static/styles/style.css">
    <!-- Bootstrap core CSS -->
	<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
	<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
	<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"></script>
	<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"></script>
	<script>
    function checkFileDetails() {
        var fi = document.getElementById('file');
        if (fi.files.length > 0) { 
            //validation lol script
            for (var i = 0; i <= fi.files.length - 1; i++) {
                var fileName, fileExtension, fileSize, fileType, dateModified;
                fileName = fi.files.item(i).name;
                fileExtension = fileName.replace(/^.*\./, '');
                if (fileExtension == 'jpg' || fileExtension == 'jpeg'||fileExtension == 'JPG') {
                   readImageFile(fi.files.item(i));          
                }
                else {
		    fileSize = fi.files.item(i).size;  
                    fileType = fi.files.item(i).type; 
                    dateModified = fi.files.item(i).lastModifiedDate; 
                    document.getElementById('fileInfo').innerHTML =
                    document.getElementById('fileInfo').innerHTML + '<div class="alert alert-danger" role="alert" id="warn">'+
                            'Only Image files are allowed. Kindly provide images with .jpg and .jpeg extension'+'</div>';
                    document.getElementById('plug').disabled=true;
                }
            }
            function readImageFile(file) {
                var reader = new FileReader(); 
                reader.onload = function (e) {
                    var img = new Image();      
                    img.src = e.target.result;
                    img.onload = function () {
                        var w = this.width;
                        var h = this.height;
                        if(w<"""+dimension+"""||h<"""+dimension+"""){
                        document.getElementById('fileInfo').innerHTML =
                        document.getElementById('fileInfo').innerHTML + '<div class="alert alert-danger" role="alert" id="warn">' +
                                'Provided image is not suitable for processing, Please provide an image greater than width and height 255,255'+'</div>'+'</br>';
                        document.getElementById('plug').disabled=true;
                        }
                        else{
		 	console.log("else triggered");
                        document.getElementById("plug").disabled = false;
			var element = document.getElementById("warn");
                        element.parentNode.removeChild(element);
                        }
                    }
                };
                reader.readAsDataURL(file);
            }
        }
    }
</script>
  </head>
  <body class="d-flex flex-column h-100" style="
    background: #4CA1AF;  /* fallback for old browsers */
    background: -webkit-linear-gradient(to right, #C4E0E5, #4CA1AF);  /* Chrome 10-25, Safari 5.1-6 */
    background: linear-gradient(to right, #C4E0E5, #4CA1AF); /* W3C, IE 10+/ Edge, Firefox 16+, Chrome 26+, Opera 12+, Safari 7+ */
">
	<nav class="navbar navbar-expand-md bg-dark navbar-dark" style="margin-bottom: 5%;">
	  <!-- Brand -->
	  <a class="navbar-brand" href="#">"""+project_name+"""</a>

	  <!-- Toggler/collapsibe Button -->
	  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#collapsibleNavbar">
		<span class="navbar-toggler-icon"></span>
	  </button>

	  <!-- Navbar links -->
	  <div class="collapse navbar-collapse" id="collapsibleNavbar">
		<ul class="navbar-nav">
		  <li class="nav-item">
			<a class="nav-link" href="#">GitHub</a>
		  </li>
		  <li class="nav-item">
			<a class="nav-link" href="#">Information</a>
		  </li>
		  <li class="nav-item">
			<a class="nav-link" href="#">Contributors</a>
		  </li> 
		</ul>
	  </div> 
	</nav>
  
    <!-- Begin page content -->
	<main role="main" class="flex-shrink-0">
	  <div class="container" id="era" style="padding: 0 10% 5% 10%;background: #6962624d;box-shadow: 0px 3px 13px darkgrey;">
		<h1 class="mt-5">Upload an Image</h1>
		
		<form method="POST" enctype="multipart/form-data" >

			<div class="custom-file">
				<input type="file" class="custom-file-input" id="file" required name="file" onchange="checkFileDetails()" >
				<label class="custom-file-label" for="validatedCustomFile">Choose file...</label>
			</div>				
			<div class="col text-center">
				<input class="btn btn-primary btn-lg" id="plug" type="submit" name="upload" style="margin:5%;" disabled="false">
			</div>
			<div id="fileInfo"></div>
		</form>

	  </div>
	</main>

	<footer class="footer mt-auto py-3">
	  <div class="container">
		<span>Created by Katana with <3 &copy; """+dude_name+""" </span>
	  </div>
	</footer>
</body>
</html>

</div>
    """)
    f.close()
        
    f = open("result.html","w+")
    f.write("""    
<!doctype html>
<html lang="en" class="h-100">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta name="description" content="">
    <meta name=" """+dude_name+""" " content="">
    <title>"""+project_name+"""</title>
    <!--External CSS-->
	<link rel="stylesheet" type="text/css" href="{{url_for('static',filename='styles/style.css')}}">
    <!-- Bootstrap core CSS -->
	<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
	<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
	<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"></script>
	<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"></script>
	<script>
     function relocate_home()
     {
     location.href = "/";
     } 
    </script>

  </head>
  <body class="d-flex flex-column h-100" style="
       background: #4CA1AF;  /* fallback for old browsers */
       background: -webkit-linear-gradient(to right, #C4E0E5, #4CA1AF);  /* Chrome 10-25, Safari 5.1-6 */
       background: linear-gradient(to right, #C4E0E5, #4CA1AF); /* W3C, IE 10+/ Edge, Firefox 16+, Chrome 26+, Opera 12+, Safari 7+ */

">
	<nav class="navbar navbar-expand-md bg-dark navbar-dark" style="margin-bottom: 5%;">
	  <!-- Brand -->
	  <a class="navbar-brand" href="#">"""+project_name+"""</a>

	  <!-- Toggler/collapsibe Button -->
	  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#collapsibleNavbar">
		<span class="navbar-toggler-icon"></span>
	  </button>

	  <!-- Navbar links -->
	  <div class="collapse navbar-collapse" id="collapsibleNavbar">
		<ul class="navbar-nav">
		  <li class="nav-item">
			<a class="nav-link" href="#">GitHub</a>
		  </li>
		  <li class="nav-item">
			<a class="nav-link" href="#">Information</a>
		  </li>
		  <li class="nav-item">
			<a class="nav-link" href="#">Contributors</a>
		  </li> 
		</ul>
	  </div> 
	</nav>
  
    <!-- Begin page content -->
	<main role="main" class="flex-shrink-0">
	  <div class="container" id="era" style="padding: 0 10% 5% 10%;background: #6962624d;box-shadow: 0px 3px 13px darkgrey;">
		<h1 class="mt-5">Result</h1>
		<div class="col text-center" style="padding: 3%;">
		<p2>{{ dis }}</p2>
        </div>		
			<div class="col text-center">
				<input type="button" class="btn btn-info" value="Try Again" onclick="relocate_home()">
			</div>
		</form>

	  </div>
	</main>

	<footer class="footer mt-auto py-3">
	  <div class="container">
		<span>Created by Katana with <3 &copy; """+dude_name+""" </span>
	  </div>
	</footer>
</body>
</html>

</div>
""")
    f.close()
        
    f = open("style.css","w+")
    f.write("""
p2{
    font-size: 150%;
    font-family: roboto;
    color: white;
    text-shadow: 0 0 11px #0b0b0cb5;
}
 
 .bd-placeholder-img {
        font-size: 1.125rem;
        text-anchor: middle;
        -webkit-user-select: none;
        -moz-user-select: none;
        -ms-user-select: none;
        user-select: none;
      }
      @media (min-width: 768px) {
        .bd-placeholder-img-lg {
          font-size: 3.5rem;
        }
      }
	
	.container {
	  width: auto;
	  max-width: 680px;
	  padding: 0 15px;
	}
	.footer {
	  background-color: #343a40;
	  color: white;
	}
	
	h1
	{
		text-align: center;
	}
  
  .custom-file-input{
    margin: 20%;
  }
  
  .mt-5, .my-5 {
	color: white;
    margin-top: 3rem!important;
    text-shadow: 0px 2px 5px #474343;
    padding: 8%;
}

.custom-file-input {
    padding: 8%;
    position: relative;
    z-index: 2;
    width: 100%;
    height: calc(1.5em + .75rem + 2px);
    margin: 0;
    opacity: 0;
}

nav.navbar.navbar-expand-md.bg-dark {
    background-color: #343a404f!important;
}

.footer {
    background-color: #2e3c4952;
    color: white;
}
""")
    f.close()

    #move the files in the respective folder

    shutil.move("index.html", "templates/")
    shutil.move("result.html", "templates/")
    shutil.move("style.css", "static/styles/")


    
#Console menu creation
print("""
                                                           
       ██╗  ██╗ █████╗ ████████╗ █████╗ ███╗   ██╗ █████╗ 
       ██║ ██╔╝██╔══██╗╚══██╔══╝██╔══██╗████╗  ██║██╔══██╗
       █████╔╝ ███████║   ██║   ███████║██╔██╗ ██║███████║
       ██╔═██╗ ██╔══██║   ██║   ██╔══██║██║╚██╗██║██╔══██║
       ██║  ██╗██║  ██║   ██║   ██║  ██║██║ ╚████║██║  ██║
       ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝
""")
print(""".______________________________________________________|_._._._._._._._._._.
 \_____________________________________________________|_#_#_#_#_#_#_#_#_#_|
                                                       |""")
print("\n")
print("     =========================================================")
print("     Flask deployment code for image classification in seconds")
print("            https://github.com/ashishbairwa/katana            ")
print("     =========================================================")
print("\n")

print("Let's create your project!")
dude_name = str(input("What's your name btw..? : "))
project_name = str(input("Enter the name of your project :"))
print("Nice name!")
project_des = str(input("Enter a short description to the project: "))
n = input("Can you tell me how many classes do you have in the dataset?: ")
print("Good! Now give me the names:")
create_app_py()
create_app_json(project_name,project_des)
create_proc()
create_inference(n)
create_com()
create_templates()
create_run()
create_req()
print("\n")
print("===========================")
print("Writing app.py...")
print("Writing app.json...")
print("Writing procfile...")
print("Writing inference.py...")
print("Writing requirements.txt...")
print("Writing runtime.txt...")
print("Writing commons.py...")
print("Creating templates...")
print("===========================")
print("\n")
print("Your project files have created successfully...!")
print("\n")
