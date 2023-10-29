[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/qg4qXfSB)

<h2>1.Prerequisites.</h2> 
<p>Before you can use this application, you will need to ensure that you have Python installed on your system. If you don't have Python installed, you can visit the official Python website at https://www.python.org/, and download for your OS.</p>


<h2>2.Set Up Environment (via Git command).</h2>
<p>Step 1. Create folder on your desktop. Name it as you wish. For example, "test".<br>
Step 2. Go to my github repository (https://github.com/ADA-GWU/processes-and-asynchronous-messaging-ShamsiyyaAlakbarova). <br>
Step 3. Press to green CODE button, and copy HTTPS link (https://github.com/ADA-GWU/processes-and-asynchronous-messaging-ShamsiyyaAlakbarova.git).<br>
Step 4. Open your terminal, and enter into your newly created folder "test". You can do this
by running these commands:<br>
cd Desktop<br>
cd test<br>
After running these two commands, you will be inside your "test" folder.<br>
Step 5. Next clone my repo by pasting copied HTTPS link. <br>
Run this command: git clone https://github.com/ADA-GWU/processes-and-asynchronous-messaging-ShamsiyyaAlakbarova.git<br>
Step 6. Run this command: cd processes-and-asynchronous-messaging-ShamsiyyaAlakbarova. Now you are in the repo, and can start to use the application.</p>

<p>P.S. if you encounter issues while trying to clone a repository using a Git command, you can indeed download the repository as a ZIP file from the repository's web page.</p>


<h2>3.Run the Application.</h2>
<p>Step 1. Open 2 terminal windows. 1 window is for sender, and 1 window is for reader.<br>
Step 2. In each terminal window you should be inside the repo.<br> 
Commands: cd Desktop  => cd test => cd processes-and-asynchronous-messaging-ShamsiyyaAlakbarova.<br>  
Step 3. In first terminal run this command: python sender.py. In second terminal run this command: python reader.py.<br>
After running this commands, you will see this outputs: First terminal's output: "Enter a message (or 'exit' to quit):
". It means, that it waits for your message input. Second terminal's output: "Reader is listening...
Press 'q' and Enter to stop the reader."<br>
Step 4. Write an input (some message) in sender terminal. For example: hello.<br>
After your entered an input you should go to reader terminal and press "Enter". After you will be able to see output in reader terminal. In "hello" case the output will be: "Sender Shamsiyya sent "hello" at time 2023-10-29 13:38:40"<br>
Step 5. If we check our database, we will see that this record is saved there.<br></p>
