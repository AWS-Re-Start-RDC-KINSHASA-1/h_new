<center><h5>Hello everyone, this process summarizes how to install "Patroni" on Debian OS</h5></center>
<pre>academy@DESKTOP:~$ sudo apt update</pre>
<pre>academy@DESKTOP:~$ sudo apt upgrade -y</pre>
<br>
<h5>We install dependencies because they are modules or packages that your Python code needs to work.</h5>
<pre>academy@DESKTOP:~$ sudo apt install python3-pip python3-psycopg2 python3-etcd python3-yaml python3-systemd</pre>
<br>
<h5>this line of code installs patroni with etcd support</h5>
<pre>academy@DESKTOP:~$ sudo pip3 install patroni[etcd]</pre>
<pre class="warning">**ATTENTION :** If an error message occurs, it is caused by a externally managed environment ! <br>To fix it please follow the following steps:</pre>
<br>
<h5>this command line allows you to create a python environment</h5>
<pre>academy@DESKTOP:~$ sudo apt install python3-venv -y</pre>
<br>
<h5>This command line creates a my_env folder that contains a copy of the Python 3 interpreter and its standard modules. The virtual environment is enabled by default, which means that Python commands executed in this environment will use the modules installed in the virtual environment and not the modules installed at the system level.</h5>
<pre>academy@DESKTOP:~$ sudo python3 -m venv mon_env</pre>
<pre>academy@DESKTOP:~$ source mon_env/bin/activate</pre>
<pre>academy@DESKTOP:~$ sudo pip install patroni[etcd]</pre>
<h5>If the error persists you can use this:</h5>
<pre>academy@DESKTOP:~$ pip install patroni --ignore-installed --no-cache-dir --force-reinstall --break-system-packages</pre>
<h5><u>Note:</u>This procedure may not install all files so it is important to install the missing files.</h5>
<h5>The configuration file is not explained at the moment...</h5>
