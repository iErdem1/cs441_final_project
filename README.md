# Final Project
- Binghamton University Spring 2019 CS441 Gaming for Mobile Platform class Final project.

## LICENCE

```
Copyright 2019 A. Ihsan Erdem <ihsan@itugnu.org>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
```

## Installation for Debian Based GNU/Linux Distros
- Clone project from Git
- Use Python version 3.6.x
- Run <code>pip install -r requirements.txt</code> or install **virtualenv** manually
- Setup virtualenv <code>virtualenv venv -p python3.6</code>
- Activate virtualenv <code>source venv/bin/activate</code>
- To install Kivy:
```bash
    $ sudo add-apt-repository ppa:kivy-team/kivy
    $ sudo apt-get update
    $ sudo apt-install python3-kivy
```
- On project directory create a <code>img</code> subdirectory and add some images.
- To run the program you may use <code>python3 main.py</code> command on terminal.
 

## Project Description
- Project based on Kivy Framework which is Python's cross platform application 
builder.
- Kivy is basically a cross platform graphical interface library of Python.
You can develop desktop applications and also you can build your app to Android and
iOS via Buildozer. Kivy use pygame as an engine. Also, render window tools via SDL and OpenGL
so Kivy apps do not look like native iOS and Android applications.
- Kivy is a Free Software and licenced under MIT. So if you want to check source code you can
go <https://github.com/kivy/kivy>
- Project is basic tennis like game.
- Ball (My friends head in this case:)) has to reach opponents side
on the board.
- We can control size of the board and other features via our kivy
files.
- Collisions controlled by kivy's own packages and libraries.
- We use Clock feature to control movement.

- Game is getting harder in every hit, velocity of the ball is
increasing.(I am planning to update this, increase rate is too much)
- Before demo I am also planning to fix known bugs.
