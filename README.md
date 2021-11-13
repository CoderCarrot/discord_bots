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
<h1 id="hackbright-bot">Hackbright Bot</h1>
<h2 id="table-of-contents">Table of Contents</h2>
<ul>
<li>What the bot does</li>
<li>How to add the bot to your server</li>
<li>How to use the bot</li>
<li>Things that will break the bot</li>
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
<ul>
<li><a href="https://realpython.com/how-to-make-a-discord-bot-python/#how-to-make-a-discord-bot-in-the-developer-portal">How to Make a Discord Bot in the Developer Portal</a>
<ul>
<li><a href="https://realpython.com/how-to-make-a-discord-bot-python/#creating-an-application">Creating an Application</a></li>
<li><a href="https://realpython.com/how-to-make-a-discord-bot-python/#creating-a-bot">Creating a Bot</a></li>
<li><a href="https://realpython.com/how-to-make-a-discord-bot-python/#adding-a-bot-to-a-guild">Adding a Bot to a Guild</a></li>
</ul>
</li>
</ul>
<h2 id="how-to-use-the-bot">How to use the bot</h2>
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
<img src="http://g.recordit.co/qsU1LQwDax.gif" alt="Get Discord Bot Tokent"><br>
Start/connect the bot:</p>
<pre><code>$ python bot_connect.py
</code></pre>
<p>You should see the following in your console:</p>
<pre><code>$ python bot_connect.py 
Hackbright Bot has connected to Discord!
</code></pre>
<h2 id="things-that-will-break-the-bot">Things that will break the bot</h2>
<blockquote>
<p>Written with <a href="https://stackedit.io/">StackEdit</a>.</p>
</blockquote>
</div>
</body>

</html>
