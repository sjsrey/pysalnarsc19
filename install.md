# Setup and Installation

Participants are encouraged to use their own laptops in the workshop. 

There are three possible ways to interact with the workshop materials, depending on your preferences and situation:

1. Docker
2. Conda environment
2. binder

The first two options will install packages on your laptop (they vary in how they do this) while the third option does not install any files locally - instead you only need a browser to interact with the materials remotely.


If you choose either of the first two options, you will first need to download the workshop materials.

  
## Obtaining Workshop Materials

If you are familiar with GitHub, you should clone or fork this GitHub repository to a specific directory. Cloning can be done by:

```bash
git clone https://github.com/sjsrey/pysalworkshop.git
```

If you are not using git, you can grab the workshop materials as a zip file by pointing your browser to (https://github.com/sjsrey/geocomputation19.git) and then:

1. Click on the green *Clone or download* button in the upper right
2. Select the `Download Zip` link

![download](https://i.imgur.com/BeiBZmB.png)

This will download the file `pysalworkshop-master.zip` to your downloads directory.  

Once you have downloaded the zip file, extract the archive to a working directory of your choosing. The archive will expand into the directory `pysalworkshop-master`.  

Remember the location of this directory as you will need it for installation options under Docker or conda.



## Docker

This is the recommended approach if you meet the following requirements:

1. You have admin rights over your machine
2. You are running either Windows 10 Pro, macOS, or Linux


The steps to install this (given you meet the requirements above) include:

1. Obtain a copy of Docker and install it:
    * Windows10 Pro/Enterprise: Install Docker Desktop for Windows
    * macOS: Get started with Docker Desktop for Mac

2.  Once Docker is successfully installed, make sure to enable access to your main drive
(e.g. C:\\):
    * Windows10 Pro/Enterprise: Open the preferences for Docker and click the “Shared Drives” tab; click on the drive you want to add and then “Apply”
    * macOS: this feature is automatically enabled 3. Once you have Docker up and running, open up a (Docker) terminal:
    * macOS: Open /Applications/Utilities/Terminal.app
    * Windows10 Pro/Enterprise: Powershell

Then, type on the terminal the following command and hit Enter:

```docker pull sjsrey/pysalworkshop:v1
```

This will take a while to download but, once finished, you will be all ready to go.

Once the command above has finished installing your  stack, you are ready to go!

To get a Jupyter session started, you can follow these steps:

1. Change into the directory where you extracted the pysalworkshop materials 
1. Run on the same terminal as above the following command:

```
docker run --rm -ti -p 8888:8888 -v ${PWD}:/home/jovyan/work sjsrey/pysalworkshop:v1
```

This will start the docker container and you should see something like the
following (your values will be slightly different):

    Executing the command: jupyter notebook
    [I 21:20:24.648 NotebookApp] Writing notebook server cookie secret to /home/jovyan/.local/share/jupyter/runtime/notebook_cookie_secret
    [I 21:20:25.368 NotebookApp] JupyterLab extension loaded from /opt/conda/lib/python3.7/site-packages/jupyterlab
    [I 21:20:25.368 NotebookApp] JupyterLab application directory is /opt/conda/share/jupyter/lab
    [I 21:20:25.637 NotebookApp] [Jupytext Server Extension] Deriving a JupytextContentsManager from LargeFileManager
    [I 21:20:25.645 NotebookApp] Serving notebooks from local directory: /home/jovyan
    [I 21:20:25.646 NotebookApp] The Jupyter Notebook is running at:
    [I 21:20:25.649 NotebookApp] http://4ed41809b61c:8888/?token=88063b001da68e025c8d5809cd244474033b2722b068a022
    [I 21:20:25.650 NotebookApp]  or http://127.0.0.1:8888/?token=88063b001da68e025c8d5809cd244474033b2722b068a022
    [I 21:20:25.652 NotebookApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
    [C 21:20:25.667 NotebookApp]


Copy and paste this URL into your browser:
http://127.0.0.1:8888/?token=88063b001da68e025c8d5809cd244474033b2722b068a022

From the browser dashboard, select the `work` directory, and then the `content` directory to access the notebooks for the workshp.


## Conda environment

If you just want a more minimalist installation that only includes the barebones
of what’s needed in this context, and/or you are not running Windows 10 Pro,
macOS or Linux, the recommended approach is to do a conda installation. This
route will install natively a Python distribution with the libraries we will
need. Please be aware this installation is less stable as it relies on the
specific versions for your OS and latest releases (in most cases it should be
fine, and this particular stack is regularly tested, but some failures
nevertheless happen sometimes).

In this workshop we will use anaconda to build an
[environment](https://conda.io/docs/user-guide/tasks/manage-environments.html)
for **Python 3.6**. It does not matter which version of anaconda is downloaded.
We recommend installing Anaconda 3.7.

- [Windows Anaconda installation instructions](https://docs.anaconda.com/anaconda/install/windows/#)
- [macOS Annaconda installation instructions](https://docs.anaconda.com/anaconda/install/mac-os/#)
- [Linux Anaconda installation instructions](https://docs.anaconda.com/anaconda/install/linux/#)


Once you have installed Anaconda, you can explore the options for interacting with Python through Anaconda: [Getting started with Anaconda](https://docs.anaconda.com/anaconda/user-guide/getting-started/#open-nav-win).

All our work will begin from an [Anaconda prompt](https://docs.anaconda.com/anaconda/user-guide/getting-started/#write-a-python-program-using-anaconda-prompt-or-terminal).

Having read the [Ananconda prompt](https://docs.anaconda.com/anaconda/user-guide/getting-started/#write-a-python-program-using-anaconda-prompt-or-terminal) instructions, start a prompt and
 navigate to the working directory where you extracted the archive in the
*Obtaining Workshop Materials* section above.

For example, if you are on Windows and your user name is `MyName`, and you extracted the archive to:
`C:\Users\MyName\Downloads\pysalworkshop-master` 

then at the Anaconda prompt you would get there with:

```bash
cd C:\Users\MyName\Downloads\pysalworkshop-master
```

Were you instead on macOS you would do:

```bash
cd /Users/MyName/Downloads/pysalworkshop-master
```

Once there, create the workshop environment with:

```bash
conda-env create -f environment.yml
```

This will build a conda python 3+ environment that sandboxes the installation of the required packages for this workshop so we don't break anything in your computer's system Python (if it has one).

This may take 10-15 minutes to complete depending on the speed of your network connection.

Once this completes, you can activate the workshop environment:

* on Mac, Linux:
```bash
source activate pysalworkshop
```
* on Windows:
```bash
activate pysalworkshop
```

### Testing your setup
Next, you will want to test your installation with:
```bash
 jupyter-nbconvert --execute --ExecutePreprocessor.timeout=120 check_workshop.ipynb
```

You should see something like:
```bash
[NbConvertApp] Converting notebook check_workshop.ipynb to html
[NbConvertApp] Executing notebook with kernel: python3
[NbConvertApp] Writing 347535 bytes to check_workshop.html
```

Open check_workshop.html in a browser, and scroll all the way down, you should see something like:

![htmlout](https://i.imgur.com/uLjeLAc.png)

You should also see a new file in the current directory called `inc.png` that contains a map looking something like:

![incmap](https://i.imgur.com/yzEuhXI.png)

If you do see the above, you are ready for the tutorial. If not, please contact me at sjsrey@gmail.com


## Binder

Finally, if you do not wish to, or are unable to, install the packages and software using either of the first two options, you can interact with the workshop materials using a Binder instance. Basically, this is a custom Linux environment running on a remote server that has all the packages and materials installed. To access it, point your web browser to:

https://mybinder.org/v2/gh/sjsrey/pysalworkshop/master

This will start-up an instance of the workshop environment. After a few minutes you will see the jupyter notebook listing of the materials. Select the `contents` folder to access the notebooks.

Please note that while you can interact with the materials using the Binder option, there may be some latency depending on the speed of your internet connection. At any rate, this options give you the ability to work with the materials live during our workshop in the event the Docker or conda options are not feasible.

