<!DOCTYPE html>
<html>

<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="https://stackedit.io/style.css" />
</head>


<body class="stackedit">
  <div class="stackedit__html"><hr>
<hr>
<h1 id="random-hackbright-bot">Random Hackbright Bot</h1>
<h2 id="table-of-contents">Table of Contents</h2>
<ul>
  <li><a href="https://github.com/CoderCarrot/discord_bots/tree/master/hackbright_bot#what-the-bot-does">What the bot does</a></li>
  <li><a href="https://github.com/CoderCarrot/discord_bots/tree/master/hackbright_bot#how-to-add-the-bot-to-your-server">How to add the bot to your server</a></li>
  <li><a href="https://github.com/CoderCarrot/discord_bots/tree/master/hackbright_bot#how-to-start-the-bot">How to start the bot</a>
    <ul>
      <li><a href="https://github.com/CoderCarrot/discord_bots/tree/master/hackbright_bot#online">Online</a></li>
      <li><a href="https://github.com/CoderCarrot/discord_bots/tree/master/hackbright_bot#locally">Locally</a></li>
    </ul>
  </li>
  <li><a href="https://github.com/CoderCarrot/discord_bots/tree/master/hackbright_bot#how-to-use-the-bot">How to use the bot</a>
    <ul>
      <li><a href="https://github.com/CoderCarrot/discord_bots/tree/master/hackbright_bot#pairing">Pairing</a></li>
      <li><a href="https://github.com/CoderCarrot/discord_botstree/master//hackbright_bot#queue-management">Queue Management</a>
        <ul>
          <li><a href="https://github.com/CoderCarrot/discord_bots/tree/master/hackbright_bot#open-queue">Open the queue</a></li>
          <li><a href="https://github.com/CoderCarrot/discord_bots/tree/master/hackbright_bot#close-queue">Close the queue</a></li>
        </ul>
      </li>
    </ul>
  </li>
  <li><a href="https://github.com/CoderCarrot/discord_bots/tree/master/hackbright_bot#things-that-will-break-the-bot">Things that will break the bot</a></li>
</ul>
<h2 id="what-the-bot-does">What the bot does</h2>
<ol>
  <li>Open the Lab Queue channel to student questions/input</li>
  <li>Close the Lab Queue channel to student questions/input</li>
  <li>Get a list of students that will be participating in lab today</li>
  <li>Create pairs from the list of students and assign them to lab rooms</li>
</ol>
<h2 id="how-to-add-the-bot-to-your-server">How to add the bot to your server</h2>
<p>Follow the instruction in <a href="https://realpython.com/how-to-make-a-discord-bot-python/">this article</a>:</p>
<ol>
  <li>
    <p><a href="https://realpython.com/how-to-make-a-discord-bot-python/#how-to-make-a-discord-bot-in-the-developer-portal">How to Make a Discord Bot in the Developer Portal</a></p>
    <ul>
      <li><a href="https://realpython.com/how-to-make-a-discord-bot-python/#creating-an-application">Creating an Application</a></li>
      <li><a href="https://realpython.com/how-to-make-a-discord-bot-python/#creating-a-bot">Creating a Bot</a></li>
      <li><a href="https://realpython.com/how-to-make-a-discord-bot-python/#adding-a-bot-to-a-guild">Adding a Bot to a Guild</a></li>
    </ul>
  </li>
  <li>
      <p>When adding the bot to the Discord channel, make sure it has only the following permissions:</p>
      <ul>
        <li><code>Manage Roles</code></li>
        <li><code>Manage Channels</code></li>
        <li><code>View Channels</code></li>
        <li><code>Send Messages</code></li>
        <li><code>Private Threads</code></li>
        <li><code>Send Messages in Threads</code></li>
        <li><code>Manage Messages</code></li>
        <li><code>Manage Threads</code></li>
        <li><code>Read Message History</code></li>
        <li><code>Mention Everyone</code></li>
      </ul>
  </li>
  <li>
  <p>Make sure all Privileged Gateway Intents are selected<br>
  <img src="http://g.recordit.co/vcDhvAXQeV.gif" alt="Privileged Gateway Intents"></p>
  </li>
</ol>
<h2 id="how-to-start-the-bot">How to start the bot</h2>
<h3 id="online">Online:</h3>
<ol>
  <li>Create a <a href="http://repl.it">repl.it</a>.</li>
  <li>Copy and paste <a href="https://replit.com/join/qkjipoinvw-codercarrot">this code</a> into it.
    <ul>
      <li>Alternatively, you can just run the code without creating your own <a href="http://repl.it">repl.it</a>.</li>
    </ul>
  </li>
  <li>Add your bot token in the Secrets <code>(Environmental variables)</code> section with the key <code>DISCORD_TOKEN</code><br>
  <img src="http://g.recordit.co/idEYvKbnFj.gif" alt="Secrets"></li>
  <li>Run the code before using any of the commands in Discord.<br>
  You will see the following in the console when the bot is connected:<br>
  <img src="http://g.recordit.co/10V1AnPzLi.gif" alt="Connection Message"></li>
</ol>
<p><strong>Note:</strong> <em>To have the bot running all of the time, you will need a premium <a href="http://repl.it">repl.it</a> account.</em></p>
<h3 id="locally">Locally:</h3>
<p>Clone the repo:</p>
<pre><code>$ git clone https://github.com/CoderCarrot/discord_bots.git
</code></pre>
<p>Create a virtual environment:</p>
<pre><code>$ virtualenv env
</code></pre>
<p>Activate the virtual environment:</p>
<pre><code>$ source env/bin/activate
</code></pre>
<p>Install dependencies:</p>
<pre><code>$ pip3 install -r requirements.txt
</code></pre>
<p>Create a file named <code>.env</code> and add your bot token to the file:</p>
<pre><code>DISCORD_TOKEN={bot_client_token}
</code></pre>
<p>Choose <code>Click to Reveal Token</code> and copy the token to replace above.<br>
<img src="http://g.recordit.co/qsU1LQwDax.gif" alt="Get Discord Bot Tokent"></p>
<p>Start/connect the bot:</p>
<pre><code>$ python random_bot.py
</code></pre>
<p>You should see the following in your console:</p>
<pre><code>$ python random_bot.py 
Hackbright Bot has connected to Discord!
</code></pre>
<h2 id="how-to-use-the-bot">How to use the bot</h2>
<h3 id="pairing">Pairing:</h3>
<p>In the <code>lab-pairs</code> channel, type in <code>get students</code> and have the students that will be in lab for the day react to the message.<br>
<img src="http://g.recordit.co/Qy4IanDShm.gif" alt="Get Students"></p>
<p>Once the students are done reacting, type in <code>make pairs</code> and make sure there are no messages between these steps.<br>
<img src="http://g.recordit.co/lyx1XfisAw.gif" alt="Make Pairs"></p>
<h3 id="queue-management">Queue Management:</h3>
<h4 id="open-queue">Open the queue</h4>
<p>In the <code>lab-queue</code> channel, type in <code>queue.open()</code>.</p>
<p>This will change the permissions on the channel so that anyone with a <code>student</code> role will explicitly be able to post in the channel.<br>
<img src="http://g.recordit.co/Op1I5bj5Ut.gif" alt="Allow Student Posting"></p>
<h4 id="close-queue">Close the queue</h4>
<p>In the <code>lab-queue</code> channel, type in <code>queue.close()</code>.</p>
<p>This will change the permissions on the channel so that anyone with a <code>student</code> role will <strong>not</strong> be able to post in the channel.<br>
<img src="http://g.recordit.co/ifvSRkkWhX.gif" alt="Disable Student Posting"></p>
<h2 id="things-that-will-break-the-bot">Things that will break the bot</h2>
<ul>
<li>Renaming the lab queue channel</li>
<li>Renaming the lab pair channel</li>
</ul>
<hr>
<blockquote>
<p>Written with <a href="https://stackedit.io/">StackEdit</a>.</p>
</blockquote>
</div>
</body>

</html>
